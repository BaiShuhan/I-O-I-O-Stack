# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:25:36 2018

@author: Administrator
"""

import matplotlib.pyplot as plt

source_address0 =  "txsp_ins_q2c.dat"

dataset=[]

#打开源trace文件、修改后目标存储文件
trace_f0 = open(source_address0,'r')

print("begin")

#逐行读取，放入元素为5个的列表中，将第一个时间time*1000000
for line in trace_f0:
    list1 = line.split()
    list1[0] = (float)(list1[0])
    list1[1] = (float)(list1[1])
    list1[1] = list1[1]*1000
    
    dataset.append(list1[1])
    
#关闭文件
trace_f0.close()

dataset.sort()
print(max(dataset))

plotDataset = [[],[]]
count = len(dataset)

for i in range(count):
    plotDataset[0].append(dataset[i])
    plotDataset[1].append(((float)(i+1))/count)
    
plt.plot(plotDataset[0], plotDataset[1], '-', linewidth=2, label='txsp')
plt.annotate('(%.3f, 1)' % max(dataset), xy=(max(dataset), 1), xytext=(max(dataset)-80, 0.8), arrowprops=dict(facecolor='black', shrink=0.1, width=0.5, headwidth=5))

plt.title('Request Response Time CDF', fontsize=14)
plt.xlabel('response time(ms)', fontsize=14)
plt.ylabel('CDF', fontsize=14)
plt.legend(loc='best')

#print(count, count1)

plt.savefig("txsp_ins_latency_cdf.pdf")

print("end")