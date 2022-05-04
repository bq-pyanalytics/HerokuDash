import pandas as pd

# Импортируем файлы
visits = pd.read_csv("../datasets/visits_log.csv")
orders = pd.read_csv("../datasets/orders_log.csv")
costs = pd.read_csv("../datasets/costs.csv")

# Переименуем столбцы
visits = visits.rename(
    columns={
        'Device': 'device',
        'End Ts': 'end_date_ts',
        'Source Id': 'source_id',
        'Start Ts': 'start_date_ts',
        'Uid': 'uid'
    })

orders = orders.rename(
    columns={
        'Buy Ts': 'buy_date_ts',
        'Revenue': 'revenue',
        'Uid': 'uid'
    })

costs = costs.rename(
    columns={
        'dt': 'cost_date_ts'
    })

# Приведем данные к нужному типу
visits['end_date_ts'] = pd.to_datetime(visits['end_date_ts'])
visits['start_date_ts'] = pd.to_datetime(visits['start_date_ts'])
orders['buy_date_ts'] = pd.to_datetime(orders['buy_date_ts'])
costs['cost_date_ts'] = pd.to_datetime(costs['cost_date_ts'])

# Создадим дополнительные столбцы
visits['year_date_ts'] = visits['start_date_ts'].dt.year
visits['month_date_ts'] = visits['start_date_ts'].astype('datetime64[M]')
visits['week_date_ts'] = visits['start_date_ts'].astype('datetime64[W]')
visits['day_date_ts'] = visits['start_date_ts'].astype('datetime64[D]')

