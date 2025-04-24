import numpy as np
import matplotlib.pyplot as plt

def get_fern_params():
    """
    返回巴恩斯利蕨的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    # TODO: 实现巴恩斯利蕨的参数
    fern_params = [
        
        [0.00, 0.00, 0.00, 0.16, 0.00, 0.00, 0.01],
        
     
        [0.85, 0.04, -0.04, 0.85, 0.00, 1.60, 0.85],
        
      
        [0.20, -0.26, 0.23, 0.22, 0.00, 1.60, 0.07],
        
    
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
       
        [0.00, 0.00, 0.00, 0.50, 0.00, 0.00, 0.1],
        
      
        [0.42, -0.42, 0.42, 0.42, 0.00, 0.20, 0.45],
        
    
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
    
   
    probs = np.array([p for a, b, c, d, e, f, p in ifs_params])
    cum_probs = np.cumsum(probs)
    
    for i in range(num_points + num_skip):
       
        r = np.random.random()
        selected_index = 0
        for j, cp in enumerate(cum_probs):
            if r <= cp:
                selected_index = j
                break
        
        selected_transform = ifs_params[selected_index]
        
       
        current_point = apply_transform(current_point, selected_transform)
        
      
        if i >= num_skip:
            points.append(current_point)
    
   
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
    
  
    plt.scatter(points[:,0], points[:,1], s=0.1, alpha=0.8, c='green')
    
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
