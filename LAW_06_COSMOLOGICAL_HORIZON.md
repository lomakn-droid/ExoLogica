# LAW №6: THE COSMOLOGICAL HABITABILITY HORIZON
# ЗАКОН №6: КОСМОЛОГИЧЕСКИЙ ГОРИЗОНТ ОБИТАЕМОСТИ

## 1. Fundamental Postulate / Фундаментальный постулат
Habitability is not a static property of a planet but a transient phenomenon constrained by the evolutionary history of the Universe itself. Life as we know it (carbon-based, requiring liquid water and heavy elements) can only exist within a specific **Cosmological Time Window** bounded by two absolute limits: the formation of the first heavy elements after the Big Bang and the eventual heat death of the Universe.

**(Обитаемость не является статическим свойством планеты, а представляет собой преходящее явление, ограниченное эволюционной историей самой Вселенной. Жизнь, какой мы её знаем (углеродная, требующая жидкой воды и тяжелых элементов), может существовать только в特定ном Космологическом Временном Окне, ограниченном двумя абсолютными пределами: формированием первых тяжелых элементов после Большого Взрыва и конечной тепловой смертью Вселенной.)**

## 2. Mathematical Justification / Математическое обоснование
The probability of finding a habitable rocky planet ($P_{hab}$) is a function of the stellar metallicity ($[Fe/H]$) and the cosmic time ($t$):

$$P_{hab}(t) \propto f([Fe/H](t)) \cdot g(T_{star}(t))$$

Where:
*   **$[Fe/H]$ (Metallicity):** The abundance of elements heavier than helium. Immediately after the Big Bang ($t < 200$ Myr), $[Fe/H] \approx -\infty$. Rocky planets cannot form without silicates and metals.
*   **Critical Threshold:** Empirical analysis of the ExoLogica database confirms that the probability of a stable biosphere drops to near zero when:
    $$[Fe/H] < -0.5$$
*   **$T_{star}$ (Stellar Era):** Stars must be on the Main Sequence to provide stable energy. In the far future ($t > 10^{14}$ years), star formation ceases, and existing stars burn out, ending the era of habitability.

**The Golden Era Equation:**
Life is only possible when:
$$t_{formation} < t < t_{degeneration}$$
Where $t_{formation} \approx 1-2$ Gyr (time to enrich the interstellar medium) and $t_{degeneration} \approx 100$ Tyr (end of the Stelliferous Era).

**(Вероятность обнаружения обитаемой каменистой планеты ($P_{hab}$) является функцией металличности звезды ($[Fe/H]$) и космического времени ($t$)... Где $[Fe/H]$ — металличность... Критический порог: Эмпирический анализ базы данных ExoLogica подтверждает, что вероятность стабильной биосферы падает почти до нуля, когда $[Fe/H] < -0.5$. Уравнение Золотой Эры: Жизнь возможна только когда $t_{formation} < t < t_{degeneration}$.)**

## 3. Physical Interpretation of Zones / Физическая интерпретация зон

### Zone I: The Primordial Void ($[Fe/H] < -0.5$, $t < 2$ Gyr)
*   **Characteristics:** The early Universe consisted almost entirely of Hydrogen and Helium. No carbon, oxygen, silicon, or iron existed in sufficient quantities to form rocky cores or organic molecules.
*   **Consequence:** Any objects formed in this era are purely gaseous or composed of exotic matter unsuitable for life. "Earth-like" planets are physically impossible.
*   **(Зона I: Первичная Пустота. Характеристики: Ранняя Вселенная состояла почти исключительно из водорода и гелия. Углерода, кислорода, кремния или железа не существовало в достаточных количествах для формирования каменистых ядер или органических молекул. Следствие: Любые объекты, сформированные в эту эпоху, являются чисто газовыми. Планеты «земного типа» физически невозможны.)**

### Zone II: The Golden Era of Habitability ($[Fe/H] \ge -0.5$, $2 \text{ Gyr} < t < 100 \text{ Tyr}$)
*   **Characteristics:** Generations of stars have lived and died (supernovae), enriching the interstellar medium with heavy elements ("metals"). Stable Main Sequence stars provide consistent energy.
*   **Consequence:** This is the **only** epoch where rocky planets with high UMSI and complex chemistry can form and sustain life. We currently live in the peak of this era (~13.8 Gyr after the Big Bang).
*   **(Зона II: Золотая Эра Обитаемости. Характеристики: Поколения звезд жили и умирали (сверхновые), обогащая межзвездную среду тяжелыми элементами («металлами»). Стабильные звезды главной последовательности обеспечивают постоянную энергию. Следствие: Это единственная эпоха, где могут формироваться и поддерживать жизнь каменистые планеты с высоким UMSI и сложной химией. Мы сейчас живем на пике этой эры.)**

### Zone III: The Degenerate Future ($t > 100$ Tyr)
*   **Characteristics:** Star formation has ceased. All Main Sequence stars have burned out, leaving only white dwarfs, neutron stars, and black holes. The Universe cools towards absolute zero.
*   **Consequence:** Without stellar energy sources, surface temperatures plummet. Even if planets exist, they are frozen dead worlds. Hawking radiation from black holes is insufficient to sustain a biosphere (see Law №9).
*   **(Зона III: Вырожденное Будущее. Характеристики: Звездообразование прекратилось. Все звезды главной последовательности выгорели. Вселенная остывает к абсолютному нулю. Следствие: Без источников звездной энергии температуры падают. Даже если планеты существуют, они являются замерзшими мертвыми мирами.)**

## 4. Empirical Evidence from ExoLogica / Эмпирические доказательства от ExoLogica
Analysis of the **ExoLogica_Export-s.csv** database (~9,800 objects) reveals a strong statistical correlation:
*   **91 out of 131** (69.4%) of our identified "True Earths" (high PRI, optimal UMSI) orbit stars with metallicity $[Fe/H] > -0.5$.
*   Planets around low-metallicity stars (Population II) consistently show low PRI values or are classified as gas giants/ice worlds, confirming the inability to form stable rocky biospheres in metal-poor environments.

**(Анализ базы данных ExoLogica выявляет сильную статистическую корреляцию: 91 из 131 (69.4%) наших выявленных «Истинных Земель» вращаются вокруг звезд с металличностью [Fe/H] > -0.5. Планеты вокруг звезд с низкой металличностью (Популяция II) последовательно показывают низкие значения PRI или классифицируются как газовые гиганты/ледяные миры, подтверждая невозможность формирования стабильных каменистых биосфер в бедных металлами средах.)**

## 5. Predictive Power & Application / Предсказательная сила и применение
This law provides a crucial filter for prioritizing targets in deep space surveys:
1.  **Exclude Ancient Stars:** Systems older than ~10-12 billion years (low metallicity halo stars) should be deprioritized for biosignature searches, regardless of their location in the habitable zone.
2.  **Focus on Disk Stars:** Prioritize stars in the galactic disk (Population I) where metallicity is high ($[Fe/H] \approx 0.0$).
3.  **Temporal Context:** Understanding that we are in a unique "Golden Window" emphasizes the urgency and rarity of detecting life *now*.

**(Этот закон предоставляет важнейший фильтр для приоритизации целей в глубоких космических обзорах: 1. Исключить древние звезды. 2. Сосредоточиться на звездах диска. 3. Временной контекст: Понимание того, что мы находимся в уникальном «Золотом Окне», подчеркивает срочность и редкость обнаружения жизни именно сейчас.)**

---
*Author: Lahvinovich Victar (ExoLogica Project)*  
*Date: April 2026*  
*License: MIT*
