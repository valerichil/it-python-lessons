import matplotlib.pyplot as plt

# Задаем данные
time = [1, 2, 3, 4, 5]
temperature = [20, 22, 25, 24, 23]

# Создаем график
plt.plot(time, temperature)

# Настройка осей и заголовка
plt.xlabel('Время (часы)')
plt.ylabel('Температура (градусы Цельсия)')
plt.title('Зависимость температуры от времени')

# Отображаем график
plt.show()
