import pandas as pd

# Задайте URL-адресу для таблиці
url = 'https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8'

# Зчитайте таблицю за допомогою read_html()
tables = pd.read_html(url)

# Виберіть таблицу, яку ви хочете обробити (наприклад, першу)
data = tables[12]
    

# # Виведіть перші рядки таблиці
# print("Перші рядки таблиці:")
# print(data.head())

# # Визначте кількість рядків та стовпців у датафреймі
# print("\nРозмір таблиці (рядки, стовпці):", data.shape)

# Замініть у таблиці значення "—" на значення NaN
data = data.replace('—', pd.NA)

# Визначте типи всіх стовпців
# print("\nТипи стовпців:")
# print(data.dtypes)

# Замініть типи нечислових колонок на числові
non_numeric_columns = data.columns[data.dtypes == object and not data["Регіон"]]
data[non_numeric_columns] = data[non_numeric_columns].apply(pd.to_numeric, errors='coerce')
# print(data)

# Порахуйте частку пропусків у кожному стовпці
missing_percentage = data.isnull().sum() / len(data) * 100

print(missing_percentage)

# Видаліть дані по всій країні (останній рядок таблиці)
data = data.iloc[:-1]

# Замініть відсутні дані в стовпцях середніми значеннями цих стовпців
data = data.fillna()
print(data)

# # Отримайте список регіонів, де рівень народжуваності у 2019 році був вищим за середній по Україні
# regions_higher_than_average_2019 = data[data['2019'] > data['2019'].mean()]['Регіон']

# # Виведіть список регіонів
# print("\nРегіони з вищим рівнем народжуваності у 2019 році за середнім по Україні:")
# print(regions_higher_than_average_2019)

# Знайдіть регіон з найвищою народжуваністю у 2014 році
region_highest_birth_rate_2014 = data[data['2014'] == data['2014'].max()]['Регіон'].values[0]

# print("\nРегіон з найвищою народжуваністю у 2014 році:", region_highest_birth_rate_2014)

# Побудуйте стовпчикову діаграму народжуваності по регіонах у 2019 році
import matplotlib.pyplot as plt

data.plot(kind='bar', x='Регіон', y='2019', figsize=(10, 6))
plt.title('Народжуваність по регіонах у 2019 році')
plt.xlabel('Регіон')
plt.ylabel('Народжуваність')
plt.xticks(rotation=90)
plt.show()
