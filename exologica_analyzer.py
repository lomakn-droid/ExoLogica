import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import tkinter as tk
from tkinter import filedialog, messagebox
import warnings
import os

# Игнорируем предупреждения о делении на ноль или переполнении для чистоты вывода
warnings.filterwarnings('ignore')

# --- КОНСТАНТЫ И НАСТРОЙКИ ---
# Цветовая палитра для разных типов планет
COLORS_MAP = {
    'Газовый гигант': '#1f77b4',       # Синий
    'Ледяной гигант': '#aec7e8',       # Светло-синий
    'Обитаемая Земля': '#2ca02c',      # Зеленый (Жизнь!)
    'Каменистая планета': '#ff7f0e',   # Оранжевый
    'Массивная Суперземля': '#d62728', # Красный
    'Железная планета': '#7f7f7f',     # Серый
    'Мир-Океан': '#9467bd',            # Фиолетовый
    'Раскаленный каменистый мир': '#8c564b', # Коричневый
    'Мини-Нептун (Газ)': '#c49c94',    # Розовато-серый
    'nan': '#333333'                   # Черный для неизвестных
}

# --- МАТЕМАТИЧЕСКОЕ ЯДРО ---
def gaussian(x, a, mu, sigma):
    """
    Функция Гаусса для аппроксимации Закона Экзолоджики.
    P_hab(rho) = A * exp(-(rho - mu)^2 / (2 * sigma^2))
    """
    return a * np.exp(-((x - mu)**2) / (2 * sigma**2))

