# ⚙️ ExoLogica AI: System Architecture & Technical Overview
# (ExoLogica AI: Архитектура системы и технический обзор)

> **Abstract:** This document details the technical architecture of the **ExoLogica AI** engine (v2.0), a hybrid astrophysical simulator designed to analyze exoplanet habitability. Unlike traditional statistical models, ExoLogica combines **Bayesian inference**, **physics-based equation-of-state modeling**, and **Machine Learning (XGBoost)** to reconstruct missing planetary parameters and calculate the novel **PRI (Planetary Retainability Index)**.
>
> **(Аннотация:** Данный документ описывает техническую архитектуру движка **ExoLogica AI** (версия 2.0) — гибридного астрофизического симулятора для анализа обитаемости экзопланет. В отличие от традиционных статистических моделей, ExoLogica объединяет **байесовский вывод**, **физическое моделирование уравнений состояния** и **машинное обучение (XGBoost)** для восстановления недостающих параметров планет и расчета нового индекса **PRI (Индекс Удерживаемости Планеты)**.)

---

## 1. Technology Stack / Технологический Стек

The ExoLogica pipeline is built using modern Python data science libraries, optimized for high-performance numerical computing.
**(Конвейер ExoLogica построен с использованием современных библиотек науки о данных на Python, оптимизированных для высокопроизводительных численных вычислений.)**

| Component / Компонент | Technology / Технология | Purpose / Назначение |
| :--- | :--- | :--- |
| **Core Language** | Python 3.9+ | Main execution environment. |
| **Data Processing** | `pandas`, `numpy` | Handling large datasets (9,800+ rows), cleaning, and vectorization. |
| **Statistical Inference** | `scipy`, `statsmodels` | Bayesian mass reconstruction, curve fitting (Gaussian regression). |
| **Machine Learning** | `xgboost`, `scikit-learn` | Classification of planet types, PRI prediction, anomaly detection. |
| **Visualization** | `matplotlib`, `seaborn` | Generating publication-quality plots (Habitability Gaussian, Spectra). |
| **GUI Framework** | `tkinter` | User-friendly interface for local analysis (`exologica_spectra.py`). |
| **Physics Engine** | Custom Python Modules | Implementation of Zeng et al. (2016) Mass-Radius relations, Ice VII phase diagrams. |

---

## 2. The 14-Stage Analysis Pipeline / 14-ступенчатый Конвейер Анализа

The core of ExoLogica is a sequential processing pipeline that transforms raw observational data into a refined habitability score. Each stage applies specific physical laws or algorithms.
**(Ядром ExoLogica является последовательный конвейер обработки, который преобразует сырые наблюдательные данные в уточненный индекс обитаемости. Каждый этап применяет特定的 физические законы или алгоритмы.)**

### Phase 1: Data Ingestion & Cleaning (Этапы 1-3)
1.  **Aggregation:** Merging data from NASA Exoplanet Archive, Kepler, TESS, K2, and radial velocity surveys.
    *(Агрегация: Объединение данных из архива NASA и различных миссий.)*
2.  **Noise Filtering:** Removing false positives, instrumental artifacts, and stars with insufficient metadata.
    *(Фильтрация шума: Удаление ложных срабатываний и артефактов.)*
3.  **Unit Normalization:** Converting all parameters to SI units or standard astronomical units ($M_\oplus$, $R_\oplus$, $g/cm^3$).
    *(Нормализация единиц: Приведение всех параметров к стандартным единицам.)*

### Phase 2: Parameter Reconstruction (Этапы 4-7)
4.  **Mass Reconstruction (Bayesian):** For planets with known radius but unknown mass, we apply a Bayesian probabilistic model based on the Chen & Kipping (2017) mass-radius relation to estimate $M_p$ with uncertainty bounds.
    *(Реконструкция массы: Байесовская оценка массы для планет с известным радиусом.)*
5.  **Density Calculation:** Precise computation of bulk density $\rho = \frac{M}{V}$ with error propagation analysis.
    *(Расчет плотности: Точный вычисление средней плотности с анализом погрешностей.)*
6.  **Thermal Equilibrium:** Calculating equilibrium temperature $T_{eq}$ considering albedo variations for different surface types (Ocean vs. Rock).
    *(Тепловое равновесие: Расчет равновесной температуры с учетом альбедо.)*
7.  **Orbital Dynamics:** Verifying orbital stability and calculating Hill Sphere radius to assess moon retention potential.
    *(Орбитальная динамика: Проверка стабильности орбиты и расчет сферы Хилла.)*

### Phase 3: Physics-Based Modeling (Этапы 8-11)
8.  **Internal Structure Modeling:** Using equations of state (EOS) for silicates and iron to determine Core Mass Fraction (CMF).
    *(Моделирование внутреннего строения: Использование уравнений состояния для определения доли ядра.)*
