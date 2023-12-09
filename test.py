import pandas as pd

# Читання файлу
file_path = '2017_jun_final.csv'
data = pd.read_csv(file_path)

# Отримання списку стовпців з винятком 'Язык.программирования'
columns_to_keep = data['Язык.программирования']

# Видалення рядків з пропущеними значеннями у вибраних стовпцях
data = data.dropna(subset=columns_to_keep)

# Вивід результату
print(data)