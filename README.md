# 🌌 ExoLogica AI: The Multimodal Framework for Astrophysics
### (ExoLogica AI: Мультимодальный фреймворк для астрофизики)

> **Abstract:** ExoLogica AI is an advanced scientific ecosystem that combines Bayesian inference, MCMC sampling, and planetary density analysis to solve two of the greatest mysteries in space science: the physical constraints on habitability and the stability of universal constants.
>
> **Аннотация:** ExoLogica AI — это передовая научная экосистема, сочетающая байесовский вывод, сэмплирование MCMC и анализ плотности планет для решения двух величайших загадок космической науки: физических ограничений обитаемости и стабильности мировых констант.

---

## 🪐 Module 1: The Critical Density Law (Astrobiology)
### (Модуль 1: Закон Критической Плотности — Астробиология)

Our research proves that stable Earth-type biospheres can only exist within a narrow **Critical Density Window**:
**Наше исследование доказывает, что стабильные биосферы земного типа могут существовать только в узком «Критическом Окне Плотности»:**

$$4.8 \le \rho \le 7.8 \text{ g/cm}^3$$

* **Optimum Density ($\rho_{opt}$):** $\approx 6.26 \text{ g/cm}^3$ (The "ExoLogica Peak").
* **PRI (Planetary Retainability Index):** Our proprietary metric that replaces the obsolete ESI. It measures a planet's ability to maintain geochemical cycles and a magnetic dynamo.

---

## ⚛️ Module 2: Fundamental Physics Engine (MCMC)
### (Модуль 2: Движок Фундаментальной Физики — MCMC)

We utilize the **Many-Multiplet method** and high-resolution **JWST NIRSpec** spectra to test the variation of fundamental constants ($\alpha$ and $\mu$) in strong gravitational fields ($\log g \approx 8$).
**Мы используем метод многих мультиплетов и спектры JWST для проверки вариации фундаментальных констант в сильных гравитационных полях.**

* **Precision (Точность):** Achieved constraints up to $10^{-10}$ for $\Delta\mu/\mu$ and $\Delta\alpha/\alpha$.
* **Bayesian Inference:** Integrated `emcee` sampler for parameter decoupling ($z_{corr}$, constants, and pressure shifts).
* **Targets:** Successfully validated on **GD 362** and **WD 1145+017**.

---

## 📊 Key Discoveries / Ключевые Открытия

1.  **Habitability:** Analyzed 9,800+ exoplanets. Life-friendly environments are strictly limited by internal structure, not just orbital distance.
2.  **Physics:** No "New Physics" detected at the $10^{-10}$ level, confirming General Relativity's robustness in the strong-field regime.

---

## 🛠 Project Structure / Структура Проекта

* `/habitability`: Python tools for density analysis and the **PRI** calculation.
* `/fundamental_physics`: The MCMC engine (`exologica_v25.py`) for spectral analysis.
* `/data`: Validated datasets (`ExoLogica_Export-s.csv`) with 9,800+ objects.
* `/plots`: Precision posterior distributions (Corner Plots).

---

## 🧪 How to Use / Как Использовать

### Installation / Установка:
```bash
pip install pandas numpy scipy matplotlib emcee corner tqdm
