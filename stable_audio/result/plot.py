import matplotlib.pyplot as plt
import re

def extract_values(file_path, value_keyword="KLD Value"):
    """
    从文本文件中提取值参数及其对应的数值
    
    参数:
        file_path (str): 文本文件路径
        value_keyword (str): 要提取的数值关键字，默认为"KLD Value"
        
    返回:
        list: 提取到的数值列表
    """
    values = []
    # 创建带空格和不带空格两种可能的关键字模式
    pattern_options = [
        re.compile(fr"{value_keyword}\s*:\s*(\d+\.\d+)"),  # 匹配 "Keyword: value"
        re.compile(fr"{value_keyword}\s*=\s*(\d+\.\d+)")   # 匹配 "Keyword = value"
    ]
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                # 尝试所有可能的模式匹配
                for pattern in pattern_options:
                    match = pattern.search(line)
                    if match:
                        try:
                            value = float(match.group(1))
                            values.append(value)
                            break  # 匹配成功后跳出模式循环
                        except ValueError:
                            print(f"数值转换错误: {line}")
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 不存在")
    return values


def plot_scatter(values, xlabel="Layer Index", ylabel=None, title=None):
    if not values:
        print("没有可绘制的数据！")
        return
    
    indices = list(range(len(values)))
    
    plt.figure(figsize=(12, 6))
    plt.scatter(indices, values, s=80, alpha=0.7, c='royalblue', edgecolor='black')

    mean_value = sum(values) / len(values)
    plt.axhline(y=mean_value, 
                color='red', 
                linestyle='--', 
                linewidth=2)
    
    print(mean_value)
    
    # 设置图表属性 - 无网格线
    plt.xlabel(xlabel, fontsize=20, fontname='Times New Roman', labelpad=18)
    plt.ylabel(ylabel, fontsize=20, fontname='Times New Roman', labelpad=18)
    if title:
        plt.title(title, fontsize=20, fontname='Times New Roman', pad=15)

    plt.tick_params(axis='both',          # 同时应用于x轴和y轴
                    direction='in',       # 刻度线方向向内
                    which='both',         # 同时应用于主要和次要刻度线
                    top=True,             # 顶部显示刻度线
                    right=True,           # 右侧显示刻度线
                    length=6,             # 刻度线长度
                    width=1.5,            # 刻度线宽度
                    colors='gray',        # 刻度线颜色变淡
                    labelcolor='black',   # 刻度标签颜色
                    pad=8)                # 刻度标签与坐标轴的距离

    plt.xticks(fontname='Times New Roman', fontsize=20)
    plt.yticks(fontname='Times New Roman', fontsize=20)
    
    # 自动调整布局
    plt.tight_layout()
    plt.savefig('KL_Score.png', dpi=1000, bbox_inches='tight')
    plt.show()
    
    
    

# 使用示例
if __name__ == "__main__":
    # 参数配置
    FILE_PATH = "FD_Openl3.txt"  # 替换为实际文件路径
    VALUE_KEYWORD = "FD Value"  # 可改为 "KL Value" 或 "KL" 等
    YLABEL = "FD Openl3"
    
    # 提取数据并绘图
    kld_values = extract_values(FILE_PATH, VALUE_KEYWORD)
    plot_scatter(kld_values, ylabel=YLABEL)


