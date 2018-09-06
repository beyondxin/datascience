#神经网络
from keras.models import Sequential
from keras.layers.core import Dense, Activation

model = Sequential()
model.add(Dense(10,input_dim =3))
model.add(Activation('relu'))
model.add(Dense(1,input_dim=10))
model.add(Activation('sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam',metrics=['accuracy'])


model.fit(x,y,epochs = 1000,batch_size = 10)
yp = model.predict_classes(x).reshape(len(y))
model.evaluate(x,y)

#测试测试