9.  **Phase Transition Analysis:** Checking if ocean depth pressure exceeds the Ice VII threshold ($P > 2.2 \text{ GPa}$), which blocks geochemical cycles.
    *(Анализ фазовых переходов: Проверка порога образования льда VII на дне океана.)*
10. **Magnetic Dynamo Simulation:** Estimating the likelihood of a magnetic field based on core convection models and rotation periods.
    *(Симуляция магнитного динамо: Оценка вероятности наличия магнитного поля.)*
11. **Atmospheric Escape:** Calculating Jeans escape parameter $\lambda$ to determine atmospheric retention against stellar wind.
    *(Уход атмосферы: Расчет параметра Джинса для оценки удержания атмосферы.)*

### Phase 4: AI Synthesis & Scoring (Этапы 12-14)
12. **Feature Engineering:** Creating composite features like "Geochemical Potential" and "Tectonic Activity Score".
    *(Инжиниринг признаков: Создание составных признаков для ML.)*
13. **ML Classification (XGBoost):** A trained Gradient Boosting model classifies planets into types: *Habitable Earth, Ocean World, Iron Planet, Gas Giant*.
    *(Классификация ML: Модель XGBoost классифицирует планеты по типам.)*
14. **PRI Calculation:** The final **Planetary Retainability Index** is computed as a weighted product of geochemical and geodynamic probabilities, bounded by the Critical Density Law.
    *(Расчет PRI: Финальный индекс удерживаемости, ограниченный Законом Критической Плотности.)*

---

## 3. Key Algorithms & Formulas / Ключевые Алгоритмы и Формулы

### A. Mass-Radius Relation (Bayesian)
We use a broken power-law model to infer mass ($M$) from radius ($R$):
$$ M = C \cdot R^\alpha $$
Where coefficients $C$ and $\alpha$ vary depending on the planetary regime (Terran, Neptune-like, etc.), derived from posterior distributions of known exoplanets.

### B. The PRI Index Formula
The core metric of our system is defined as:
$$ PRI(\rho) = P_{geo}(\rho) \times P_{dyn}(\rho) \times f(T_{eq}) $$
Where:
*   $P_{geo}$: Probability of open geochemical cycle (Logistic function, threshold $\rho > 4.8$).
*   $P_{dyn}$: Probability of active magnetic dynamo (Reverse Logistic function, threshold $\rho < 7.8$).
*   $f(T_{eq})$: Temperature habitability factor (Gaussian centered on liquid water zone).

### C. Gaussian Habitability Fit
The empirical validation of the law uses non-linear least squares optimization (`scipy.optimize.curve_fit`) to fit the data to:
$$ P_{hab}(\rho) = A \cdot e^{-\frac{(\rho - \mu)^2}{2\sigma^2}} $$
Resulting in parameters: $\mu \approx 6.26$, $\sigma \approx 2.11$.

---

## 4. Software Modules Description / Описание Программных Модулей

The repository includes three main executable modules:

1.  **`exologica_analyzer.py`**:
    *   **Function:** Global statistical analysis.
    *   **Features:** Loads full dataset, fits Gaussian curve, visualizes density distribution, outputs Top-10 candidates.
    *   **Use Case:** Quick verification of the Critical Density Law.

2.  **`exologica_spectra.py`**:
    *   **Function:** Synthetic spectroscopy simulator.
    *   **Features:** Generates mock JWST spectra based on planet type (Ocean/Iron/Habitable), adding noise and specific absorption lines (H₂O, CO₂, CH₄, O).
    *   **Use Case:** Visualizing what biosignatures might look like for specific candidates.

3.  **Data Export Pipeline (Internal)**:
    *   Generates `ExoLogica_Export.csv` (Prime candidates) and `ExoLogica_Export-s.csv` (Full database).

---

## 5. Reproducibility & Validation / Воспроизводимость и Валидация

All results presented in this project are fully reproducible using the provided Python scripts and CSV datasets.
*   **Dataset Version:** v2.0 (March 2026)
*   **Model Accuracy:** $R^2 = 0.923$ on test set for PRI prediction.
*   **Validation Method:** Cross-validation with hold-out sets and comparison against known Solar System bodies (Earth, Mars, Venus).

*(Все результаты полностью воспроизводимы с помощью предоставленных скриптов. Точность модели $R^2 = 0.923$.)*

---

## 6. Future Development Roadmap / Дорожная Карта Развития

*   **v2.1:** Integration of real JWST transmission spectra data for validation.
*   **v2.2:** Adding tidal heating models for planets around M-dwarfs.
*   **v3.0:** Web-based interactive dashboard (Streamlit/React) for public access.

---

*Author: Lomakn-droid (ExoLogica Project)*
*License: MIT License*
*Contact: Lomakn@gmail.com*
