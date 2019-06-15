#простите за усеченный вариант задания

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('ex1data1.csv')

data1 = pd.DataFrame(file, columns = ['6.1101'])
data2 = pd.DataFrame(file, columns = ['17.592'])

X = data1['6.1101'].tolist()
Y = data2['17.592'].tolist()

x1 = [4,23]

y1 = [0,-5]
y1[0] = 2*x1[0]-10
y1[1] = 2*x1[1]-10


#plt.plot(x, y, 'r*', label = u'Данные из файла') Отображение с помощью plot
plt.scatter(X, Y, c ='blue',label = u'Данные из файла')
plt.plot(x1, y1, 'b', c ='red', label = u'Линейная функция y = 2x -10')

plt.title('График 2*X-10')

plt.ylabel('Y')
plt.xlabel('X')

plt.legend(loc='upper left')

plt.grid(True) #сетка

plt.savefig('plot.png', format='png', dpi=100)

plt.show()
