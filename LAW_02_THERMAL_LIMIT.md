# LAW №2: THE ATMOSPHERIC THERMAL LIMIT LAW
# ЗАКОН №2: ТЕРМИЧЕСКИЙ ПРЕДЕЛ АТМОСФЕРЫ

## 1. Fundamental Postulate / Фундаментальный постулат
The existence of a stable atmosphere on an exoplanet is not guaranteed even with suitable surface temperature. There is a critical dependence between the planet's orbital period ($P$) and its maximum possible surface temperature ($T_{max}$), above which the planet physically cannot retain an atmosphere due to the dominance of thermal energy over gravitational potential.

This boundary defines the **"Zone of Thermal Survival"**. Planets located above this boundary on the "Temperature-Period" diagram inevitably lose volatiles and transform into airless rocky bodies (Chthonian planets).

**(Существование стабильной атмосферы у экзопланеты не гарантировано даже при подходящей температуре поверхности. Существует критическая зависимость между орбитальным периодом планеты ($P$) и максимально возможной температурой её поверхности ($T_{max}$), выше которой планета физически не способна удерживать атмосферу из-за доминирования тепловой энергии над гравитационным потенциалом. Эта граница определяет «Зону Термического Выживания». Планеты, находящиеся выше этой границы на диаграмме «Температура-Период», неизбежно теряют летучие вещества и превращаются в безвоздушные скалистые тела.)**

## 2. Mathematical Justification / Математическое обоснование
The evaporation boundary is described by a power function reflecting the balance between the kinetic energy of gas molecules and the work required to escape the planet's gravitational well. Empirical analysis of the ExoLogica database (~9,800 objects) shows that this dependence is approximated by the formula:

$$T_{max}(P) \approx C \cdot P^{-k}$$

Where:
*   $T_{max}$ — Limiting surface temperature (K), above which the atmosphere is unstable.
*   $P$ — Orbital period (days).
*   $C \approx 2500$ — Empirical coefficient depending on the average mass and radius of rocky planets in the sample.
*   $k \approx 0.6$ — Power index reflecting the physics of thermal equilibrium and tidal influence.

For our sample, the specific boundary passes along the line:
$$T_{limit} = 2500 \cdot P^{-0.6}$$

**(Граница испарения описывается степенной функцией, отражающей баланс между кинетической энергией молекул газа и работой выхода из гравитационной ямы планеты. Эмпирический анализ базы данных ExoLogica (~9800 объектов) показал, что эта зависимость аппроксимируется формулой... Где $T_{max}$ — предельная температура..., $P$ — орбитальный период..., $C \approx 2500$ — эмпирический коэффициент..., $k \approx 0.6$ — показатель степени... Для нашей выборки конкретная граница проходит по линии $T_{limit} = 2500 \cdot P^{-0.6}$.)**

## 3. Physical Interpretation of Zones / Физическая интерпретация зон

### Zone I: Thermal Dissipation ($T > T_{limit}$)
*   **Characteristic:** Thermal energy dominates over gravity.
*   **Consequence:** Catastrophic loss of atmosphere and volatiles. The planet boils away, becoming a bare rock. Life is impossible due to lack of pressure and water.
*   **(Характеристика: Тепловая энергия доминирует над гравитацией. Следствие: Катастрофическая потеря атмосферы и летучих веществ. Планета выкипает, превращаясь в голую скалу. Жизнь невозможна из-за отсутствия давления и воды.)**

### Zone II: Thermal Survival ($T \leq T_{limit}$)
*   **Characteristic:** Planetary gravity is sufficient to retain gases against thermal expansion.
*   **Consequence:** Long-term atmospheric evolution, greenhouse effect formation, and presence of liquid water are possible. This is the only zone where a stable biosphere can exist (subject to the Critical Density Law).
*   **(Характеристика: Гравитация планеты достаточна для удержания газов против теплового расширения. Следствие: Возможна долгосрочная эволюция атмосферы, формирование парникового эффекта и наличие жидкой воды. Это единственная зона, где возможно существование стабильной биосферы.)**

## 4. Integration with Other Laws / Интеграция с другими законами
The Atmospheric Thermal Limit Law is a necessary but not sufficient condition for habitability. It works in tandem with **Law №1 (Critical Density)**:
1.  First, the planet must pass the density filter ($4.8 < \rho < 7.8$ g/cm³).
2.  Then, it must be within the Zone of Thermal Survival ($T \leq 2500 \cdot P^{-0.6}$).

Only the intersection of these two conditions guarantees the physical possibility of an Earth-like world.

**(Закон Термического Предела является необходимым, но не достаточным условием обитаемости. Он работает в тандеме с Законом №1 (Критическая Плотность): 1. Сначала планета должна пройти фильтр по плотности. 2. Затем она должна находиться в Зоне Термического Выживания. Только пересечение этих двух условий гарантирует физическую возможность существования земноподобного мира.)**

## 5. Predictive Power / Предсказательная сила
This law allows for the instant filtering of thousands of candidates from Kepler, TESS, and K2 catalogs that have suitable temperatures but are too close to their stars (short period), rendering them airless. This saves telescope time (JWST, PLATO) by preventing observations of knowingly dead worlds.

**(Данный закон позволяет мгновенно отсеивать тысячи кандидатов из каталогов Kepler, TESS и K2, которые имеют подходящую температуру, но находятся слишком близко к звезде, что делает их безвоздушными. Это экономит время телескопов, предотвращая наблюдения заведомо мертвых миров.)**

---
*Author: Lahvinovich Victar (ExoLogica Project)*  
*Date: April 2026*  
*License: MIT*
