import math
import matplotlib.pyplot as plt
import numpy as np

# Функція для вивода вектора
def print_vec(vec):
    size = int(math.sqrt(len(vec)))
    for i in range(0, size):
        for j in range(0, size):
            if vec[i * size + j] == 1:
                print('+', end='')
            else:
                print('-', end='')
        print()

# Функція активації
def activation_func(s, T):
    if s <= 0:
        return 0
    elif s > T:
        return T
    else:
        return s

# Паттерни для навчання
patterns = {
    '0': [
        -1, -1, -1, 1,
        -1, -1, -1, 1,
        1, -1, -1, 1,
        1, 1, 1, 1,
    ],
    '1': [
        -1, -1, -1, 1,
        -1, -1, 1, 1,
        -1, 1, -1, 1,
        1, -1, -1, 1,
    ],
}

# кільксть патернів
pattern_count = len(patterns)
# розмір
pattern_size = len(patterns['0'])
# Коефіцієнт k
k = 1 / pattern_count
# Поріг
T = k * pattern_size

# Вивід патернів для навчання
fig, axs = plt.subplots(2, 5, figsize=(10, 4))
for i, pattern in enumerate(patterns):
    reshaped_pattern = np.reshape(patterns[pattern], [4, 4])
    ax = axs[i // 5, i % 5]
    ax.axis('off')
    ax.set_title('learning ' + pattern)
    ax.imshow(reshaped_pattern, cmap='gray_r')
plt.tight_layout()
plt.show()

# Тестові вектори
test_vectors = {
    '0': [
        -1, -1, -1, 1,
        -1, -1, -1, 1,
        1, -1, -1, 1,
        1, 1, 1, 1,
    ],
    '1': [
        -1, -1, -1, 1,
        -1, -1, 1, 1,
        -1, 1, -1, 1,
        1, -1, -1, 1,
    ],
    '2': [
        1, 1, 1, 1,
        1, -1, -1, 1,
        1, -1, -1, 1,
        1, -1, -1, 1,
    ],
    '3': [
        1, 1, 1, -1,
        1, 1, 1, -1,
        -1, 1, 1, -1,
        -1, -1, -1, -1,
    ],
    '4': [
        1, 1, 1, -1,
        1, 1, -1, -1,
        1, -1, 1, -1,
        -1, 1, 1, -1,
    ],
}

# Створюємо загальне вікно для всіх графіків
fig, axs = plt.subplots(2, len(test_vectors) + 1, figsize=(15, 8))

# Виводимо патерни
for i, pattern in enumerate(patterns):
    reshaped_pattern = np.reshape(patterns[pattern], [4, 4])
    ax = axs[i // 5, i % 5]
    ax.axis('off')
    ax.set_title('learning ' + pattern)
    ax.imshow(reshaped_pattern, cmap='gray_r')

# Прохід по тестовим векторам і відображення графіків
for idx, tvi in enumerate(test_vectors):
    test_vector = test_vectors[tvi]

    matches = {pattern: 0 for pattern in patterns}

    for pattern_label, pattern_vector in patterns.items():
        num_matches = sum(1 for tv, pv in zip(test_vector, pattern_vector) if tv == pv)
        matches[pattern_label] = num_matches / pattern_size * 100

    # Вивід процентів в консоль
    print("Matching percentages for Test vector", tvi)
    for pattern, percentage in matches.items():
        print("Pattern", pattern, ":", percentage, "%")

    # Графік з процентами
    ax = axs[-1, idx]
    ax.bar(matches.keys(), matches.values())
    ax.set_title('% for Test vector ' + tvi)
    ax.set_xlabel('Pattern')
    ax.set_ylabel('Matching Percentage (%)')
    ax.set_ylim(0, 100)

    # Вивід тестового вектора
    reshaped_test_vector = np.reshape(test_vector, [4, 4])
    ax = axs[-2, idx]
    ax.axis('off')
    ax.set_title('Test vector ' + tvi)
    ax.imshow(reshaped_test_vector, cmap='gray_r')

plt.tight_layout()
plt.show()
