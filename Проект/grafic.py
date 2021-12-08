import matplotlib.pyplot as plt

rrr = [4,51,60,70.83]
qqq = [0.44,0.66,2.24,61]
www = [0.54,0.71,2.13,51]
sss = [0.68,0.84,4.50,30]
vvv = [0.86,1.2,4.50,25]
zzz = [1,1.30,5.75,70]
das = [2007,2008,2011,2017]

plt.plot(das,rrr,label = "План розрахунків бухгалтерського обліку підприємств")
plt.plot(das,qqq,label = "ППП УЗПИКС")
plt.plot(das,www,label = "ППП УТЕП")
plt.plot(das,sss,label = "ППП УОС")
plt.plot(das,vvv,label = "ППП УФРО")
plt.plot(das,zzz,label = "АРМ бухгалтера матеріально-технічного відділу")
plt.xlabel("Кількість заказів")
plt.ylabel("Потреба у товарі")
plt.legend()
plt.grid(True)

plt.show()