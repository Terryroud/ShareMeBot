from tensorflow import keras
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