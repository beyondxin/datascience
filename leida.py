#画蛛网图
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
labels = ["L","R","F","M","C"]
names = locals()
for i in range(5):
    names['cluster%s' %i] = data_zscored[data_zscored["y_hat"] == i].mean(axis = 0)

fig =plt.figure()
ax = fig.add_subplot(111, polar=True)
for i in range(5):
    da = names['cluster%s' %i]
    angles = np.linspace(0, 2*np.pi, 5, endpoint=False)
    data = np.concatenate((da[:-1],[da[0]])) # 闭合
    angles = np.concatenate((angles, [angles[0]])) # 闭合
    
    ax.plot(angles,data)
    #ax.fill(angles, data, facecolor='r', alpha=0.25)# 填充
    ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
    ax.set_title("matplotlib雷达图", va='bottom', fontproperties="SimHei")
    ax.set_rlim(0,10)
    ax.grid(True)
plt.show()
