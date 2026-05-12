'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/19Matplotlib.py
Description: 
'''
import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib

zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")
 
x = np.arange(1,11) 
y =  2  * x +  5 


# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
# plt.plot(x,y) 
# plt.show()

# x = np.arange(1,11) 
# y =  2  * x +  5 
# plt.title("学习 - DEMO", fontproperties=zhfont1) 
# plt.xlabel("x轴", fontproperties=zhfont1) 
# plt.ylabel("z轴", fontproperties=zhfont1) 
# plt.plot(x,y) 
# plt.show()


# plt.title("学习 - demo", fontproperties=zhfont1)
# plt.xlabel("x轴")
# plt.ylabel("y轴")
# plt.plot(x, y, "ob")
# plt.show()


# 计算正弦曲线上点的 x 和 y 坐标
x = np.arange(0,  3  * np.pi,  0.1) 
y = np.sin(x)
plt.title("sine wave form")  
# 使用 matplotlib 来绘制点
plt.plot(x, y) 
plt.show()


x =  [5,8,10] 
y =  [12,16,6] 
x2 =  [6,9,11] 
y2 =  [6,15,7] 
plt.bar(x, y, align =  'center') 
plt.bar(x2, y2, color =  'g', align =  'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis') 
plt.show()
