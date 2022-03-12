import pandas as pd
from IPython.display import display


# Вариант №3 для заданий №5, 6 - письмо(writing score)
# мне нужен первый вариант- математика

# Загрузить датафрейм
arr = pd.read_csv('StudentsPerformance.csv')

print('названия колонок\n', arr.columns)

# вывод всего DataFrame
#display(arr)
#arr.to_csv(sys.stdout)
print(arr.head(5).to_string())



# Выолнить для всего датафрейма расчет описательных статистик
print(round(arr.describe(), 2))
print('Примечание:\n25% - 1 квантиль\n75% - 3 квантиль\n50% - медиана')
print()

# Определить какие типы данных используются в датафрейме
# print(arr.dtypes) #вывод лишь сведений о типах данных столбцов
print(arr.info()) #информация о датафрейме вроде заголовка, количество значений, типы данных столбцов
print()

# Рассчитать среднее значение оценки разных полов по варианту
print('Средняя оценка для девочек ->',round(arr[(arr['gender'] == 'female')].mean()['writing score'], 3))
print('Средняя оценка для мальчиков ->',round(arr[(arr['gender'] == 'male')].mean()['writing score'], 3))
print()

# Рассчитать отклонение значения оценки разных полов по варианту
print('Отклонение оценки для девочек ->', round(arr[(arr['gender'] == 'female')].std()['writing score'], 3))
print('Отклонение оценки для мальчиков ->', round(arr[(arr['gender'] == 'male')].std()['writing score'], 3))
print()

# Изучить способы обращений к датафрейму
print(arr["gender"].head()) #5 строк одного столбца сначала
print(arr['race/ethnicity'].tail()) #5 строк одного стобца сконца
print()

# Сделать сабсет датафрейма (параметры сабсета выбрать произвольно) двумя разными способами

# Сделать сабсет датафрейма из 5 строк, номер начальной строки равен порядковому номеру в списке группы
SubSet = arr[['gender',
              'race/ethnicity',
              'parental level of education',
              'lunch',
              'test preparation course']].iloc[20:25]
print('SubFrame')
display(SubSet)
print()

# Изменить индексы сабсета на имена (имена выбрать произвольно)
names = ['Муфаса',
         'Рафики',
         'Шрам',
         'Тимон',
         'Пумба']
# Сделать сабсет датафрейма обратившись по новому индексу
SubSet.index = names
display(SubSet)
print()

# Вывести одну строку исходного датафрейма, определить тип
print(arr.iloc[20])
print()

# Вывести одну колонку исходного датафрейма, определить тип
print(arr['gender'])
print()
