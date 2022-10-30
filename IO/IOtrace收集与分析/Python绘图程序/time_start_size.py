# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:33:47 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from pylab import *

source_address =  "txsp_ins_w.dat"

x_values=[]
y_values=[]

#打开源trace文件、修改后目标存储文件
trace_f1 = open(source_address,'r')

print("begin")

#逐行读取，放入元素为5个的列表中，将第一个时间time*1000000
for line in trace_f1:
    list1 = line.split()
    list1[0] = (float)(list1[0])
    list1[1] = (int)(list1[1])
    list1[2] = (int)(list1[2])
      
    list1[2] = list1[2]-list1[1]
    
    x_values.append(list1[0])
    y_values.append(list1[1]-11966464)    
    
#关闭文件
trace_f1.close()
print("min sector number:",min(y_values))

'''
scatter() 
x:横坐标 y:纵坐标 s:点的尺寸
'''

plt.scatter(x_values, y_values, c='blue', s=5, label='txsp')
 
# 设置图表标题并给坐标轴加上标签
plt.title('Request Start Sertor Numbers', fontsize=14)
#plt.title('Request size', fontsize=14)
plt.xlabel('time(s)', fontsize=14)
plt.ylabel('sector number', fontsize=14)
#plt.ylabel('size(sector)', fontsize=14)
plt.legend(loc='best')

'''
科学计数法表示
'''
ax = plt.gca()  #获取当前图像的坐标轴信息
xfmt = ScalarFormatter(useMathText=True)
xfmt.set_powerlimits((0, 0))  # 
gca().yaxis.set_major_formatter(xfmt)

 
# 设置刻度标记的大小
#plt.tick_params(axis='both', which='major', labelsize=14)
 
# 设置每个坐标轴的取值范围
#plt.axis([0, 1100, 0, 1100000])
#plt.show()
#plt.savefig("txsp_ins_time-start.pdf")
plt.savefig("txsp_ins_time-start.pdf")

print("end")       