# --- ОСНОВНАЯ ЛОГИКА ---
def load_and_analyze():
    # 1. Открытие диалога выбора файла
    file_path = filedialog.askopenfilename(
        title="Select ExoLogica Dataset (CSV)",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if not file_path:
        return  # Пользователь отменил выбор

    print(f"\n🚀 Loading data from: {os.path.basename(file_path)}...")

    try:
        # 2. Чтение и очистка данных
        # Пробуем определить разделитель автоматически, но по умолчанию ставим ';'
        df = pd.read_csv(file_path, sep=';')
        
        # Принудительное преобразование числовых колонок
        df['Плотн(г/см3)'] = pd.to_numeric(df['Плотн(г/см3)'], errors='coerce')
        df['PRI'] = pd.to_numeric(df['PRI'], errors='coerce')
        
        # Удаляем строки, где нет плотности или PRI
        df_clean = df.dropna(subset=['Плотн(г/см3)', 'PRI'])
        
        if len(df_clean) == 0:
            messagebox.showerror("Error", "No valid numeric data found in the file!")
            return

        print(f"✅ Successfully loaded and cleaned {len(df_clean)} objects.")

        # 3. Подгонка кривой (Curve Fitting)
        p0 = [0.9, 6.2, 2.0]  # Начальные догадки: A=0.9, mu=6.2, sigma=2.0
        try:
            popt, pcov = curve_fit(gaussian, df_clean['Плотн(г/см3)'], df_clean['PRI'], p0=p0)
            a_opt, mu_opt, sigma_opt = popt
            print(f"📊 ExoLogica Law Parameters Fit:")
            print(f"   Optimum Density (μ): {mu_opt:.3f} g/cm³")
            print(f"   Window Width (σ):    {sigma_opt:.3f}")
            print(f"   Amplitude (A):       {a_opt:.3f}")
        except RuntimeError:
            print("⚠️ Could not fit curve perfectly. Using default parameters.")
            mu_opt, sigma_opt, a_opt = 6.26, 2.11, 0.90

        # 4. Построение графика
        plt.figure(figsize=(14, 9))
        
        # Отрисовка точек рассеяния по группам
        for planet_type, group in df_clean.groupby('Уточненная природа'):
            color = COLORS_MAP.get(planet_type, '#333333')
            label = planet_type if planet_type != 'nan' else 'Unknown Type'
            # Рисуем точки прозрачными, чтобы видеть плотность скопления
            plt.scatter(group['Плотн(г/см3)'], group['PRI'], 
                        c=color, label=label, s=40, alpha=0.6, edgecolors='none')

        # Отрисовка теоретической кривой Закона Экзолоджики
        x_line = np.linspace(0, 15, 500)
        y_line = gaussian(x_line, a_opt, mu_opt, sigma_opt)
        plt.plot(x_line, y_line, 'k-', linewidth=3, label=f'ExoLogica Law (Fit: μ={mu_opt:.2f})')

        # Выделение "Критического окна" (4.8 - 7.8)
        plt.axvspan(4.8, 7.8, color='#2ca02c', alpha=0.15, label='Critical Life Window (4.8–7.8)')
        plt.axvline(mu_opt, color='red', linestyle='--', linewidth=2, label=f'Optimum ({mu_opt:.2f})')

        # Настройки оформления
        title_text = 'Global Habitability Map: ExoLogica Law Validation\n(Глобальная карта обитаемости: Проверка Закона Экзолоджики)'
        plt.title(title_text, fontsize=16, fontweight='bold')
        plt.xlabel('Planet Density (g/cm³) / Плотность планеты (г/см³)', fontsize=12)
        plt.ylabel('PRI Index (Planetary Retainability) / Индекс PRI', fontsize=12)
        plt.xlim(0, 15) 
        plt.ylim(-0.1, 1.1)
        plt.legend(loc='upper right', fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.4)
        plt.tight_layout()

        print("\n📈 Plotting Global Map... (Close the plot window to see Top Candidates)")
        plt.show()

        # 5. Поиск и вывод ТОП-10 кандидатов
        print("\n" + "="*80)
        print(" TOP-10 POTENTIALLY HABITABLE WORLDS (ExoLogica Filter)")
        print(" ТОП-10 ПОТЕНЦИАЛЬНО ОБИТАЕМЫХ МИРОВ (Фильтр Закона Экзолоджики)")
        print("="*80)
        
        # Фильтр: Плотность в окне 4.8-7.8, PRI > 0.7, исключаем газовые/ледяные гиганты
        candidates = df_clean[
            (df_clean['Плотн(г/см3)'] >= 4.8) & 
            (df_clean['Плотн(г/см3)'] <= 7.8) & 
            (df_clean['PRI'] > 0.7) &
            (~df_clean['Уточненная природа'].isin(['Газовый гигант', 'Ледяной гигант', 'Мини-Нептун (Газ)']))
        ].copy()
        
        # Сортировка по PRI (убывание)
        candidates = candidates.sort_values(by='PRI', ascending=False)
        
        if not candidates.empty:
            # Выбираем колонки для вывода
            display_cols = ['Планета', 'Звезда', 'Уточненная природа', 'Плотн(г/см3)', 'PRI', 'ESI', 'Статус ИИ']
            
            # Вывод первых 10 строк
            top_10 = candidates.head(10)[display_cols]
            
            # Красивый вывод таблицы в консоль
            print(top_10.to_string(index=False))
            
            print("\n" + "-"*80)
            print(f"💡 Total candidates found in 'Golden Zone': {len(candidates)} out of {len(df_clean)}")
            print("-"*80)
        else:
            print("⚠️ No candidates found matching strict criteria in this dataset.")

    except Exception as e:
        messagebox.showerror("System Error", f"An error occurred during processing:\n{e}")
        print(f" Error: {e}")

# --- ЗАПУСК GUI ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("ExoLogica AI: Density Law Analyzer")
    root.geometry("550x280")
    
    # Центрирование окна
    root.eval('tk::PlaceWindow . center')

    # Заголовок
    lbl_title = tk.Label(root, text="ExoLogica AI Analyzer", font=("Arial", 14, "bold"))
    lbl_title.pack(pady=10)

    # Описание
    lbl_desc = tk.Label(root, 
        text="Load ExoLogica_Export-s.csv to visualize the\nGlobal Habitability Map and find Top Candidates.\n"
             "(Загрузите файл ExoLogica_Export-s.csv для построения\nглобальной карты и поиска лучших кандидатов)", 
        font=("Arial", 10), justify=tk.CENTER)
    lbl_desc.pack(pady=10)

    # Кнопка запуска
    btn_run = tk.Button(root, text="🚀 Select CSV & Run Analysis", 
                    font=("Arial", 11, "bold"), bg="#2ecc71", fg="white", 
                    cursor="hand2", command=load_and_analyze)
    btn_run.pack(expand=True, fill=tk.BOTH, padx=40, pady=10)

    # Футер
    lbl_footer = tk.Label(root, text="Based on ExoLogica Law (ρ ≈ 6.26 g/cm³)", font=("Arial", 8), fg="gray")
    lbl_footer.pack(pady=5)

    root.mainloop()
