import numpy as np
import matplotlib.pyplot as plt

def koch_generator(u, level):
    """
    递归/迭代生成科赫曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    # TODO: 实现科赫曲线生成算法
     if level == 0:
        return u
    else:
        a, b = u
        c = a + (b - a) / 3
        d = c + (b - a) * np.exp(1j * np.pi / 3) / 3
        e = a + 2 * (b - a) / 3
        new_points = np.array([a, c, d, e, b])
        segments = [
            new_points[:2],
            new_points[1:3],
            new_points[2:4],
            new_points[3:5]
        ]
        result = []
        for seg in segments:
            result.append(koch_generator(seg, level-1))
        return np.concatenate(result)
        
def minkowski_generator(u, level):
    """
    递归/迭代生成闵可夫斯基香肠曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    # TODO: 实现闵可夫斯基香肠曲线生成算法
    if level == 0:
        return u
    else:
        a, b = u
        length = np.abs(b - a)
        angle = np.angle(b - a)
        step = length / 8
        new_points = np.array([
            a,
            a + step * np.exp(1j * angle),
            a + 2 * step * np.exp(1j * angle),
            a + 3 * step * np.exp(1j * angle),
            a + 4 * step * np.exp(1j * angle),
            a + 5 * step * np.exp(1j * angle),
            a + 6 * step * np.exp(1j * angle),
            a + 7 * step * np.exp(1j * angle),
            a + 8 * step * np.exp(1j * angle),
            b
        ])
        segments = [
            new_points[:2],
            new_points[1:3],
            new_points[2:4],
            new_points[3:5],
            new_points[4:6],
            new_points[5:7],
            new_points[6:8],
            new_points[7:9]
        ]
        result = []
        for seg in segments:
            result.append(minkowski_generator(seg, level-1))
        return np.concatenate(result)


if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1])

    # 绘制不同层级的科赫曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        koch_points = koch_generator(init_u, i)
        row, col = i // 2, i % 2
        axs[row, col].plot(np.real(koch_points), np.imag(koch_points), 'k-', lw=1)
        axs[row, col].set_title(f"Koch Curve Level {i}")
        axs[row, col].axis('equal')
        axs[row, col].axis('off')
    plt.tight_layout()
    plt.savefig('koch_curve.png')
    plt.show()


    # 绘制不同层级的闵可夫斯基香肠曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        minkowski_points = minkowski_generator(init_u, i)
        row, col = i // 2, i % 2
        axs[row, col].plot(np.real(minkowski_points), np.imag(minkowski_points), 'k-', lw=1)
        axs[row, col].set_title(f"Minkowski Sausage Level {i}")
        axs[row, col].axis('equal')
        axs[row, col].axis('off')
    plt.tight_layout()
    plt.savefig('minkowski_sausage.png')
    plt.show()
