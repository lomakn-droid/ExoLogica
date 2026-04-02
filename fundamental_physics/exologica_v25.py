import numpy as np
import emcee
import corner
import matplotlib.pyplot as plt
from tqdm import tqdm

# --- ВЫБОР ОБЪЕКТА ---
TARGET = "WD 1145+017" # Или "GD 362"
c = 299792.458

if TARGET == "GD 362":
    z_grav_ref = 42.4 / c
    obs_ls = [4.67409, 2.34593, 1.55992, 1.18297]
    color_p = "teal"
else:
    z_grav_ref = 28.6 / c
    obs_ls = [4.67385, 2.34582, 1.55985, 1.18292]
    color_p = "darkorange"

# Параметры линий: K_mu (масса протона), K_alpha (тонкая структура), S_p (давление)
lines_db = [
    {"name": "CO v(1-0) P(1)", "l_0": 4.67343, "K_mu": 0.4981, "K_a": 0.0,    "S_p": 0.001},
    {"name": "CO v(2-0) R(2)", "l_0": 2.34560, "K_mu": 0.4992, "K_a": 0.0,    "S_p": 0.001},
    {"name": "Fe I (NIR)",     "l_0": 1.55970, "K_mu": 0.0,    "K_a": 0.021,  "S_p": 0.010},
    {"name": "Mg I (NIR)",     "l_0": 1.18280, "K_mu": 0.0,    "K_a": -0.005, "S_p": 0.008}
]

# --- BAYESIAN LOGIC ---
def log_prior(theta):
    z_c, dmu, da, P = theta
    # Регуляризация (запрещаем модели уходить в нефизичные дебри)
    if -1e-5 < dmu < 1e-5 and -1e-6 < da < 1e-6 and -5e-6 < z_c < 5e-6 and -2.0 < P < 2.0:
        return -0.5 * (z_c / 1e-6)**2 # Gaussian prior on z_corr
    return -np.inf

def log_likelihood(theta, obs_lambdas, db):
    z_c, dmu, da, P = theta
    chi2 = 0
    for i, line in enumerate(db):
        model_z = (z_grav_ref + z_c) + (line["K_mu"] * dmu) + (line["K_a"] * da) + (line["S_p"] * P / c)
        l_calc = line["l_0"] * (1 + model_z)
        sigma = line["l_0"] * 3e-6 # Точность калибровки ~3 км/с
        chi2 += ((obs_lambdas[i] - l_calc) / sigma)**2
    return -0.5 * chi2

def log_probability(theta, obs, db):
    lp = log_prior(theta)
    return lp + log_likelihood(theta, obs, db) if np.isfinite(lp) else -np.inf

# --- EXECUTION ---
print(f">>> Запуск ExoLogica MCMC для {TARGET}...")
ndim, nwalkers, nsteps = 4, 32, 15000
p0 = [np.zeros(ndim) + 1e-9 * np.random.randn(ndim) for i in range(nwalkers)]
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, args=(obs_ls, lines_db))

for _ in tqdm(sampler.sample(p0, iterations=nsteps), total=nsteps): pass

# --- ВИЗУАЛИЗАЦИЯ ---
samples = sampler.get_chain(discard=3000, thin=20, flat=True)
labels = [r"$z_{corr}$", r"$\Delta\mu/\mu$", r"$\Delta\alpha/\alpha$", r"$P_{eff}$"]
corner.corner(samples, labels=labels, show_titles=True, color=color_p, truths=[0,0,0,0])
plt.savefig(f"exologica_physics_{TARGET}.png")
plt.show()
