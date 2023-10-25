import matplotlib.pyplot as plt

# Задаем данные
categories = ['A', 'B', 'C', 'D']
values = [15, 24, 30, 12]

# Создаем столбчатую диаграмму
plt.subplot(131)
plt.bar(categories, values)
plt.subplot(132)
plt.scatter(categories, values)
plt.subplot(133)
plt.plot(categories, values)
plt.suptitle('Categorical Plotting')
plt.show()

# Настройка осей и заголовка
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.title('Столбчатая диаграмма')

# Отображаем диаграмму
plt.show()
