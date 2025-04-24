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
        a = u[0]
        b = u[1]
        delta = b - a
        c = a + delta / 3
        e = a + 2 * delta / 3
        vec = delta / 3
        d = c + vec * np.exp(1j * np.pi / 3)
        new_points = np.array([a, c, d, e, b])
        
        segments = [
            koch_generator(new_points[:2], level-1),
            koch_generator(new_points[1:3], level-1),
            koch_generator(new_points[2:4], level-1),
            koch_generator(new_points[3:5], level-1)
        ]
        
        combined = []
        for i in range(len(segments)):
            if i < len(segments) - 1:
                combined.append(segments[i][:-1])
            else:
                combined.append(segments[i])
        return np.concatenate(combined)
        
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
        a = u[0]
        b = u[1]
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
            b
        ])
        
        segments = [
            new_points[0:2],
            new_points[1:3],
            new_points[2:4],
            new_points[3:5],
            new_points[4:6],
            new_points[5:7],
            new_points[6:8],
            new_points[7:9],
        ]
        
        result = []
        for seg in segments:
            res = minkowski_generator(seg, level-1)
            result.append(res[:-1])
        result.append(res[-1:])  
        return np.concatenate(result)


if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1])

    # 绘制不同层级的科赫曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        koch_points = koch_generator(init_u, i)
        ax = axs[i//2, i%2]
        ax.plot(np.real(koch_points), np.imag(koch_points), 'k-', lw=1)
        ax.set_title(f"Koch Curve Level {i+1}")
        ax.axis('equal')
        ax.axis('off')
    plt.tight_layout()
    plt.savefig('koch_curve.png')
    plt.show()


    # 绘制不同层级的闵可夫斯基香肠曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        # TODO: 调用minkowski_generator生成点
        minkowski_points = minkowski_generator(init_u, i)
        ax = axs[i//2, i%2]
        ax.plot(np.real(minkowski_points), np.imag(minkowski_points), 'k-', lw=1)
        ax.set_title(f"Minkowski Sausage Level {i+1}")
        ax.axis('equal')
        ax.axis('off')
    plt.tight_layout()
    plt.savefig('minkowski_sausage.png')
    plt.show()
