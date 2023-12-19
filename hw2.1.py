import pandas as pd
import matplotlib.pyplot as plt


url = "https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8"
data = pd.read_html(url, match='Коефіцієнт народжуваності в регіонах України', thousands=".", decimal=",")[0]


# Вивести перші рядки таблиці за допомогою методу head
print(data.head())


# Визначте кількість рядків та стовпців у датафреймі (атрибут shape)
print(data.shape)


# Замініть у таблиці значення "—" на значення NaN
data = data.replace('—', pd.NA)
print(data)


# Визначте типи всіх стовпців за допомогою dataframe.dtypes
print(data.dtypes)


# Замініть типи нечислових колонок на числові. Підказка - це колонки, де знаходився символ "—"
first_column = data.iloc[:, 0]

non_numeric_columns = data.columns[data.dtypes == object][1:]
for col in non_numeric_columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')

data = pd.concat([first_column, data.iloc[:, 1:]], axis=1)

print(data)


# Порахуйте, яка частка пропусків міститься в кожній колонці (використовуйте методи isnull та sum)
nulls_part = data.isnull().sum() / len(data) * 100
print(nulls_part)


# Видаліть з таблиці дані по всій країні, останній рядок таблиці
data = data.iloc[:-1]
print(data)


# Замініть відсутні дані в стовпцях середніми значеннями цих стовпців (метод fillna)
mean_values = data.mean(numeric_only=True)
data = data.fillna(mean_values)
print(data)


# Отримайте список регіонів, де рівень народжуваності у 2019 році був вищим за середній по Україні
regions_higher_than_average_2019 = data[data['2019'] > data['2019'].mean()]['Регіон']
print(regions_higher_than_average_2019)


# У якому регіоні була найвища народжуваність у 2014 році?
region_highest_birth_rate_2014 = data[data['2014'] == data['2014'].max()]['Регіон'].values[0]
print(region_highest_birth_rate_2014)


# import matplotlib.pyplot as plt

data.plot(kind='bar', x='Регіон', y='2019', figsize=(10, 6))
plt.title('Народжуваність по регіонах у 2019 році')
plt.xlabel('Регіон')
plt.ylabel('Народжуваність')
plt.xticks(rotation=90)
plt.show()