import pandas as pd
import matplotlib.pyplot as plt


# Прочитайте csv файл (використовуйте функцію read_csv)
df = pd.read_csv("bestsellers with categories.csv")


# Виведіть перші п'ять рядків (використовується функція head)
print(df.head)

# Виведіть розміри датасету (використовуйте атрибут shape)
df_size = df.shape
print(df_size)

books_in_df = df_size[0]
print(f'Про скільки книг зберігає дані датасет? Відповідь: {books_in_df}')


# Давайте змінимо регістр на малий, а пробіл замінимо на нижнє підкреслення (snake_style). А заразом і вивчимо корисний атрибут датафрейму: columns (можна просто присвоїти список нових імен цьому атрибуту)

df.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']


# Перевірте, чи у всіх рядків вистачає даних: виведіть кількість пропусків (na) у кожному зі стовпців (використовуйте функції isna та sum)
# Відповідь: Чи є в якихось змінних пропуски? (Так / ні)

na_per_column = df.isna().sum()
print(na_per_column)


# Перевірте, які є унікальні значення в колонці genre (використовуйте функцію unique)

uniq_genre = df['genre'].unique()
print(uniq_genre)
print(f'Які є унікальні жанри? Відповідь: {uniq_genre}')


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

print(f"Максимальна ціна? Відповідь: {max_price}")
print(f"Мінімальна ціна? Відповідь: {min_price}")
print(f"Середня ціна? Відповідь: {mean_price}")
print(f"Медіанна ціна? Відповідь: {median_price}")


# Пошук та сортування даних

max_rating = df['user_rating'].max()
print(f'Який рейтинг у датасеті найвищий? Відповідь: {max_rating}')

books_with_max_rating = df[df['user_rating'] == max_rating].shape[0]
print(f'Скільки книг мають такий рейтинг? Відповідь: {books_with_max_rating}')

max_reviews_index = df['reviews'].idxmax()
book_with_most_reviews = df.loc[max_reviews_index]
print(f'Яка книга має найбільше відгуків? Відповідь: {books_with_max_rating}')

data_2015 = df[df['year'] == 2015]
top_50_2015 = data_2015.nlargest(50, 'price')
most_expensive_2015 = top_50_2015.nlargest(1, 'price')
print(f'З тих книг, що потрапили до Топ-50 у 2015 році, яка книга найдорожча? Відповідь: {most_expensive_2015}')

data_2010_fiction = df[(df['year'] == 2010) & (df['genre'] == 'Fiction')]
fiction_in_top_50_2010 = data_2010_fiction.shape[0]
print(f'Скільки книг жанру Fiction потрапили до Топ-50 у 2010 році (використовуйте &)? Відповідь: {fiction_in_top_50_2010}')

data_4_9_2010_2011 = df[(df['user_rating'] == 4.9) & (df['year'].isin([2010, 2011]))]
count_4_9_2010_2011 = data_4_9_2010_2011.shape[0]
print(f'Скільки книг з рейтингом 4.9 потрапило до рейтингу у 2010 та 2011 роках (використовуйте | або функцію isin)? Відповідь: {fiction_in_top_50_2010}')

data_2015_under_8 = df[(df['year'] == 2015) & (df['price'] < 8)]
sorted_data_2015_under_8 = data_2015_under_8.sort_values(by='price')
last_book_sorted = sorted_data_2015_under_8.iloc[-1]
print(f'Яка книга остання у відсортованому списку? Відповідь: {last_book_sorted}')


# Агрегування даних та з'єднання таблиць

genre_price_stats = df.groupby('genre')['price'].agg(['min', 'max'])
print(genre_price_stats)

max_price_fiction = genre_price_stats.loc['Fiction', 'max']
min_price_fiction = genre_price_stats.loc['Fiction', 'min']

max_price_non_fiction = genre_price_stats.loc['Non Fiction', 'max']
min_price_non_fiction = genre_price_stats.loc['Non Fiction', 'min']

print(f'Максимальна ціна для жанру Fiction: Відповідь: {max_price_fiction}')
print(f'Мінімальна ціна для жанру Fiction: Відповідь: {min_price_fiction}')
print(f'Максимальна ціна для жанру Non Fiction: Відповідь: {max_price_non_fiction}')
print(f'Мінімальна ціна для жанру Non Fiction: Відповідь: {min_price_non_fiction}')


# Групування та підрахунок кількості книг для кожного автора

author_book_count = df.groupby('author')['name'].agg(book_count='count')
print(author_book_count)

dimensions = author_book_count.shape
author_most_books = author_book_count.idxmax()
num_books_author_most = author_book_count.max()

print(f'Якої розмірності вийшла таблиця? Відповідь: {dimensions}')
print(f'Який автор має найбільше книг? Відповідь: {author_most_books}')
print(f'Скільки книг цього автора? Відповідь: {num_books_author_most}')


# Створення датафрейму з середнім рейтингом для кожного автора

author_avg_rating = df.groupby('author')['user_rating'].agg(avg_rating='mean')
print(author_avg_rating)

author_min_avg_rating = author_avg_rating.idxmin()
min_avg_rating = author_avg_rating.min()

print(f'У якого автора середній рейтинг мінімальний? Відповідь: {author_min_avg_rating}')
print(f'Який у цього автора середній рейтинг? Відповідь: {min_avg_rating}')


# З'єднання датафреймів для кожного автора, що містить кількість книг та середній рейтинг

author_info = pd.concat([author_book_count, author_avg_rating], axis=1)
author_info_sorted = author_info.sort_values(by=['book_count', 'avg_rating'])

first_author = author_info_sorted.index[0]
print(f'Який автор перший у списку? Відповідь: {first_author}')