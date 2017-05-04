import matplotlib.pyplot as mpl
import moduloDiplomado as mD

p1 = mD.createDic("martin", 23, 8)
print p1


graf = mD.graficaX2([1,2,3,4,5,6,7,8,9,10])
x = graf["eje x"]
y = graf["eje y"]

mpl.plot(x,y)
mpl.show()

