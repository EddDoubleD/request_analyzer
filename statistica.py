from sys import argv

import pandas as pd

if __name__ == '__main__':
    directory = argv[1]
    # Загружаем данные
    df = pd.read_csv(directory + '/result.csv')

    quantiles_count = df['count'].quantile([0.25, 0.5, 0.75, 0.98])
    print("Квантили количества параметров:", quantiles_count)

    # Фильтрация запросов без ошибок
    no_error_df = df[df['failed'] == False]

    # Среднее время выполнения запросов без ошибки, сгруппированное по количеству параметров
    avg_time_by_count = no_error_df.groupby('count')['time'].mean()
    print("Среднее время выполнения запросов без ошибок по количествам параметров:", avg_time_by_count)

    error_rate = (df['failed'].sum() / len(df)) * 100
    print(f"Процент запросов с ошибками: {error_rate}%")

    max_time = df['time'].max()
    print(f"Максимальное время выполнения запроса: {max_time} ms")

    std_dev_time = no_error_df['time'].std()
    print("Стандартное отклонение времени выполнения успешных запросов:", std_dev_time)