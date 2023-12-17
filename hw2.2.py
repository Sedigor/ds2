import pandas as pd

data = pd.read_csv("2017_jun_final.csv")


# Прочитайте отриману таблицю, використовуючи метод head
print(data.head)

# Визначте розмір таблиці за допомогою методу shape
print(data.shape)

columns_title = ['N', 
                'Job position', 
                'Programming language', 
                'Specialization', 
                'General work experience', 
                'Work exp at current place', 
                'Salary per month', 
                'Salary change over 12 months', 
                'City', 
                'Company size', 
                'Company type', 
                'Gender', 
                'Age', 
                'Education', 
                'University', 
                'Still a student', 
                'English level', 
                'Subject area', 
                'Date of completion', 
                'user_agent', 
                'exp', 
                'current_job_exp', 
                'salary', 
                'Currency', 
                'cls']

columns_title = [title.lower().replace(' ', '_') for title in columns_title]
data.columns = columns_title
print(data.head)


# Визначте типи всіх стовпців за допомогою dataframe.dtypes
print(data.dtypes)


# Порахуйте, яка частка пропусків міститься в кожній колонці (використовуйте методи isnull та sum)
nulls_part = data.isnull().sum() / len(data) * 100
print(nulls_part)


# Видаліть усі стовпці з пропусками, крім стовпця "Мова програмування"
columns_to_keep = ['programming_language']
data = data.dropna(subset=columns_to_keep)
print(data)


# Знову порахуйте, яка частка пропусків міститься в кожній колонці і переконайтеся, що залишився тільки стовпець "Мова програмування"
nulls_part = data.isnull().sum() / len(data) * 100
print(nulls_part)


# Видаліть усі рядки у вихідній таблиці за допомогою методу dropna
data.dropna()
print(data)


# Визначте новий розмір таблиці за допомогою методу shape
print(data.shape)


# Створіть нову таблицю python_data, в якій будуть тільки рядки зі спеціалістами, які вказали мову програмування Python
python_data = data[data['programming_language'] == 'Python']
print(python_data)


# Визначте розмір таблиці python_data за допомогою методу shape
print(python_data.shape)


# Використовуючи метод groupby, виконайте групування за стовпчиком "Посада"
python_data.groupby('job_position')
print(python_data)


# Створіть новий DataFrame, де для згрупованих даних за стовпчиком "Посада", виконайте агрегацію даних за допомогою методу agg і знайдіть мінімальне та максимальне значення у стовпчику "Зарплата.в.місяць"
aggregated_salaries = python_data.groupby('job_position')['salary_per_month'].agg(['min', 'max'])
print(aggregated_salaries)


# Створіть функцію fill_avg_salary, яка повертатиме середнє значення заробітної плати на місяць. Використовуйте її для методу apply та створіть новий стовпчик "avg"
aggregated_salaries['avg'] = python_data['salary_per_month'].mean()


# Створіть описову статистику за допомогою методу describe для нового стовпчика.
description = aggregated_salaries['avg'].describe()
print(description)


# Збережіть отриману таблицю в CSV файл
description.to_csv('description_aggregated_salaries.csv', index=False)

