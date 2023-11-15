import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
import csv
from heapq import nlargest

a = []
with open('llll.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        a.append(row)

b = []
c = []
for i in a:
    if len(i) != 0:
        b.append(i)
        c += i
x = []#!!!!!!!!!!!!!!!!!!!!!!
for i in b:
    q = []
    for j in i:
        j = j.strip()
        q.append(j)
    x.append(q)
d = []#!!!!!!!!!!!!!!!
for i in b:
    for j in i:
        j = j.strip()
        d.append(j)
d = d[17:] #общ 25963  4374
x = x[1:] #част 5723   999



y_val = []
x_val = []
empty = []

for i in range(25963):
    empty.append(0)



for i in x:
    z = empty
    for j in i:
        z[d.index(j)] = 1
    x_val.append(z)



for i in range(5723):
    v = []
    for j in range(5723):
        v.append(0)
    y_val.append(v)

for i in range(5723):
    y_val[i][i] = 1

model = keras.Sequential([
    Flatten(input_shape=(25963, 1, 1)),
    Dense(200, activation='relu'),
    Dense(100, activation='relu'),
    Dense(5723,  activation='softmax')
])

print(model.summary())

model.compile(optimizer='Adam',
             loss='MeanSquaredError',
             metrics=['accuracy'])


his = model.fit(np.array(x_val), np.array(y_val), epochs=60, validation_split=0.2)

a = []


with open('oooo.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        a.append(row)

b = []
c = []
for i in a:
    if len(i) != 0:
        b.append(i)
        c += i
c = c[9:]

model.save('model1')
model1 = keras.models.load_model('model1')
y = ['Food', 'Cat']#я хз как это сделать ну типо в массив поместить тэги которые юзер хочет
res = []
z = empty
for j in y:
  z[d.index(j)] = 1
res.append(z)
res = model1.predict(np.array(res))
res = nlargest(10, res)
res = res[0]
for i in range(10):
  print(c[np.argmax(res[i:])])




