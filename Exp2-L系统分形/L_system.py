"""
项目2: L-System分形生成与绘图模板
请补全下方函数，实现L-System字符串生成与绘图。
"""
import matplotlib.pyplot as plt
import math

def apply_rules(axiom, rules, iterations):
    """
    生成L-System字符串
    :param axiom: 初始字符串（如"F"或"0"）
    :param rules: 规则字典，如{"F": "F+F--F+F"} 或 {"1": "11", "0": "1[0]0"}
    :param iterations: 迭代次数
    :return: 经过多轮迭代后的最终字符串
    """
    # TODO: 实现L-System字符串生成逻辑
    
    current_string = axiom
    for _ in range(iterations):
        new_string = ""
        for char in current_string:
            if char in rules:
                new_string += rules[char]
            else:
                new_string += char
        current_string = new_string
    return current_string

def draw_l_system(instructions, angle, step, start_pos=(0,0), start_angle=0, savefile=None):
    """
    根据L-System指令绘图
    :param instructions: 指令字符串（如"F+F--F+F"）
    :param angle: 每次转向的角度（度）
    :param step: 每步前进的长度
    :param start_pos: 起始坐标 (x, y)
    :param start_angle: 起始角度（0表示向右，90表示向上）
    :param savefile: 若指定则保存为图片文件，否则直接显示
    """
    # TODO: 实现L-System绘图逻辑
   
    x, y = start_pos
    current_angle = start_angle
    stack = []
    fig, ax = plt.subplots()
    ax.plot([x], [y], 'k,')  # 起点
    
    for char in instructions:
        if char == 'F' or char == '0' or char == '1':
            # 计算下一个点
            rad = math.radians(current_angle)
            nx = x + step * math.cos(rad)
            ny = y + step * math.sin(rad)
            # 绘制线段
            ax.plot([x, nx], [y, ny], 'k-')
            # 更新当前位置
            x, y = nx, ny
        elif char == '+':
            # 向左转
            current_angle += angle_deg
        elif char == '-':
            # 向右转
            current_angle -= angle_deg
        elif char == '[':
            # 压栈（保存当前状态并左转）
            stack.append((x, y, current_angle))
            current_angle += angle_deg  # 根据规则应用左转
        elif char == ']':
            # 出栈（恢复状态并右转）
            x, y, current_angle = stack.pop()
            current_angle -= angle_deg  # 根据规则应用右转
    
    # 设置图形属性
    ax.set_title('L-System Fractal')
    ax.axis('equal')
    ax.axis('off')
    
    if savefile:
        plt.savefig(savefile, bbox_inches='tight')
    else:
        plt.show()
    plt.close()



if __name__ == "__main__":
    """
    主程序示例：分别生成并绘制科赫曲线和分形二叉树
    学生可根据下方示例，调整参数体验不同分形效果
    """
    # 1. 生成并绘制科赫曲线
axiom = "F"  # 公理
rules = {"F": "F+F--F+F"}  # 规则
iterations = 3  # 迭代次数
angle_deg = 60  # 每次转向角度
step = 10  # 步长

instr = apply_rules(axiom, rules, iterations)   
draw_l_system(instr, angle_deg, step, savefile="l_system_koch.png")

    # 2. 生成并绘制分形二叉树
axiom = "0"
rules = {"1": "11", "0": "1[0]0"}
iterations = 5
angle_deg = 45
step = 10

instr = apply_rules(axiom, rules, iterations)
draw_l_system(instr, angle_deg, step, savefile="fractal_tree.png")
