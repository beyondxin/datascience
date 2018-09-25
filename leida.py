#画蛛网图
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
labels = ["L","R","F","M","C"]
names = locals()
for i in range(5):
    names['cluster%s' %i] = data_zscored[data_zscored["y_hat"] == i].mean(axis = 0)

fig =plt.figure(figsize = (16,8))
ax = fig.add_subplot(111, polar=True)
for i in range(5):
    da = names['cluster%s' %i]
    angles = np.linspace(0, 2*np.pi, 5, endpoint=False)
    data = np.concatenate((da[:-1],[da[0]])) # 闭合
    angles = np.concatenate((angles, [angles[0]])) # 闭合
    
    ax.plot(angles,data,label = '客户群%s' %i)
    #ax.fill(angles, data, facecolor='r', alpha=0.25)# 填充
    ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
    ax.set_title("matplotlib雷达图", va='bottom', fontproperties="SimHei")
    #ax.set_rlim(0,2)
    ax.legend()
    ax.grid(True)
plt.show()
