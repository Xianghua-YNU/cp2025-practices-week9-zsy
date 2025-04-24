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
    u = np.array([0, 1j])
    
    if level <= 0:
        return u
    
    α = np.pi/3 
    for _ in range(level):
        new_u = []
        for i in range(len(u)-1):
            start = u[i]
            end = u[i+1]
            
            p1 = st
            p2 = st + (end - st)/3
            p3 = p2 + (end - st)/3 * np.exp(1j*α)
            p4 = st + 2*(end - st)/3
            p5 = end
            
            new_u.extend([p1, p2, p3, p4, p5])
        
        u = np.array(new_u)
        
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
    u = np.array([0, 1]) 
    
    α = np.pi/2 
    for _ in range(level):
        new_u = []
        for i in range(len(u)-1):
            start = u[i]
            end = u[i+1]
            
            p1 = st
            p2 = st + (end - s)/4
            p3 = p2 + (end - st)/4 * np.exp(1j*α)
            p4 = p2 + (end - st)/4 * (1 + 1j)
            p5 = st + (end - st)/2 + (end - st)/4 * 1j
            p6 = st + (end - st)/2
            p7 = st + (end - st)/2 - (end - st)/4 * 1j
            p8 = st + 3*(end - st)/4 - (end - st)/4 * 1j
            p9 = st + 3*(end - st)/4
            p10 = end
            
            new_u.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        
        u = np.array(new_u)
    
    return u


if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1])

    # 绘制不同层级的科赫曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        koch_points = koch_generator(init_u, i+1)
        axs[i//2, i%2].plot(koch_points.real, koch_points.imag, 'k-', lw=1)
        axs[i//2, i%2].set_title(f"Koch Curve Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.savefig('koch_curve.png')
    plt.show()


    # 绘制不同层级的闵可夫斯基香肠曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        minkowski_points = minkowski_generator(init_u, i+1)
        axs[i//2, i%2].plot(minkowski_points.real, minkowski_points.imag, 'k-', lw=1)
        axs[i//2, i%2].set_title(f"Minkowski Sausage Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.savefig('minkowski_sausage.png')
    plt.show()
