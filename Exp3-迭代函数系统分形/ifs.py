import numpy as np
import matplotlib.pyplot as plt

def get_fern_params():
    """
    返回巴恩斯利蕨的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    # TODO: 实现巴恩斯利蕨的参数
    fern_params = [
        # T1 (Stem)
        [0.00, 0.00, 0.00, 0.16, 0.00, 0.00, 0.01],
        
        # T2 (Successively smaller leaflets)
        [0.85, 0.04, -0.04, 0.85, 0.00, 1.60, 0.85],
        
        # T3 (Largest left-hand leaflet)
        [0.20, -0.26, 0.23, 0.22, 0.00, 1.60, 0.07],
        
        # T4 (Largest right-hand leaflet)
        [-0.15, 0.28, 0.26, 0.24, 0.00, 0.44, 0.07]
    ]
    return fern_params

def get_tree_params():
    """
    返回概率树的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    # TODO: 实现概率树的参数 
    tree_params = [
        # T1 (Trunk/Base scaling)
        [0.00, 0.00, 0.00, 0.50, 0.00, 0.00, 0.1],
        
        # T2 (Left Branch)
        [0.42, -0.42, 0.42, 0.42, 0.00, 0.20, 0.45],
        
        # T3 (Right Branch)
        [-0.42, 0.42, 0.42, 0.42, 0.00, 0.20, 0.45]
    ]
    return tree_params

def apply_transform(point, params):
    """
    应用单个变换到点
    :param point: 当前点坐标(x,y)
    :param params: 变换参数[a,b,c,d,e,f,p]
    :return: 变换后的新坐标(x',y')
    """
    # TODO: 实现变换公式
    x, y = point
    a, b, c, d, e, f, p = params
    
    new_x = a * x + b * y + e
    new_y = c * x + d * y + f
    
    return (new_x, new_y)

def run_ifs(ifs_params, num_points=100000, num_skip=100):
    """
    运行IFS迭代生成点集
    :param ifs_params: IFS参数列表
    :param num_points: 总点数
    :param num_skip: 跳过前n个点
    :return: 生成的点坐标数组
    """
    # TODO: 实现混沌游戏算法
    current_point = (0.0, 0.0)
    points = []
    for _ in range(num_points + num_skip):
        # 随机选择一个变换 (根据概率 p)
        # 使用 numpy 的 random.choice 函数，它可以根据给定的概率分布随机选择一个索引
        probabilities = [param[6] for param in ifs_params]
        selected_transform = np.random.choice(ifs_params, p=probabilities)
        
        # 应用选中的变换
        current_point = apply_transform(current_point, selected_transform)
        current_point = current_point
        
        # 如果迭代次数大于跳过数，就存储点
        if i >= num_skip:
            points.append(current_point)
    
    # 转换为numpy数组
    points = np.array(points)
    return points
    

def plot_ifs(points, title="IFS Fractal"):
    """
    绘制IFS分形
    :param points: 点坐标数组
    :param title: 图像标题
    """
    # TODO: 实现分形绘制
    plt.figure(figsize=(10, 10))
    
    # 绘制散点图
    plt.scatter(points[:,0], points[:,1], s=0.1, alpha=0.8, c='green')
    
    # 设置标题和坐标轴
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.axis('off')
    
    # 保存图像
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
    
    # 显示图像
    plt.show()

if __name__ == "__main__":
    # 生成并绘制巴恩斯利蕨
    fern_params = get_fern_params()
    fern_points = run_ifs(fern_params)
    plot_ifs(fern_points, "Barnsley Fern")
    
    # 生成并绘制概率树
    tree_params = get_tree_params()
    tree_points = run_ifs(tree_params)
    plot_ifs(tree_points, "Probability Tree")
