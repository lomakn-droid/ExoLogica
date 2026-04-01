import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Circle, Wedge
import math

# --- ДАННЫЕ ПЛАНЕТЫ ---
PLANET_DATA = {
    "name": "KOI-4878 b",
    "star": "KOI-4878",
    "mass_me": 1.81,
    "radius_re": 1.04,
    "density": 8.85,
    "temp_k": 250,
    "period_days": 449.01,
    "esi": 0.978,
    "pri": 0.344,
    "type_ai": "Железная планета",
    "status": "НЕОБИТАЕМА"
}

class ModernPlanetPassport:
    def __init__(self, root):
        self.root = root
        self.root.title(f"ExoLogica AI: Passport of {PLANET_DATA['name']}")
        self.root.geometry("1200x800")
        self.root.configure(bg="#0f0f0f")
        
        # Настройка стилей
        self.setup_styles()
        self.setup_ui()

    def setup_styles(self):
        """Настройка современных стилей интерфейса"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Цветовая палитра
        self.colors = {
            'bg_primary': '#0f0f0f',
            'bg_secondary': '#1a1a1a',
            'bg_card': '#252525',
            'text_primary': '#ffffff',
            'text_secondary': '#b0b0b0',
            'accent_green': '#00ff88',
            'accent_red': '#ff4466',
            'accent_blue': '#00ccff',
            'accent_orange': '#ffaa00'
        }

    def setup_ui(self):
        """Создание современного интерфейса с вкладками"""
        # Заголовок
        self.create_header()
        
        # Основной контейнер
        main_container = tk.Frame(self.root, bg=self.colors['bg_primary'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Создаем Notebook (вкладки)
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Вкладка 1: Общая информация
        self.tab_info = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(self.tab_info, text=" Общая информация")
        self.create_info_tab()
        
        # Вкладка 2: Внутреннее строение
        self.tab_structure = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(self.tab_structure, text="🔬 Внутреннее строение")
        self.create_structure_tab()
        
        # Вкладка 3: Спектральный анализ
        self.tab_spectrum = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(self.tab_spectrum, text=" Спектральный анализ")
        self.create_spectrum_tab()
        
        # Вкладка 4: Вердикт ИИ
        self.tab_verdict = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(self.tab_verdict, text="⚖️ Вердикт ИИ")
        self.create_verdict_tab()

    def create_header(self):
        """Создание стильного заголовка"""
        header_frame = tk.Frame(self.root, bg=self.colors['bg_secondary'], height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_text = f" ПАСПОРТ ПЛАНЕТЫ: {PLANET_DATA['name']}"
        subtitle_text = "Анализ по Закону Экзолоджики v2.0"
        
        title_lbl = tk.Label(header_frame, text=title_text, 
                            font=("Arial", 20, "bold"), 
                            fg=self.colors['accent_green'],
                            bg=self.colors['bg_secondary'])
        title_lbl.pack(pady=(15, 5))
        
        subtitle_lbl = tk.Label(header_frame, text=subtitle_text,
                               font=("Arial", 10),
                               fg=self.colors['text_secondary'],
                               bg=self.colors['bg_secondary'])
        subtitle_lbl.pack()

    def create_info_tab(self):
        """Вкладка с общей информацией"""
        # Левая панель с параметрами
        left_panel = tk.Frame(self.tab_info, bg=self.colors['bg_secondary'], width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20), pady=20)
        left_panel.pack_propagate(False)
        
        self.create_params_card(left_panel)
        
        # Правая панель с кратким описанием
        right_panel = tk.Frame(self.tab_info, bg=self.colors['bg_primary'])
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, pady=20)
        
        self.create_description_panel(right_panel)

    def create_params_card(self, parent):
        """Карточка с физическими параметрами"""
        card_frame = tk.Frame(parent, bg=self.colors['bg_card'], relief=tk.RAISED, bd=2)
        card_frame.pack(fill=tk.X, padx=15, pady=15)
        
        title_lbl = tk.Label(card_frame, text=" ФИЗИЧЕСКИЕ ПАРАМЕТРЫ",
                            font=("Arial", 14, "bold"), fg=self.colors['accent_green'],
                            bg=self.colors['bg_card'], anchor=tk.W)
        title_lbl.pack(fill=tk.X, pady=(10, 15), padx=15)
        
        params = [
            ("Масса", f"{PLANET_DATA['mass_me']} M⊕", self.colors['accent_blue']),
            ("Радиус", f"{PLANET_DATA['radius_re']} R⊕", self.colors['accent_blue']),
            ("Плотность", f"{PLANET_DATA['density']} г/см³", self.colors['accent_red']),
            ("Температура", f"{PLANET_DATA['temp_k']} K", self.colors['accent_orange']),
            ("Период", f"{PLANET_DATA['period_days']} дней", self.colors['accent_orange']),
            ("ESI", f"{PLANET_DATA['esi']} ⚠️ Обманчиво высок", self.colors['accent_orange']),
            ("PRI", f"{PLANET_DATA['pri']} 🔴 Критически низок", self.colors['accent_red']),
            ("Тип по ИИ", PLANET_DATA['type_ai'], self.colors['accent_green']),
        ]
        
        for label, value, color in params:
            param_frame = tk.Frame(card_frame, bg=self.colors['bg_card'])
            param_frame.pack(fill=tk.X, pady=3, padx=15)
            
            lbl_name = tk.Label(param_frame, text=label, 
                               font=("Consolas", 10), 
                               fg=self.colors['text_secondary'], 
                               bg=self.colors['bg_card'], 
                               width=12, anchor=tk.W)
            lbl_name.pack(side=tk.LEFT)
            
            lbl_val = tk.Label(param_frame, text=value, 
                              font=("Consolas", 10, "bold"), 
                              fg=color, 
                              bg=self.colors['bg_card'], 
                              anchor=tk.W)
            lbl_val.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def create_description_panel(self, parent):
        """Панель с описанием планеты"""
        desc_frame = tk.Frame(parent, bg=self.colors['bg_card'], relief=tk.RAISED, bd=2)
        desc_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        title_lbl = tk.Label(desc_frame, text=" ОПИСАНИЕ ПЛАНЕТЫ",
                            font=("Arial", 14, "bold"), fg=self.colors['accent_green'],
                            bg=self.colors['bg_card'], anchor=tk.W)
        title_lbl.pack(fill=tk.X, pady=(10, 15), padx=15)
        
        desc_text = (
            f"**{PLANET_DATA['name']}** — экзопланета, обращающаяся вокруг звезды {PLANET_DATA['star']}.\n\n"
            "Эта планета представляет особый интерес для нашего исследования, так как демонстрирует "
            "классический пример того, почему традиционный индекс ESI может вводить в заблуждение.\n\n"
            "Несмотря на высокий ESI (0.978), наша система ExoLogica AI классифицирует её как "
            "\"Железную планету\" из-за аномально высокой плотности.\n\n"
            "**Ключевые особенности:**\n"
            "• Аномально высокая плотность указывает на гипертрофированное железное ядро\n"
            "• Тонкая силикатная мантия не поддерживает активную тектонику\n"
            "• Отсутствие магнитного динамо делает планету уязвимой для звездного ветра\n"
            "• Атмосфера практически отсутствует или сильно разрежена"
        )
        
        desc_lbl = tk.Label(desc_frame, text=desc_text,
                           font=("Arial", 11), fg=self.colors['text_primary'],
                           bg=self.colors['bg_card'], justify=tk.LEFT,
                           wraplength=600)
        desc_lbl.pack(padx=15, pady=15)

    def create_structure_tab(self):
        """Вкладка с внутренним строением"""
        # Создаем фигуру для графика
        fig, ax = plt.subplots(figsize=(10, 8), facecolor=self.colors['bg_primary'])
        fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
        
        ax.set_facecolor(self.colors['bg_primary'])
        ax.set_title("ВНУТРЕННЕЕ СТРОЕНИЕ ПЛАНЕТЫ\n(Модель ExoLogica)", 
                    color=self.colors['accent_green'], fontsize=16, pad=20, fontweight='bold')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off')
        
        # Расчет доли ядра
        core_fraction = 0.75
        mantle_fraction = 0.25
        
        # Ядро
        core_circle = Circle((0, 0), core_fraction, 
                            color='#8B4513', alpha=0.9,
                            edgecolor=self.colors['accent_orange'], linewidth=4)
        ax.add_patch(core_circle)
        
        # Мантия
        mantle_wedge = Wedge((0, 0), 1.0, 0, 360, 
                            width=mantle_fraction, 
                            color='#CD853F', alpha=0.7,
                            edgecolor=self.colors['accent_orange'], linewidth=3)
        ax.add_patch(mantle_wedge)
        
        # Текст
        ax.text(0, 0, f"ЯДРО\n{core_fraction*100:.0f}%", 
               ha='center', va='center', 
               color='white', fontsize=20, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.5", facecolor='#8B4513', 
                        alpha=0.8, edgecolor=self.colors['accent_orange']))
        
        ax.text(0, 0.85, "МАНТИЯ\n(Сжата)", 
               ha='center', va='center', 
               color='#FFD700', fontsize=14, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='#CD853F', 
                        alpha=0.7, edgecolor=self.colors['accent_orange']))
        
        # Легенда
        legend_data = [
            ('🟤 Железное ядро (75%)', '#8B4513'),
            ('🟡 Тонкая мантия (25%)', '#CD853F')
        ]
        
        for i, (label, color) in enumerate(legend_data):
            ax.text(-1.4, 1.2 - i*0.15, label, color=color, fontsize=12, 
                   fontweight='bold', ha='left')
        
        # Встраиваем график
        canvas = FigureCanvasTkAgg(fig, master=self.tab_structure)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def create_spectrum_tab(self):
        """Вкладка со спектральным анализом"""
        # Создаем фигуру для спектра
        fig, ax = plt.subplots(figsize=(12, 8), facecolor=self.colors['bg_primary'])
        fig.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
        
        ax.set_facecolor(self.colors['bg_primary'])
        ax.set_title("СИНТЕТИЧЕСКИЙ СПЕКТР (JWST Simulation)", 
                    color=self.colors['accent_green'], fontsize=16, pad=20, fontweight='bold')
        ax.set_xlabel("Длина волны (мкм)", color=self.colors['text_secondary'], fontsize=12)
        ax.set_ylabel("Глубина транзита (ppm)", color=self.colors['text_secondary'], fontsize=12)
        ax.grid(True, color='#333333', linestyle='--', alpha=0.6)
        
        # Генерация данных спектра
        wavelengths = np.linspace(0.6, 5.0, 500)
        base_depth = 200
        
        noise = np.random.normal(0, 8, size=len(wavelengths))
        spectrum = np.ones_like(wavelengths) * base_depth + noise
        
        # Слабый CO2 для железной планеты
        co2_line = 20 * np.exp(-0.5 * ((wavelengths - 4.3) / 0.1)**2)
        spectrum += co2_line
        
        from scipy.ndimage import gaussian_filter1d
        smooth_spectrum = gaussian_filter1d(spectrum, sigma=2)
        
        ax.plot(wavelengths, smooth_spectrum, color=self.colors['accent_red'], 
               linewidth=2.5, label='KOI-4878 b Spectrum', alpha=0.9)
        ax.fill_between(wavelengths, smooth_spectrum, base_depth*0.9, 
                       color=self.colors['accent_red'], alpha=0.2)
        
        # Аннотации
        annotations = [
            (4.3, base_depth + 25, 'CO₂ (Слабый)', self.colors['accent_orange']),
            (1.4, base_depth + 5, 'Нет H₂O', '#666666'),
            (2.5, base_depth + 5, 'Нет O₃', '#666666'),
            (3.3, base_depth + 5, 'Нет CH₄', '#666666')
        ]
        
        for x, y, text, color in annotations:
            ax.annotate(text, xy=(x, y), xytext=(x, y+10),
                       fontsize=10, color=color, ha='center',
                       arrowprops=dict(arrowstyle='->', color=color, alpha=0.7, lw=1))
        
        ax.legend(loc='upper right', facecolor='#333333', 
                 edgecolor=self.colors['accent_green'], labelcolor='white')
        
        # Встраиваем график
        canvas = FigureCanvasTkAgg(fig, master=self.tab_spectrum)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def create_verdict_tab(self):
        """Вкладка с вердиктом ИИ"""
        verdict_frame = tk.Frame(self.tab_verdict, bg=self.colors['bg_card'], relief=tk.RAISED, bd=3)
        verdict_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        title_lbl = tk.Label(verdict_frame, text="⛔ ВЕРДИКТ ЭКЗОЛОДЖИКИ", 
                            font=("Arial", 18, "bold"), fg=self.colors['accent_red'],
                            bg=self.colors['bg_card'])
        title_lbl.pack(pady=(20, 20))
        
        verdict_text = (
            "🔍 **АНАЛИЗ ВНУТРЕННЕГО СТРОЕНИЯ:**\n\n"
            "• Гипертрофированное железное ядро (~75% массы)\n"
            "• Критически тонкая силикатная мантия\n"
            "• Отсутствие активной тектоники плит\n\n"
            "🌋 **ГЕОДИНАМИЧЕСКИЙ СТАТУС:**\n\n"
            "• Магнитное динамо: НЕ АКТИВНО\n"
            "• Атмосферная защита: ОТСУТСТВУЕТ\n"
            "• Звездный ветер: ПОЛНОСТЬЮ СДУВАЕТ АТМОСФЕРУ\n\n"
            "💀 **ИТОГОВЫЙ ВЫВОД:**\n\n"
            "Несмотря на высокий ESI (0.978), планета является геофизически мертвым миром.\n"
            "Высокая плотность указывает на доминирование железа в составе, что приводит к:\n"
            "1. Подавлению мантийной конвекции\n"
            "2. Отсутствию тектоники плит\n"
            "3. Прекращению работы магнитного динамо\n"
            "4. Полной потере атмосферы под воздействием звездного ветра\n\n"
            "🎯 **РЕКОМЕНДАЦИЯ:** Исключить из списка приоритетных целей для поиска жизни."
        )
        
        verdict_lbl = tk.Label(verdict_frame, text=verdict_text,
                              font=("Consolas", 11), fg=self.colors['text_primary'],
                              bg=self.colors['bg_card'], justify=tk.LEFT,
                              wraplength=900)
        verdict_lbl.pack(padx=30, pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernPlanetPassport(root)
    root.mainloop()
