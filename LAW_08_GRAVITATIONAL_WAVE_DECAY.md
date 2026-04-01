# LAW №8: GRAVITATIONAL-WAVE ORBITAL DECAY
# ЗАКОН №8: ГРАВИТАЦИОННО-ВОЛНОВОЙ РАСПАД ОРБИТ

## 1. Fundamental Postulate / Фундаментальный постулат
According to Einstein's General Theory of Relativity, any massive bodies orbiting each other emit energy in the form of **gravitational waves**. This emission causes a gradual loss of orbital energy, leading to an inevitable decrease in the orbital separation ($a$) and, eventually, the collision of the bodies.

For exoplanets, this law establishes an absolute **"Orbital Deadline"**: even if a planet possesses ideal conditions for life (perfect UMSI, temperature, density), it is **doomed** if its orbital decay time ($t_{decay}$) is shorter than the time required for biological evolution (estimated at $\approx 2$ billion years). Such worlds are termed **"Doomed Worlds"**.

**(Согласно Общей теории относительности Эйнштейна, любые массивные тела, вращающиеся друг вокруг друга, излучают энергию в виде гравитационных волн. Это излучение вызывает постепенную потерю орбитальной энергии, что приводит к неизбежному уменьшению орбитального расстояния ($a$) и, в конечном итоге, к столкновению тел. Для экзопланет этот закон устанавливает абсолютный «Орбитальный Дедлайн»: даже если планета обладает идеальными условиями для жизни (идеальный UMSI, температура, плотность), она обречена, если время её орбитального распада ($t_{decay}$) меньше времени, необходимого для биологической эволюции (оценочно $\approx 2$ млрд лет). Такие миры называются «Обреченными Мирами». )**

## 2. Mathematical Justification / Математическое обоснование
The time remaining until the complete decay of the orbit ($t_{decay}$) for a planet of mass $m$ orbiting a star of mass $M$ at a semi-major axis $a$ is given by the Peters-Mathews formula derived from General Relativity:

$$ t_{decay} = \frac{5}{256} \frac{c^5}{G^3} \frac{a^4}{(M \cdot m)(M + m)} $$

Where:
*   $c$ — Speed of light ($299,792,458$ m/s).
*   $G$ — Gravitational constant ($6.67430 \times 10^{-11}$ m³/kg·s²).
*   $a$ — Semi-major axis of the orbit (meters).
*   $M$ — Mass of the host star (kg).
*   $m$ — Mass of the planet (kg).

**Key Dependence:** The decay time is proportional to the fourth power of the distance ($t \propto a^4$). This means that a small decrease in orbital distance leads to a dramatic reduction in the planet's lifespan.

**(Время до полного распада орбиты ($t_{decay}$) для планеты массой $m$, вращающейся вокруг звезды массой $M$ на большой полуоси $a$, задается формулой Петерса-Мэттьюса, выведенной из ОТО: ... Где $c$ — скорость света... $G$ — гравитационная постоянная... $a$ — большая полуось орбиты... $M$ — масса звезды-хозяина... $m$ — масса планеты... Ключевая зависимость: Время распада пропорционально четвертой степени расстояния ($t \propto a^4$). Это означает, что малейшее уменьшение орбитального расстояния приводит к драматическому сокращению срока жизни планеты.)**

## 3. Empirical Evidence from ExoLogica / Эмпирические доказательства от ExoLogica
Analysis of the **ExoLogica_Export-s.csv** database (~9,838 objects) using the above formula revealed two distinct populations:

1.  **The Doomed Worlds (110 Objects):**
    *   These are primarily massive gas giants or brown dwarfs on ultra-short orbits ($a < 0.05$ AU).
    *   Their calculated $t_{decay}$ is **less than 2 billion years**.
    *   *Example:* **CR Boo b** has only ~4.7 million years left before colliding with its star. Despite potentially stable conditions now, they are transient phenomena destined for destruction.

2.  **Relativistic Immunity of Habitable Planets:**
    *   Crucially, **ZERO** planets identified as "True Earths" (high PRI, optimal UMSI, rocky composition) fall into the Doomed category.
    *   Rocky planets in the habitable zone have $t_{decay}$ values exceeding **30,000 billion years**, far longer than the current age of the Universe (13.8 Gyr).
    *   **Conclusion:** Nature protects potential life. The same gravitational laws that destroy close-in giants ensure the long-term stability of rocky worlds in the habitable zone.

