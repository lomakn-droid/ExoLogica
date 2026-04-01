import pandas as pd
import numpy as np

def main():
    print("🚀 Запуск ExoLogica UMSI-Анализатора (Path C)...")
    print("="*60)

    # 1. Загрузка и подготовка данных
    try:
        df = pd.read_csv('ExoLogica_Export-s.csv', sep=';')
        print(f"✅ База данных успешно загружена. Всего строк: {len(df)}")
        
        # Проверяем доступные колонки
        print(f"📋 Доступные колонки: {list(df.columns)[:10]}...")  # Показываем первые 10
        
    except FileNotFoundError:
        print("❌ Ошибка: Файл 'ExoLogica_Export-s.csv' не найден!")
        print("Убедитесь, что файл находится в той же папке, что и скрипт.")
        return
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        return

    # Определяем возможные варианты названий колонок
    name_cols = ['Планета', 'Planet', 'Name', 'Название']
    star_cols = ['Звезда', 'Star', 'Host Star', 'Звезда-хозяин']
    type_cols = ['Уточненная природа', 'Type', 'Planet Type', 'Тип']
    
    # Находим правильные названия колонок
    planet_col = None
    star_col = None  
    type_col = None
    
    for col in name_cols:
        if col in df.columns:
            planet_col = col
            break
            
    for col in star_cols:
        if col in df.columns:
            star_col = col
            break
            
    for col in type_cols:
        if col in df.columns:
            type_col = col
            break

    cols_needed = ['Масса(Me)', 'Радиус(Re)', 'Т-ра(K)', 'Плотн(г/см3)', 'PRI']
    
    # Конвертация и очистка числовых колонок
    for col in cols_needed:
        if col in df.columns:
            df[col] = df[col].replace(['-', 'Неизвестно', '', 'nan'], np.nan)
            if df[col].dtype == 'object':
                df[col] = df[col].str.replace(',', '.', regex=False)
            df[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            df[col] = np.nan

    # Оставляем только строки с необходимыми числовыми данными
    df_clean = df.dropna(subset=cols_needed).copy()
    df_clean = df_clean[(df_clean['Т-ра(K)'] > 0) & (df_clean['Радиус(Re)'] > 0)]
    
    print(f"✅ После очистки осталось {len(df_clean)} объектов для анализа.")

    # 2. Вычисление UMSI (Universal Matter Stability Index)
    df_clean['UMSI'] = (df_clean['Масса(Me)'] / (df_clean['Радиус(Re)'] * df_clean['Т-ра(K)'])) * 10000

    # 3. Фильтрация: РАЗОБЛАЧЕНИЕ ИМПОСТЕРОВ
    imposters_high = df_clean[(df_clean['PRI'] > 0.8) & (df_clean['UMSI'] > 230)]
    imposters_low = df_clean[(df_clean['PRI'] > 0.8) & (df_clean['UMSI'] < 18)]
    imposters = pd.concat([imposters_high, imposters_low]).sort_values('UMSI', ascending=False)

    print(f"\n🚨 НАЙДЕНО ИМПОСТЕРОВ: {len(imposters)}")
    if len(imposters) > 0:
        print("Эти планеты имели высокий PRI, но UMSI доказал, что это не каменистые миры:")
        
        # Создаем DataFrame для красивого вывода
        display_data = []
        for _, row in imposters.head(5).iterrows():
            display_data.append({
                'Планета': row.get(planet_col, 'N/A') if planet_col else 'N/A',
                'Звезда': row.get(star_col, 'N/A') if star_col else 'N/A', 
                'Тип': row.get(type_col, 'N/A') if type_col else 'N/A',
                'Масса(Me)': f"{row['Масса(Me)']:.2f}",
                'Радиус(Re)': f"{row['Радиус(Re)']:.2f}",
                'Плотн(г/см³)': f"{row['Плотн(г/см3)']:.2f}" if pd.notna(row['Плотн(г/см3)']) else 'N/A',
                'PRI': f"{row['PRI']:.3f}",
                'UMSI': f"{row['UMSI']:.2f}"
            })
        
        display_df = pd.DataFrame(display_data)
        print(display_df.to_string(index=False))
    else:
        print("Нет импостеров с такими критериями в этой выборке.")

    # 4. Фильтрация: ИСТИННЫЕ ЗЕМЛИ
    true_earths = df_clean[
        (df_clean['UMSI'] >= 18) & 
        (df_clean['UMSI'] <= 230) & 
        (df_clean['Радиус(Re)'] < 2.0) & 
        (df_clean['Т-ра(K)'] >= 200) & 
        (df_clean['Т-ра(K)'] <= 350)
    ].sort_values('PRI', ascending=False)

    print(f"\n💎 НАЙДЕНО ИСТИННЫХ ЗЕМЕЛЬ: {len(true_earths)}")
    if len(true_earths) > 0:
        print("Абсолютный топ кандидатов для телескопа JWST:")
        
        display_data_top = []
        for _, row in true_earths.head(10).iterrows():
            display_data_top.append({
                'Планета': row.get(planet_col, 'N/A') if planet_col else 'N/A',
                'Звезда': row.get(star_col, 'N/A') if star_col else 'N/A',
                'Масса(Me)': f"{row['Масса(Me)']:.2f}",
                'Радиус(Re)': f"{row['Радиус(Re)']:.2f}",
                'Т-ра(K)': f"{row['Т-ра(K)']:.1f}",
                'PRI': f"{row['PRI']:.3f}",
                'UMSI': f"{row['UMSI']:.2f}"
            })
        
        display_df_top = pd.DataFrame(display_data_top)
        print(display_df_top.to_string(index=False))
    else:
        print("Нет планет, соответствующих строгим критериям Истинных Земель.")

    # Оценка Земли для сравнения
    earth_umsi = (1 / (1 * 288)) * 10000
    print(f"\n🌍 Для справки: UMSI Земли равен примерно {earth_umsi:.2f}")

    # Дополнительная статистика
    print(f"\n📊 ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА:")
    print(f"Всего проанализировано планет: {len(df_clean)}")
    high_pri_count = len(df_clean[df_clean['PRI'] > 0.8])
    print(f"Планет с высоким PRI (>0.8): {high_pri_count}")
    
    stable_zone_count = len(df_clean[(df_clean['UMSI'] >= 18) & (df_clean['UMSI'] <= 230)])
    print(f"Планет в зоне стабильности UMSI (18-230): {stable_zone_count}")
    
    if high_pri_count > 0:
        reduction = ((high_pri_count - len(true_earths)) / high_pri_count) * 100
        print(f"Снижение шума (False Positives): {reduction:.1f}%")

    print("="*60)
    print("✨ Анализ завершен.")

if __name__ == "__main__":
    main()
