import numpy as np
import matplotlib.pyplot as plt

# =========================
# =========================
def apply_transform(points, M):
    return points @ M.T

def draw(points, M, title, subplot):
    pts_new = apply_transform(points, M)

    plt.subplot(*subplot)
    plt.axhline(0)
    plt.axvline(0)
    plt.grid(True)
    plt.axis('equal')

    plt.plot(
        np.append(points[:,0], points[0,0]),
        np.append(points[:,1], points[0,1]),
        'bo-', label='Original'
    )
    plt.plot(
        np.append(pts_new[:,0], pts_new[0,0]),
        np.append(pts_new[:,1], pts_new[0,1]),
        'ro-', label='Transformed'
    )
    plt.title(title)
    plt.legend(fontsize=8)

# =========================
# Исходный многоугольник
# =========================
polygon = np.array([
    [1, 1],
    [3, 1],
    [3, 2],
    [2, 3],
    [1, 2]
])

# Параметры
a, b, c, d = 2, 3, 2, 3

# =========================
# Матрицы преобразований
# =========================

# 1. Отражение относительно y = ax
M1 = (1 / (1 + a**2)) * np.array([
    [1 - a**2, 2*a],
    [2*a, a**2 - 1]
])

# 2. Ортогональная проекция на y = bx
v = np.array([1, b])
M2 = np.outer(v, v) / (v @ v)

# 3. Поворот на 10c градусов
theta = np.deg2rad(10 * c)
M3 = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# 4. Центральная симметрия
M4 = -np.eye(2)

# 5. Отражение y=ax, затем поворот -10d
theta2 = np.deg2rad(-10 * d)
R2 = np.array([
    [np.cos(theta2), -np.sin(theta2)],
    [np.sin(theta2),  np.cos(theta2)]
])
M5 = R2 @ M1

# 6. y=0 → y=ax, x=0 → y=bx
M6 = np.array([
    [1, 0],
    [a, b]
])

# 7. y=ax → y=0, y=bx → x=0
M7 = np.linalg.inv(M6)

# 8. Перестановка прямых y=ax и y=bx
M8 = M6 @ M7

# 9. Недигональная, круг → круг площади c
scale = np.sqrt(c)
M9 = np.array([
    [scale, 1],
    [0, scale]
])

# 10. Недигональная, круг → некруг площади d
M10 = np.array([
    [d, 1],
    [0, 1]
])

# 11. AB ≠ BA
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[0, -1],
              [1,  0]])

# 12. AB = BA
C = np.array([[2, 0],
              [0, 1]])
D = np.array([[3, 0],
              [0, 4]])

# =========================
# Визуализация
# =========================
plt.figure(figsize=(12, 8))

draw(polygon, M1,  "1. Reflection y = ax", (2, 4, 1))
draw(polygon, M2,  "2. Projection to y = bx", (2, 4, 2))
draw(polygon, M3,  "3. Rotation 10c°", (2, 4, 3))

draw(polygon, M4,  "4. Central symmetry", (2, 4, 4))
draw(polygon, M5,  "5. Reflect + rotate", (2, 4, 5))
draw(polygon, M6,  "6. y=0→y=ax, x=0→y=bx", (2, 4, 6))

draw(polygon, M7,  "7. Inverse mapping", (2, 4, 7))
draw(polygon, M8,  "8. Swap y=ax and y=bx", (2, 4, 8))

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))

draw(polygon, M9,  "9. Circle → circle (area c)", (2, 5, 1))

draw(polygon, M10, "10. Circle → non-circle (area d)", (2, 5, 2))

draw(polygon, A,   "11. A", (2, 5, 3))
draw(polygon, B,   "11. B", (2, 5, 4))

draw(polygon, A @ B, "11. AB", (2, 5, 5))
draw(polygon, B @ A, "11. BA", (2, 5, 6))

draw(polygon, C,   "12. A", (2, 5, 7))
draw(polygon, D,   "12. B", (2, 5, 8))

draw(polygon, C @ D, "12. AB", (2, 5, 9))
draw(polygon, D @ C, "12. BA", (2, 5, 10))

plt.tight_layout()
plt.show()
