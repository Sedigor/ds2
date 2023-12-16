import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("bestsellers with categories.csv")


# Прочитайте csv файл (використовуйте функцію read_csv)
# Виведіть перші п'ять рядків (використовується функція head)
# Виведіть розміри датасету (використовуйте атрибут shape)
# Відповідь: Про скільки книг зберігає дані датасет?

print(df.head)
print('-' * 20)
print(df.shape)


# Давайте змінимо регістр на малий, а пробіл замінимо на нижнє підкреслення (snake_style). А заразом і вивчимо корисний атрибут датафрейму: columns (можна просто присвоїти список нових імен цьому атрибуту)

df.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']


# Перевірте, чи у всіх рядків вистачає даних: виведіть кількість пропусків (na) у кожному зі стовпців (використовуйте функції isna та sum)
# Відповідь: Чи є в якихось змінних пропуски? (Так / ні)

na_per_column = df.isna().sum()
print(na_per_column)


# Перевірте, які є унікальні значення в колонці genre (використовуйте функцію unique)
# Відповідь: Які є унікальні жанри?

uniq_genre = df['genre'].unique()
print(uniq_genre)
print(f'Які є унікальні жанри? {uniq_genre}')


# Тепер подивіться на розподіл цін: побудуйте діаграму (використовуйте kind='hist')

df['price'].plot(kind='hist')

plt.title('Розподіл цін')
plt.xlabel('Ціна')
plt.ylabel('Частота')
plt.show()


# Визначте, яка ціна у нас максимальна, мінімальна, середня, медіанна (використовуйте функції max, min, mean, median)

max_price = df['price'].max()
min_price = df['price'].min()
mean_price = df['price'].mean()
median_price = df['price'].median()

print(f"Максимальна ціна?: {max_price}")
print(f"Мінімальна ціна?: {min_price}")
print(f"Середня ціна?: {mean_price}")
print(f"Медіанна ціна?: {median_price}")