**(Анализ базы данных ExoLogica с использованием вышеуказанной формулы выявил две различные популяции:
1. Обреченные Миры (110 объектов): Это преимущественно массивные газовые гиганты или коричневые карлики на ультракоротких орбитах. Их рассчитанное $t_{decay}$ составляет менее 2 млрд лет. Пример: CR Boo b осталось всего ~4.7 млн лет до столкновения со звездой. Несмотря на потенциально стабильные условия сейчас, они являются преходящими явлениями, обреченными на разрушение.
2. Релятивистский Иммунитет Обитаемых Планет: Что критически важно, НИ ОДНА планета, идентифицированная как «Истинная Земля» (высокий PRI, оптимальный UMSI, каменистый состав), не попадает в категорию Обреченных. Каменистые планеты в обитаемой зоне имеют значения $t_{decay}$, превышающие 30 000 млрд лет, что намного больше текущего возраста Вселенной (13.8 млрд лет). Вывод: Природа защищает потенциальную жизнь. Те же гравитационные законы, которые уничтожают близкие гиганты, обеспечивают долгосрочную стабильность каменистых миров в обитаемой зоне.)**

## 4. Physical Interpretation of Zones / Физическая интерпретация зон

### Zone I: The Graveyard of Orbits ($t_{decay} < 2$ Gyr)
*   **Characteristics:** Ultra-close massive bodies ($a < 0.05$ AU). High gravitational wave luminosity.
*   **Consequence:** Rapid inspiral. The planet will merge with the star within a timeframe too short for complex life to evolve or survive. These are "false positives" for long-term habitability.
*   **(Зона I: Кладбище Орбит. Характеристики: Ультра-близкие массивные тела. Высокая светимость гравитационных волн. Следствие: Быстрая спираль. Планета сольется со звездой за время, слишком короткое для эволюции или выживания сложной жизни. Это «ложные цели» для долгосрочной обитаемости.)**

### Zone II: The Stable Corridor ($t_{decay} > 13.8$ Gyr)
*   **Characteristics:** Planets at safe distances ($a > 0.1$ AU) or with low masses. Negligible gravitational wave emission.
*   **Consequence:** Orbital stability over cosmological timescales. These worlds have sufficient time for abiogenesis and biological evolution. All known "True Earths" reside here.
*   **(Зона II: Стабильный Коридор. Характеристики: Планеты на безопасных расстояниях или с низкими массами. Пренебрежимо малое излучение гравитационных волн. Следствие: Орбитальная стабильность в космологических масштабах времени. Эти миры имеют достаточно времени для абиогенеза и биологической эволюции. Все известные «Истинные Земли» находятся здесь.)**

## 5. Predictive Power & Application / Предсказательная сила и применение
This law provides a critical filter for prioritizing targets for future telescopes (JWST, PLATO, ARIEL):
1.  **Exclude Transient Giants:** Any massive planet with $t_{decay} < 2$ Gyr should be excluded from lists of long-term habitable candidates, regardless of current temperature or composition.
2.  **Confirm Stability of Earth-Twins:** The absence of rocky planets in the "Doomed" zone confirms that our search for life can safely focus on systems where $t_{decay}$ exceeds the age of the Universe.
3.  **Future Observations:** Monitoring the orbital decay of ultra-short period planets (like CR Boo b) offers a unique opportunity to directly test General Relativity in extreme regimes.

**(Этот закон предоставляет критический фильтр для приоритизации целей для будущих телескопов: 1. Исключить Преходящие Гиганты: Любой массивный объект с $t_{decay} < 2$ млрд лет должен быть исключен из списков кандидатов на долгосрочную обитаемость. 2. Подтвердить Стабильность Земель-Близнецов: Отсутствие каменистых планет в «Обреченной» зоне подтверждает, что наш поиск жизни может безопасно фокусироваться на системах, где $t_{decay}$ превышает возраст Вселенной. 3. Будущие Наблюдения: Мониторинг орбитального распада планет с ультракоротким периодом предлагает уникальную возможность напрямую проверить Общую теорию относительности в экстремальных режимах.)**

---
*Author: Lahvinovich Victar (ExoLogica Project)*  
*Date: April 2026*  
*License: MIT*
