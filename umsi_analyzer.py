import pandas as pd
import numpy as np

def main():
    print("🚀 Запуск ExoLogica UMSI-Анализатора (Path C)...")
    print("="*60)

    # 1. Загрузка и подготовка данных
    try:
        df = pd.read_csv('ExoLogica_Export-s.csv', sep=';')
        print(f"✅ База данных успешно загружена. Всего строк: {len(df)}")
    except FileNotFoundError:
        print("❌ Ошибка: Файл 'ExoLogica_Export-s.csv' не найден!")
        print("Убедитесь, что файл находится в той же папке, что и скрипт.")
        return
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        return

    cols_needed = ['Масса(Me)', 'Радиус(Re)', 'Т-ра(K)', 'Плотн(г/см3)', 'PRI', 'Планета', 'Звезда', 'Уточненная природа']
    
    # Конвертация и очистка
    for col in cols_needed:
        if col in df.columns:
            df[col] = df[col].replace(['-', 'Неизвестно', '', 'nan'], np.nan)
            if df[col].dtype == 'object':
                df[col] = df[col].str.replace(',', '.', regex=False)
            df[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            # Если колонки нет, создаем пустую или пропускаем (для имен планет)
            if col not in ['Планета', 'Звезда', 'Уточненная природа']:
                df[col] = np.nan

    # Оставляем только строки с необходимыми числовыми данными
    df_clean = df.dropna(subset=['Масса(Me)', 'Радиус(Re)', 'Т-ра(K)', 'PRI']).copy()
    df_clean = df_clean[(df_clean['Т-ра(K)'] > 0) & (df_clean['Радиус(Re)'] > 0)]
    
    print(f"✅ После очистки осталось {len(df_clean)} объектов для анализа.")

    # 2. Вычисление UMSI (Universal Matter Stability Index)
    # Формула: (Масса / (Радиус * Температура)) * 10000
    df_clean['UMSI'] = (df_clean['Масса(Me)'] / (df_clean['Радиус(Re)'] * df_clean['Т-ра(K)'])) * 10000

    # 3. Фильтрация: РАЗОБЛАЧЕНИЕ ИМПОСТЕРОВ
    # Планеты, которые обманули старый индекс PRI (PRI > 0.8), но раздавлены гравитацией (UMSI > 230)
    # Или слишком легкие (UMSI < 18), чтобы удержать атмосферу
    imposters_high = df_clean[(df_clean['PRI'] > 0.8) & (df_clean['UMSI'] > 230)]
    imposters_low = df_clean[(df_clean['PRI'] > 0.8) & (df_clean['UMSI'] < 18)]
    imposters = pd.concat([imposters_high, imposters_low]).sort_values('UMSI', ascending=False)

    print(f"\n НАЙДЕНО ИМПОСТЕРОВ: {len(imposters)}")
    if len(imposters) > 0:
        print("Эти планеты имели высокий PRI, но UMSI доказал, что это не каменистые миры:")
        display_cols = ['Планета', 'Уточненная природа', 'Масса(Me)', 'Радиус(Re)', 'Плотн(г/см3)', 'PRI', 'UMSI']
        # Проверяем наличие колонок перед выводом
        available_cols = [c for c in display_cols if c in imposters.columns]
        print(imposters[available_cols].head(5).to_string(index=False))
    else:
        print("Нет импостеров с такими критериями в этой выборке.")

    # 4. Фильтрация: ИСТИННЫЕ ЗЕМЛИ (The Golden Candidates)
    # Строгие физические рамки: 
    # UMSI от 18 до 230 (Зона Стабильности)
    # Радиус < 2.0 (чтобы исключить океаниды и мини-нептуны)
    # Температура от 200 до 350K (зона жидкой воды)
    true_earths = df_clean[
        (df_clean['UMSI'] >= 18) & 
        (df_clean['UMSI'] <= 230) & 
        (df_clean['Радиус(Re)'] < 2.0) & 
        (df_clean['Т-ра(K)'] >= 200) & 
        (df_clean['Т-ра(K)'] <= 350)
    ].sort_values('PRI', ascending=False)

    print(f"\n НАЙДЕНО ИСТИННЫХ ЗЕМЕЛЬ: {len(true_earths)}")
    if len(true_earths) > 0:
        print("Абсолютный топ кандидатов для телескопа JWST (Идеальный UMSI + Идеальная Температура):")
        display_cols_top = ['Планета', 'Звезда', 'Масса(Me)', 'Радиус(Re)', 'Т-ра(K)', 'PRI', 'UMSI']
        available_cols_top = [c for c in display_cols_top if c in true_earths.columns]
        print(true_earths[available_cols_top].head(10).to_string(index=False))
    else:
        print("Нет планет, соответствующих строгим критериям Истинных Земель.")

    # Оценка Земли для сравнения (Масса=1, Радиус=1, Т-ра~288K)
    earth_umsi = (1 / (1 * 288)) * 10000
    print(f"\n🌍 Для справки: UMSI Земли равен примерно {earth_umsi:.2f}")

    # Дополнительная статистика
    print(f"\n ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА:")
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
