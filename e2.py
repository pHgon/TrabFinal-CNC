import math
import matplotlib.pyplot as plotLib

def y(x):
    return math.log10(x)

def yd(x):
    return (1/x)

x = 1.6
h = 0.25
qtdeIteracoes = 10

print("Euler")
yInicial = y(x)
xInicial = x
yValues = [yInicial]
xValues = [xInicial]
for i in range(0, qtdeIteracoes):
    yInicial= yInicial + h * y(xInicial)
    xInicial += h
    yValues.append(yInicial)
    xValues.append(xInicial)

plotLib.plot(xValues, yValues, linestyle='dashed', label='function')
plotLib.plot(xValues, yValues, 'ro', label='Points')
plotLib.show()

