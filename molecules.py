import numpy as np
import matplotlib.pyplot as plt

# Функция для расчета силы притяжения Ван-дер-Ваальса
def vdW_force(r):
    A = 1.0 # Параметр притяжения
    r0 = 1.0 # Эквилибриумное значение расстояния
    return -2*A/r * (2*(r0/r)**12 - (r0/r)**6)

# Функция для расчета энергии Морзе
def morse_energy(r):
    D = 1.0 # Глубина потенциальной ямы
    a = 1.0 # Параметр, определяющий ширину ямы
    return D*(1 - np.exp(-a*(r - 1)))

# Функция для расчета ускорения частицы
def calculate_acceleration(positions):
    N = len(positions) # Количество частиц

    # Инициализация пустого массива ускорений
    accelerations = np.zeros((N,))

    # Расчет силы притяжения между частицами
    for i in range(N):
        for j in range(i+1, N):
            r = np.abs(positions[i] - positions[j]) # Расстояние между частицами
            force = vdW_force(r) # Сила притяжения Ван-дер-Ваальса
            accelerations[i] += force # Добавление силы к ускорению
            accelerations[j] -= force # Добавление противоположной силы к ускорению

    return accelerations

# Функция для моделирования движения частиц
def simulate_motion(N, m, dt, num_steps):
    positions = np.zeros((N,)) # Инициализация массива позиций частиц
    velocities = np.zeros((N,)) # Инициализация массива скоростей частиц

    # Генерация случайных начальных позиций и скоростей
    positions = np.random.uniform(-5, 5, (N,))
    velocities = np.random.uniform(-0.5, 0.5, (N,))

    # Основной цикл моделирования
    for step in range(num_steps):
        accelerations = calculate_acceleration(positions) # Расчет ускорений
        positions += velocities*dt # Обновление позиций
        velocities += accelerations*dt/m # Обновление скоростей

    return positions

# Параметры моделирования
N = 100 # Количество частиц
m = 1.0 # Масса одной частицы
dt = 0.01 # Шаг интегрирования
num_steps = 1000 # Количество шагов интегрирования

# Моделирование движения частиц
positions = simulate_motion(N, m, dt, num_steps)

# Визуализация результатов
plt.plot(positions, np.zeros((N,)), 'bo')
plt.xlabel('Position')
plt.ylabel('Particles')
plt.title('Simulation of van der Waals Gas')
plt.show()