import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExoSpectraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ExoLogica AI - JWST Spectra Simulator")
        self.root.geometry("1100x700")
        self.root.configure(bg="#1e1e1e")
        
        self.df = None
        self.current_planet = None

        self.setup_ui()

    def setup_ui(self):
        # Левая панель
        left_frame = tk.Frame(self.root, width=260, bg="#2d2d2d", padx=10, pady=10)
        left_frame.pack_propagate(False)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        title_lbl = tk.Label(left_frame, text="ExoSpectra", fg="#00ffcc", bg="#2d2d2d", font=("Arial", 14, "bold"))
        title_lbl.pack(pady=10)

        # ИСПРАВЛЕНИЕ: Убрали кастомные цвета, чтобы macOS не прятала белый текст на светлом фоне
        load_btn = tk.Button(left_frame, text="Загрузить датасет (.csv)", command=self.load_data, 
                             font=("Arial", 10))
        load_btn.pack(fill=tk.X, pady=5)

        self.save_btn = tk.Button(left_frame, text="Сохранить график (PNG)", command=self.save_plot, 
                                  font=("Arial", 10), state=tk.DISABLED)
        self.save_btn.pack(fill=tk.X, pady=5)

        search_lbl = tk.Label(left_frame, text="Список планет (PRI > 0):", fg="white", bg="#2d2d2d", font=("Arial", 9))
        search_lbl.pack(anchor=tk.W, pady=(10, 0))

        # Список планет
        self.planet_listbox = tk.Listbox(left_frame, bg="#1e1e1e", fg="#00ffcc", font=("Consolas", 10), 
                                         selectbackground="#007acc", selectforeground="white", relief=tk.FLAT)
        self.planet_listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        self.planet_listbox.bind('<<ListboxSelect>>', self.on_planet_select)

        # Информационная панель
        self.info_text = tk.Text(left_frame, height=13, bg="#1e1e1e", fg="white", font=("Consolas", 8), relief=tk.FLAT, wrap=tk.WORD)
        self.info_text.pack(fill=tk.X, pady=10)
        self.info_text.insert(tk.END, "Ожидание данных...")
        self.info_text.config(state=tk.DISABLED)

        # Правая панель (График)
        self.right_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.fig, self.ax = plt.subplots(figsize=(10, 6), facecolor='#1e1e1e')
        self.fig.subplots_adjust(bottom=0.15, left=0.1, right=0.95, top=0.9)
        self.ax.set_facecolor('#1e1e1e')
        self.ax.tick_params(colors='white')
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.title.set_color('#00ffcc')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.draw_empty_plot()

    def load_data(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not filepath: return
        
        try:
            self.df = pd.read_csv(filepath, sep=';', decimal='.')
            
            if 'PRI' in self.df.columns:
                self.df['PRI'] = pd.to_numeric(self.df['PRI'], errors='coerce').fillna(0)
                self.df = self.df[self.df['PRI'] > 0].sort_values(by='PRI', ascending=False)
            
            self.planet_listbox.delete(0, tk.END)
            for idx, row in self.df.iterrows():
                self.planet_listbox.insert(tk.END, str(row['Планета']))
                
            messagebox.showinfo("Успех", f"Загружено планет: {len(self.df)}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл:\n{e}")

    def on_planet_select(self, event):
        selection = self.planet_listbox.curselection()
        if not selection: return
        
        planet_name = self.planet_listbox.get(selection[0])
        self.current_planet = planet_name
        planet_data = self.df[self.df['Планета'] == planet_name].iloc[0]
        
        self.update_info(planet_data)
        self.plot_spectrum(planet_data)
        self.save_btn.config(state=tk.NORMAL)

    def update_info(self, data):
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        
        info = (
            f"Планета: {data.get('Планета', 'N/A')}\n"
            f"Тип: {data.get('Уточненная природа', 'N/A')}\n"
            f"Плотн: {data.get('Плотн(г/см3)', 0)} г/см³\n"
            f"Т-ра: {data.get('Т-ра(K)', 0)} K\n"
            f"Радиус: {data.get('Радиус(Re)', 0)} Re\n"
            f"PRI: {data.get('PRI', 0):.3f}\n"
            f"ESI: {data.get('ESI', 0):.3f}\n"
        )
        self.info_text.insert(tk.END, info)
        self.info_text.config(state=tk.DISABLED)

    def generate_synthetic_spectrum(self, density, temp, radius):
        wavelengths = np.linspace(0.6, 5.0, 500)
        
        base_transit_depth = (radius * 0.01) ** 2 * 1e6
        spectrum = np.ones_like(wavelengths) * base_transit_depth
        
        noise_level = np.random.normal(0, base_transit_depth * 0.02, size=len(wavelengths))
        
        def add_line(center, strength, width):
            return strength * np.exp(-0.5 * ((wavelengths - center) / width)**2)

        try:
            density = float(density)
            temp = float(temp)
        except:
            density, temp = 5.5, 250

        if density < 4.8:
            spectrum += add_line(1.4, base_transit_depth * 0.15, 0.05)
            spectrum += add_line(1.9, base_transit_depth * 0.18, 0.06)
            spectrum += add_line(2.7, base_transit_depth * 0.25, 0.1)
            color_theme = "#00aaff"
            title_suffix = "(Мир-Океан: Доминирование H2O)"
            
        elif density > 7.8:
            spectrum += add_line(2.0, base_transit_depth * 0.05, 0.03)
            spectrum += add_line(4.3, base_transit_depth * 0.12, 0.08)
            color_theme = "#ff4444"
            title_suffix = "(Железный склеп: Бедная атмосфера CO2)"
            
        else:
            spectrum += add_line(1.4, base_transit_depth * 0.08, 0.05)
            spectrum += add_line(1.9, base_transit_depth * 0.10, 0.06)
            spectrum += add_line(3.3, base_transit_depth * 0.06, 0.04)
            spectrum += add_line(4.3, base_transit_depth * 0.15, 0.08)
            color_theme = "#00ffcc"
            title_suffix = "(Золотая зона: Смешанная биоатмосфера)"

        rayleigh = base_transit_depth * 0.05 * (0.6 / wavelengths)**4
        spectrum += rayleigh + noise_level
        
        return wavelengths, spectrum, color_theme, title_suffix

    def plot_spectrum(self, data):
        self.ax.clear()
        self.ax.set_facecolor('#1e1e1e')
        
        density = data.get('Плотн(г/см3)', 5.5)
        temp = data.get('Т-ра(K)', 250)
        radius = data.get('Радиус(Re)', 1.0)
        planet_name = data.get('Планета', 'Unknown')

        wl, spec, color, suffix = self.generate_synthetic_spectrum(density, temp, radius)

        self.ax.plot(wl, spec, color=color, linewidth=2, alpha=0.8)
        self.ax.fill_between(wl, spec, min(spec)*0.95, color=color, alpha=0.1)

        self.ax.set_title(f"Синтетический спектр JWST: {planet_name}\n{suffix}", color='white', pad=15)
        self.ax.set_xlabel("Длина волны (мкм)", color='gray')
        self.ax.set_ylabel("Глубина транзита (ppm)", color='gray')
        self.ax.grid(True, color='#333333', linestyle='--')
        self.ax.tick_params(colors='gray')

        y_max = max(spec)
        if density < 4.8 or (4.8 <= density <= 7.8):
            self.ax.text(1.4, y_max*0.95, 'H₂O', color='#00aaff', fontsize=12, ha='center', weight='bold')
            self.ax.text(2.7, y_max*0.95, 'H₂O', color='#00aaff', fontsize=12, ha='center', weight='bold')
        if 4.8 <= density <= 7.8:
            self.ax.text(3.3, y_max*0.95, 'CH₄', color='#00ffcc', fontsize=12, ha='center', weight='bold')
        if density > 7.8 or (4.8 <= density <= 7.8):
            self.ax.text(4.3, y_max*0.95, 'CO₂', color='#ffaa00', fontsize=12, ha='center', weight='bold')

        self.canvas.draw()

    def draw_empty_plot(self):
        self.ax.clear()
        self.ax.text(0.5, 0.5, "Загрузите CSV и выберите планету\nдля симуляции спектра", 
                     color='gray', fontsize=14, ha='center', va='center', transform=self.ax.transAxes)
        self.ax.set_axis_off()
        self.canvas.draw()

    def save_plot(self):
        if not self.current_planet: return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            initialfile=f"Spectrum_{self.current_planet.replace(' ', '_')}.png",
            title="Сохранить график как...",
            filetypes=[("PNG Image", "*.png")]
        )
        
        if filepath:
            try:
                self.fig.savefig(filepath, facecolor=self.fig.get_facecolor(), edgecolor='none', dpi=300)
                messagebox.showinfo("Сохранено", f"График успешно сохранен:\n{filepath}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить изображение:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExoSpectraApp(root)
    root.mainloop()
