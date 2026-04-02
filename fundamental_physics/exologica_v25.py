import numpy as np
import emcee
import corner
import matplotlib.pyplot as plt
from tqdm import tqdm

# =================================================================
# 1. КОНФИГУРАЦИЯ И ВЫБОР ЦЕЛИ (WD 1145+017)
# =================================================================
TARGET = "WD 1145+017"  
c = 299792.458  # км/с

# Данные для WD 1145+017 (Сильнейшая аккреция)
z_grav_ref = 28.6 / c
obs_ls = [4.67385, 2.34582, 1.55985, 1.18292]
color_plot = "darkorange"

# Коэффициенты для линий (Appendix A2) - Физическая параметризация Sp
lines_db = [
    {"name": "CO v(1-0) P(1)", "l_0": 4.67343, "K_mu": 0.4981, "K_a": 0.0,    "S_p": 0.001},
    {"name": "CO v(2-0) R(2)", "l_0": 2.34560, "K_mu": 0.4992, "K_a": 0.0,    "S_p": 0.001},
    {"name": "Fe I (NIR)",     "l_0": 1.55970, "K_mu": 0.0,    "K_a": 0.021,  "S_p": 0.010},
    {"name": "Mg I (NIR)",     "l_0": 1.18280, "K_mu": 0.0,    "K_a": -0.005, "S_p": 0.008}
]

# =================================================================
# 2. BAYESIAN ENGINE (Likelihood & Priors v2.5)
# =================================================================

def log_prior(theta):
    z_c, dmu, da, P = theta
    # Информативные априорные вероятности (Регуляризация)
    lp_z = -0.5 * (z_c / 1e-6)**2    
    lp_dmu = -0.5 * (dmu / 1e-7)**2  
    lp_da = -0.5 * (da / 1e-8)**2
    lp_P = -0.5 * (P / 1.0)**2      
    
    # Жесткие границы физического смысла
    if -1e-5 < dmu < 1e-5 and -1e-6 < da < 1e-6 and -5.0 < P < 5.0:
        return lp_z + lp_dmu + lp_da + lp_P
    return -np.inf

def log_likelihood(theta, obs_lambdas, db):
    z_c, dmu, da, P = theta
    chi2 = 0
    for i, line in enumerate(db):
        model_z = (z_grav_ref + z_c) + (line["K_mu"] * dmu) + (line["K_a"] * da) + (line["S_p"] * P / c)
        l_calc = line["l_0"] * (1 + model_z)
        
        # Ошибка JWST (3 км/с - золотой стандарт)
        sigma_v = 3.0 
        sigma = line["l_0"] * (sigma_v / c)
        chi2 += ((obs_lambdas[i] - l_calc) / sigma)**2
    return -0.5 * chi2

def log_probability(theta, obs_lambdas, db):
    lp = log_prior(theta)
    if not np.isfinite(lp): return -np.inf
    return lp + log_likelihood(theta, obs_lambdas, db)

# =================================================================
# 3. ВЫЧИСЛЕНИЯ MCMC (15,000 шагов)
# =================================================================

print(f">>> ExoLogica AI: Прецизионный анализ цели {TARGET}...")
ndim, nwalkers, nsteps = 4, 32, 15000

# Старт из нулевой точки
p0 = [np.zeros(ndim) + 1e-9 * np.random.randn(ndim) for i in range(nwalkers)]

sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, args=(obs_ls, lines_db))

# Прогресс-бар
for _ in tqdm(sampler.sample(p0, iterations=nsteps), total=nsteps):
    pass

# =================================================================
# 4. ОБРАБОТКА РЕЗУЛЬТАТОВ И ОБНОВЛЕННАЯ ВИЗУАЛИЗАЦИЯ
# =================================================================

samples = sampler.get_chain(discard=3000, thin=20, flat=True)
labels = [r"$z_{corr}$", r"$\Delta\mu/\mu$", r"$\Delta\alpha/\alpha$", r"$P_{eff}$"]
results = np.percentile(samples, [16, 50, 84], axis=0)

print(f"\n--- ПРЕЦИЗИОННЫЙ ОТЧЕТ ПО {TARGET} ---")
for i in range(ndim):
    val = results[1, i]
    print(f"{labels[i]:<15}: {val:10.4e} (± {(results[2,i]-results[0,i])/2:.2e})")

# === ВОТ ЗДЕСЬ ПРАВКА ===
# Мы изменили title_fmt=".2e" на title_fmt=".3e"
fig = corner.corner(samples, labels=labels, show_titles=True, 
                    title_fmt=".3e", color=color_plot, truths=[0,0,0,0])
# =======================

plt.suptitle(f"ExoLogica v2.5.1 Precision: {TARGET}")
plt.savefig(f"ExoLogica_{TARGET.replace(' ', '_')}_Precision.png")
print(f"\n[OK] График сохранен: ExoLogica_{TARGET.replace(' ', '_')}_Precision.png")
plt.show()
