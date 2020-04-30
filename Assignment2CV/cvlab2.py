# -*- coding: utf-8 -*-
"""CVLab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D694w2nJ5yB-Ad9vKPU64JEEEueAsYbW
"""

from keras.datasets import cifar10
import matplotlib.pyplot as plt
import numpy as np
import keras 
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D, SeparableConv2D
from keras.regularizers import l2
from keras.optimizers import SGD, RMSprop
from keras.utils import to_categorical
from keras.layers.normalization import BatchNormalization
from keras.utils.vis_utils import plot_model
from keras.layers import Input, GlobalAveragePooling2D
from keras import models
from keras.models import Model
from sklearn.model_selection import train_test_split
import tensorflow

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

mean = np.mean(x_train)
std = np.std(x_train)
x_train = (x_train - mean)/(std)
x_test = (x_test - mean)/(std)

# one hot encode target values
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)





#FINAL TABLE IMPLEMENTATION!!!!!!!!!!!

input_img = Input(shape=(32,32, 3))
print(input_img.shape)

  #layer0 = Conv2D(8, (3,3),strides=(2,2) ,padding='valid' ,activation='relu')(input_img)
  #layer1 = Conv2D(8, (3,3), padding='valid', activation='relu')(input_img)
  #layer2 = Conv2D(8, (3,3), padding='same', activation='relu')(layer1)
  #layer3 = MaxPooling2D((3,3), strides=(2,2), padding='same')(input_img)
  #layer4 = Conv2D(8, (3,3), padding='valid', activation='relu')(layer1)
  #layer5 = Conv2D(8, (3,3), strides=(2,2), padding='valid', activation='relu')(input_img)
  #layer6 = Conv2D(8, (3,3), padding='valid', activation='relu')(layer2)
  #layer7 =Input(shape=(32, 32, 3)) #3 x fig 5
  #layer70 = Conv2D(8, (1,1), padding='same', activation='relu')(layer7)
  #layer71 = Conv2D(8, (3,3), padding='same', activation='relu')(layer70)
  #layer72 = Conv2D(8, (3,3), padding='same', activation='relu')(layer71)
  #layer73 = Conv2D(8, (1,1), padding='same', activation='relu')(layer7)
  #layer74 = Conv2D(8, (3,3), padding='same', activation='relu')(layer73)
  #layer75 = MaxPooling2D((3,3), strides=(1,1), padding='same')(layer7)
  #layer76 = Conv2D(8, (1,1), padding='same', activation='relu')(layer75)
  #layer77 = Conv2D(8, (1,1), padding='same', activation='relu')(layer7)
  #mid_1 = keras.layers.concatenate([layer72, layer74, layer76, layer77])
  ##second fig 5
  ##layer8 =Input(shape=(32, 32, 3)) #3 x fig 5
  #layer80 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_1)
  #layer81 = Conv2D(8, (3,3), padding='same', activation='relu')(layer80)
  #layer82 = Conv2D(8, (3,3), padding='same', activation='relu')(layer81)
  #layer83 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_1)
  #layer84 = Conv2D(8, (3,3), padding='same', activation='relu')(layer83)
  #layer85 = MaxPooling2D((3,3), strides=(1,1), padding='same')(mid_1)
  #layer86 = Conv2D(8, (1,1), padding='same', activation='relu')(layer85)
  #layer87 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_1)
  #mid_12 = keras.layers.concatenate([layer82, layer84, layer86, layer87])
  ##third fig 5
  #layer90 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_12)
  #layer91 = Conv2D(8, (3,3), padding='same', activation='relu')(layer90)
  #layer92 = Conv2D(8, (3,3), padding='same', activation='relu')(layer91)
  #layer93 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_12)
  #layer94 = Conv2D(8, (3,3), padding='same', activation='relu')(layer93)
  #layer95 = MaxPooling2D((3,3), strides=(1,1), padding='same')(mid_12)
  #layer96 = Conv2D(8, (1,1), padding='same', activation='relu')(layer95)
  #layer97 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_12)
  #mid_13 = keras.layers.concatenate([layer92, layer94, layer96, layer97])  


######################5 x fig 6

layer100 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img) #(mid_13)
layer101 = Conv2D(8, (1,3), padding='same', activation='relu')(layer100)
layer102 = Conv2D(8, (3,1), padding='same', activation='relu')(layer101)
layer103 = Conv2D(8, (1,3), padding='same', activation='relu')(layer102)
layer104 = Conv2D(8, (3,1), padding='same', activation='relu')(layer103)

### 1st layer
layer105 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img) #(mid_13)
layer106 = Conv2D(8, (1,3), padding='same', activation='relu')(layer105)
layer107 = Conv2D(8, (3,1), padding='same', activation='relu')(layer106)

### 2nd layer
layer108 = MaxPooling2D((3,3), strides=(1,1), padding='same')(input_img) #(mid_13)
layer109 = Conv2D(8, (1,1), padding='same', activation='relu')(layer108)

### 3rd layer
layer110 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img) #(mid_13)

### Concatenate
mid_14 = keras.layers.concatenate([layer104, layer107, layer109, layer110])

###################Second in Fig 6
layer200 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_14)
layer201 = Conv2D(8, (1,3), padding='same', activation='relu')(layer200)
layer202 = Conv2D(8, (3,1), padding='same', activation='relu')(layer201)
layer203 = Conv2D(8, (1,3), padding='same', activation='relu')(layer202)
layer204 = Conv2D(8, (3,1), padding='same', activation='relu')(layer203)

### 1st layer
layer205 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_14)
layer206 = Conv2D(8, (1,3), padding='same', activation='relu')(layer205)
layer207 = Conv2D(8, (3,1), padding='same', activation='relu')(layer206)

### 2nd layer
layer208 = MaxPooling2D((3,3), strides=(1,1), padding='same')(mid_14)
layer209 = Conv2D(8, (1,1), padding='same', activation='relu')(layer208)

### 3rd layer
layer210 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_14)

### Concatenate
mid_15 = keras.layers.concatenate([layer204, layer207, layer209, layer210])

########################## Third in Fig 6
layer300 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_15)
layer301 = Conv2D(8, (1,3), padding='same', activation='relu')(layer300)
layer302 = Conv2D(8, (3,1), padding='same', activation='relu')(layer301)
layer303 = Conv2D(8, (1,3), padding='same', activation='relu')(layer302)
layer304 = Conv2D(8, (3,1), padding='same', activation='relu')(layer303)

### 1st layer
layer305 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_15)
layer306 = Conv2D(8, (1,3), padding='same', activation='relu')(layer305)
layer307 = Conv2D(8, (3,1), padding='same', activation='relu')(layer306)

### 2nd layer
layer308 = MaxPooling2D((3,3), strides=(1,1), padding='same')(mid_15)
layer309 = Conv2D(8, (1,1), padding='same', activation='relu')(layer308)

### 3rd layer
layer310 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_15)

### Concatenate
mid_16 = keras.layers.concatenate([layer304, layer307, layer309, layer310])

#Fourth in Fig 6
layer400 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_16)
layer401 = Conv2D(8, (1,3), padding='same', activation='relu')(layer400)
layer402 = Conv2D(8, (3,1), padding='same', activation='relu')(layer401)
layer403 = Conv2D(8, (1,3), padding='same', activation='relu')(layer402)
layer404 = Conv2D(8, (3,1), padding='same', activation='relu')(layer403)

### 1st layer
layer405 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_16)
layer406 = Conv2D(8, (1,3), padding='same', activation='relu')(layer405)
layer407 = Conv2D(8, (3,1), padding='same', activation='relu')(layer406)

### 2nd layer
layer408 = MaxPooling2D((3,3), strides=(1,1), padding='same')(mid_16)
layer409 = Conv2D(8, (1,1), padding='same', activation='relu')(layer408)

### 3rd layer
layer410 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_16)

### Concatenate
mid_17 = keras.layers.concatenate([layer404, layer407, layer409, layer410])

################ Fifth in fig 6
layer500 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_17)
layer501 = Conv2D(8, (1,3), padding='same', activation='relu')(layer500)
layer502 = Conv2D(8, (3,1), padding='same', activation='relu')(layer501)
layer503 = Conv2D(8, (1,3), padding='same', activation='relu')(layer502)
layer504 = Conv2D(8, (3,1), padding='same', activation='relu')(layer503)

### 1st layer
layer505 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_17)
layer506 = Conv2D(8, (1,3), padding='same', activation='relu')(layer505)
layer507 = Conv2D(8, (3,1), padding='same', activation='relu')(layer506)

### 2nd layer
layer508 = MaxPooling2D((3,3), strides=(1,1), padding='same')(mid_17)
layer509 = Conv2D(8, (1,1), padding='same', activation='relu')(layer508)

### 3rd layer
layer510 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_17)

### Concatenate
mid_18 = keras.layers.concatenate([layer504, layer507, layer509, layer510])


########  2 x fig 7

## layer 0
layer600 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_18)

layer601 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_18)

### 1st layer
layer602 = Conv2D(8, (1,3), padding='same', activation='relu')(layer601)

### 2nd layer
layer603 = Conv2D(8, (3,1), padding='same', activation='relu')(layer601)

layer604 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_18)
layer605 = Conv2D(8, (3,3), padding='same', activation='relu')(layer604)

### 3rd layer
layer606 = Conv2D(8, (1,3), padding='same', activation='relu')(layer605)

### 4th layer
layer607 = Conv2D(8, (3,1), padding='same', activation='relu')(layer605)

### 5th layer
layer608 = MaxPooling2D((3,3), strides=(1,1), padding='same')(mid_18)
layer609 = Conv2D(8, (1,1), padding='same', activation='relu')(layer608)

### Concatenate
mid_19 = keras.layers.concatenate([layer600, layer602, layer603, layer606, layer607, layer609])

######## Second Fig 7

## layer 0
layer700 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_19)

layer701 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_19)

### 1st layer
layer702 = Conv2D(8, (1,3), padding='same', activation='relu')(layer701)

### 2nd layer
layer703 = Conv2D(8, (3,1), padding='same', activation='relu')(layer701)

layer704 = Conv2D(8, (1,1), padding='same', activation='relu')(mid_19)
layer705 = Conv2D(8, (3,3), padding='same', activation='relu')(layer704)

### 3rd layer
layer706 = Conv2D(8, (1,3), padding='same', activation='relu')(layer705)

### 4th layer
layer707 = Conv2D(8, (3,1), padding='same', activation='relu')(layer705)

### 5th layer
layer708 = MaxPooling2D((3,3), strides=(1,1), padding='same')(mid_19)
layer709 = Conv2D(8, (1,1), padding='same', activation='relu')(layer708)

### Concatenate
mid_20 = keras.layers.concatenate([layer600, layer702, layer703, layer706, layer707, layer709])


layerpool =MaxPooling2D((8,8), strides=(1,1), padding='same')(mid_20)
flatlayer = Flatten()(layerpool)
outputTable = Dense(10, activation='softmax')(flatlayer)
print(outputTable.shape)
modelTable = Model([input_img], outputTable)


modelTable.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = modelTable.fit(x_train, y_train, epochs=10,validation_split=0.1, batch_size=100)

plt.title('Accuracy')
plt.plot(history.history['acc'], label='test')
plt.legend()
plt.show()
temp,accurate = modelTable.evaluate(x_test, y_test, batch_size = 100)
print(accurate)
modelTable.summary()

"""GoogleNet"""

input_img = Input(shape=(32, 32, 3))

conv1 = Conv2D(16, (7,7), padding='same', strides=(2,2), activation='relu')(input_img)
maxpool1 = MaxPooling2D((3,3), strides=(2,2), padding='valid')(conv1)
norm1 = tf.nn.lrn(maxpool1)
conv2 = Conv2D(16, (1,1), padding='same', strides=(1,1), activation='relu')(norm1)
conv3 = Conv2D(16, (3,3), padding='same', strides=(1,1), activation='relu')(conv2)
norm2 = tf.nn.lrn(conv3)
maxpool2 = MaxPooling2D((3,3), strides=(2,2), padding='valid')(norm2)
dimRed1 = dimension_reductions(maxpool2)
dimRed2 = dimension_reductions(dimRed1)
maxpool3 = MaxPooling2D((3,3), strides=(2,2), padding='valid')(dimRed2)
dimRed3 = dimension_reductions(maxpool3)

# First auxiliary output
avg1 = AveragePooling2D(pool_size=(5,5), strides=(3,3))(dimRed3)
conv4 = Conv2D(16, (1,1), padding='same', activation='relu')(avg1)
flat1 = Flatten()(conv4)
dense1 = Dense(1024, activation='relu')(flat1)
drop1 = Dropout(0.5)(dense1)
dense2 = Dense(1000, activation='relu')(drop1)
loss1 = Dense(10, activation='softmax')(dense2)

dimRed4 = dimension_reductions(dimRed3)
dimRed5 = dimension_reductions(dimRed4)
dimRed6 = dimension_reductions(dimRed5)

# Second auxiliary output
avg2 = AveragePooling2D(pool_size=(5,5), strides=(3,3))(dimRed6)
conv5 = Conv2D(16, (1,1), padding='same', activation='relu')(avg2)
flat2 = Flatten()(conv5)
dense3 = Dense(1024, activation='relu')(flat2)
drop2 = Dropout(0.5)(dense3)
dense4 = Dense(1000, activation='relu')(drop2)
loss2 = Dense(10, activation='softmax')(dense4)

dimRed7 = dimension_reductions(dimRed6)
maxpool4 = MaxPooling2D((3,3), strides=(2,2), padding='valid')(dimRed7)
dimRed8 = dimension_reductions(maxpool4)
dimRed9 = dimension_reductions(dimRed8)

avg3 = AveragePooling2D(pool_size=(7,7), strides=(1,1))(dimRed9)
flat3 = Flatten()(avg3)

dense5 = Dense(1200, activation='relu')(flat3)
drop3 = Dropout(0.5)(dense5)
dense6 = Dense(600, activation='relu')(drop3)
dense7 = Dense(150, activation='relu')(dense6)

output = Dense(10, activation='softmax')(dense7)
model = Model([input_img], outputs=[loss1, loss2, output])
start = time.time()
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'], loss_weights=[0.3,0.3,1])

history = model.fit(x_train, [y_train,y_train,y_train], epochs=10, batch_size=100, shuffle=True)
end = time.time()
print()
print(end - start)

score = model.evaluate(x_test, [y_test,y_test,y_test], verbose=1)
print('Train loss:',score[0])
print('Train accuracy:',score[1])

# Show accuracy curves    
plt.figure()
plt.grid()                                              
                                                            
plt.title('Training performance')                          
plt.plot(history.epoch, history.history['loss'], label='train loss+error')  
plt.plot(history.epoch, label='val_error')   
plt.legend()

"""Here the implementations of all 3 figures in paper"""

#Here are the implementation of the 3 figures separately 


### FIGURE 5 MODEL
input_img = Input(shape=(32, 32, 3))
print(input_img.shape)

## layer 0
layer_0 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img)
layer1 = Conv2D(8, (3,3), padding='same', activation='relu')(layer_0)
layer2 = Conv2D(8, (3,3), padding='same', activation='relu')(layer1)

### 1st layer
layer3 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img)
layer4 = Conv2D(8, (3,3), padding='same', activation='relu')(layer3)
### 2nd layer
layer5 = MaxPooling2D((3,3), strides=(1,1), padding='same')(input_img)
layer6 = Conv2D(8, (1,1), padding='same', activation='relu')(layer5)
####
layer7 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img)

mid_1 = keras.layers.concatenate([layer2, layer4, layer6, layer7])
print(mid_1.shape)

flat_1 = Flatten()(mid_1)
print(flat_1)
dense_1 = Dense(1200, activation='relu')(flat_1)
dense_1 = Dropout(0.5)(dense_1)
print(dense_1.shape)
dense_2 = Dense(600, activation='relu')(dense_1)
dense_2 = Dropout(0.5)(dense_2)
print(dense_2.shape)
dense_3 = Dense(150, activation='relu')(dense_2)
print(dense_3.shape)

output5 = Dense(10, activation='softmax')(dense_3)
#print(output.shape)

model5 = Model([input_img], output5)
#####FIGURE 6 MODEL

input_img = Input(shape=(32, 32, 3))
print(input_img.shape)

## layer 0
layer0 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img)
layer1 = Conv2D(8, (1,7), padding='same', activation='relu')(layer0)
layer2 = Conv2D(8, (7,1), padding='same', activation='relu')(layer1)
layer3 = Conv2D(8, (1,7), padding='same', activation='relu')(layer2)
layer4 = Conv2D(8, (7,1), padding='same', activation='relu')(layer3)

### 1st layer
layer5 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img)
layer6 = Conv2D(8, (1,7), padding='same', activation='relu')(layer5)
layer7 = Conv2D(8, (7,1), padding='same', activation='relu')(layer6)

### 2nd layer
layer8 = MaxPooling2D((3,3), strides=(1,1), padding='same')(input_img)
layer9 = Conv2D(8, (1,1), padding='same', activation='relu')(layer8)

### 3rd layer
layer10 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img)

### Concatenate
mid_1 = keras.layers.concatenate([layer4, layer7, layer9, layer10])
print(mid_1.shape)

flat_1 = Flatten()(mid_1)
print(flat_1)
dense_1 = Dense(1200, activation='relu')(flat_1)
dense_1 = Dropout(0.5)(dense_1)
print(dense_1.shape)
dense_2 = Dense(600, activation='relu')(dense_1)
dense_2 = Dropout(0.5)(dense_2)
print(dense_2.shape)
dense_3 = Dense(150, activation='relu')(dense_2)
print(dense_3.shape)

output6 = Dense(10, activation='softmax')(dense_3)
#print(output.shape)

model6 = Model([input_img], output6)

#FIGURE 7 MODEL
input_img = Input(shape=(32, 32, 3))
print(input_img.shape)

## layer 0
layer_0 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img)

layer1 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img)

### 1st layer
layer_1 = Conv2D(8, (1,3), padding='same', activation='relu')(layer1)

### 2nd layer
layer_2 = Conv2D(8, (3,1), padding='same', activation='relu')(layer1)

layer2 = Conv2D(8, (1,1), padding='same', activation='relu')(input_img)
layer3 = Conv2D(8, (3,3), padding='same', activation='relu')(layer2)

### 3rd layer
layer_3 = Conv2D(8, (1,3), padding='same', activation='relu')(layer3)

### 4th layer
layer_4 = Conv2D(8, (3,1), padding='same', activation='relu')(layer3)

### 5th layer
layer5 = MaxPooling2D((3,3), strides=(1,1), padding='same')(input_img)
layer_5 = Conv2D(8, (1,1), padding='same', activation='relu')(layer5)

### Concatenate
mid_1 = keras.layers.concatenate([layer_0, layer_1, layer_2, layer_3, layer_4, layer_5])
print(mid_1.shape)

flat_1 = Flatten()(mid_1)
print(flat_1)
dense_1 = Dense(1200, activation='relu')(flat_1)
dense_1 = Dropout(0.5)(dense_1)
print(dense_1.shape)
dense_2 = Dense(600, activation='relu')(dense_1)
dense_2 = Dropout(0.5)(dense_2)
print(dense_2.shape)
dense_3 = Dense(150, activation='relu')(dense_2)
print(dense_3.shape)

output7 = Dense(10, activation='softmax')(dense_3)
#print(output.shape)

model7 = Model([input_img], output7)

"""Epoch 1/10
50000/50000 [==============================] - 60s 1ms/step - loss: 2.2902 - acc: 0.3441
Epoch 2/10
50000/50000 [==============================] - 57s 1ms/step - loss: 1.4176 - acc: 0.4864
Epoch 3/10
50000/50000 [==============================] - 58s 1ms/step - loss: 1.2345 - acc: 0.5550
Epoch 4/10
50000/50000 [==============================] - 57s 1ms/step - loss: 1.0793 - acc: 0.6135
Epoch 5/10
50000/50000 [==============================] - 58s 1ms/step - loss: 0.9333 - acc: 0.6663
Epoch 6/10
50000/50000 [==============================] - 58s 1ms/step - loss: 0.7905 - acc: 0.7187
Epoch 7/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.6663 - acc: 0.7638
Epoch 8/10
50000/50000 [==============================] - 58s 1ms/step - loss: 0.5410 - acc: 0.8091
Epoch 9/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.4504 - acc: 0.8419
Epoch 10/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.3674 - acc: 0.8712

10000/10000 [==============================] - 2s 199us/step
0.6488000005483627
Model: "model_3"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_3 (InputLayer)            (None, 32, 32, 3)    0                                            
__________________________________________________________________________________________________
conv2d_23 (Conv2D)              (None, 32, 32, 8)    32          input_3[0][0]                    
__________________________________________________________________________________________________
conv2d_20 (Conv2D)              (None, 32, 32, 8)    32          input_3[0][0]                    
__________________________________________________________________________________________________
conv2d_24 (Conv2D)              (None, 32, 32, 8)    584         conv2d_23[0][0]                  
__________________________________________________________________________________________________
max_pooling2d_3 (MaxPooling2D)  (None, 32, 32, 3)    0           input_3[0][0]                    
__________________________________________________________________________________________________
conv2d_19 (Conv2D)              (None, 32, 32, 8)    32          input_3[0][0]                    
__________________________________________________________________________________________________
conv2d_21 (Conv2D)              (None, 32, 32, 8)    200         conv2d_20[0][0]                  
__________________________________________________________________________________________________
conv2d_22 (Conv2D)              (None, 32, 32, 8)    200         conv2d_20[0][0]                  
__________________________________________________________________________________________________
conv2d_25 (Conv2D)              (None, 32, 32, 8)    200         conv2d_24[0][0]                  
__________________________________________________________________________________________________
conv2d_26 (Conv2D)              (None, 32, 32, 8)    200         conv2d_24[0][0]                  
__________________________________________________________________________________________________
conv2d_27 (Conv2D)              (None, 32, 32, 8)    32          max_pooling2d_3[0][0]            
__________________________________________________________________________________________________
concatenate_3 (Concatenate)     (None, 32, 32, 48)   0           conv2d_19[0][0]                  
                                                                 conv2d_21[0][0]                  
                                                                 conv2d_22[0][0]                  
                                                                 conv2d_25[0][0]                  
                                                                 conv2d_26[0][0]                  
                                                                 conv2d_27[0][0]                  
__________________________________________________________________________________________________
flatten_3 (Flatten)             (None, 49152)        0           concatenate_3[0][0]              
__________________________________________________________________________________________________
dense_9 (Dense)                 (None, 1200)         58983600    flatten_3[0][0]                  
__________________________________________________________________________________________________
dropout_5 (Dropout)             (None, 1200)         0           dense_9[0][0]                    
__________________________________________________________________________________________________
dense_10 (Dense)                (None, 600)          720600      dropout_5[0][0]                  
__________________________________________________________________________________________________
dense_11 (Dense)                (None, 150)          90150       dense_10[0][0]                   
__________________________________________________________________________________________________
dense_12 (Dense)                (None, 10)           1510        dense_11[0][0]                   
==================================================================================================
Total params: 59,797,372
Trainable params: 59,797,372
Non-trainable params: 0

50000/50000 [==============================] - 65s 1ms/step - loss: 2.1029 - acc: 0.3173
Epoch 2/10
50000/50000 [==============================] - 57s 1ms/step - loss: 1.4739 - acc: 0.4675
Epoch 3/10
50000/50000 [==============================] - 57s 1ms/step - loss: 1.2524 - acc: 0.5530
Epoch 4/10
50000/50000 [==============================] - 57s 1ms/step - loss: 1.0860 - acc: 0.6155
Epoch 5/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.9425 - acc: 0.6678
Epoch 6/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.8104 - acc: 0.7141
Epoch 7/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.6994 - acc: 0.7523
Epoch 8/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.6010 - acc: 0.7882
Epoch 9/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.5267 - acc: 0.8156
Epoch 10/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.4643 - acc: 0.8371

10000/10000 [==============================] - 2s 186us/step
0.6577999997138977
Model: "model_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            (None, 32, 32, 3)    0                                            
__________________________________________________________________________________________________
conv2d_5 (Conv2D)               (None, 32, 32, 8)    32          input_1[0][0]                    
__________________________________________________________________________________________________
conv2d_2 (Conv2D)               (None, 32, 32, 8)    32          input_1[0][0]                    
__________________________________________________________________________________________________
conv2d_6 (Conv2D)               (None, 32, 32, 8)    584         conv2d_5[0][0]                   
__________________________________________________________________________________________________
max_pooling2d_1 (MaxPooling2D)  (None, 32, 32, 3)    0           input_1[0][0]                    
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 32, 32, 8)    32          input_1[0][0]                    
__________________________________________________________________________________________________
conv2d_3 (Conv2D)               (None, 32, 32, 8)    200         conv2d_2[0][0]                   
__________________________________________________________________________________________________
conv2d_4 (Conv2D)               (None, 32, 32, 8)    200         conv2d_2[0][0]                   
__________________________________________________________________________________________________
conv2d_7 (Conv2D)               (None, 32, 32, 8)    200         conv2d_6[0][0]                   
__________________________________________________________________________________________________
conv2d_8 (Conv2D)               (None, 32, 32, 8)    200         conv2d_6[0][0]                   
__________________________________________________________________________________________________
conv2d_9 (Conv2D)               (None, 32, 32, 8)    32          max_pooling2d_1[0][0]            
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 32, 32, 48)   0           conv2d_1[0][0]                   
                                                                 conv2d_3[0][0]                   
                                                                 conv2d_4[0][0]                   
                                                                 conv2d_7[0][0]                   
                                                                 conv2d_8[0][0]                   
                                                                 conv2d_9[0][0]                   
__________________________________________________________________________________________________
flatten_1 (Flatten)             (None, 49152)        0           concatenate_1[0][0]              
__________________________________________________________________________________________________
dense_1 (Dense)                 (None, 1200)         58983600    flatten_1[0][0]                  
__________________________________________________________________________________________________
dropout_1 (Dropout)             (None, 1200)         0           dense_1[0][0]                    
__________________________________________________________________________________________________
dense_2 (Dense)                 (None, 600)          720600      dropout_1[0][0]                  
__________________________________________________________________________________________________
dropout_2 (Dropout)             (None, 600)          0           dense_2[0][0]                    
__________________________________________________________________________________________________
dense_3 (Dense)                 (None, 150)          90150       dropout_2[0][0]                  
__________________________________________________________________________________________________
dense_4 (Dense)                 (None, 10)           1510        dense_3[0][0]                    
==================================================================================================
Total params: 59,797,372
Trainable params: 59,797,372
Non-trainable params: 0
# __________________________________________________________________________________________________

Epoch 1/7
50000/50000 [==============================] - 59s 1ms/step - loss: 5.5038 - acc: 0.3400
Epoch 2/7
50000/50000 [==============================] - 57s 1ms/step - loss: 1.1891 - acc: 0.5737
Epoch 3/7
50000/50000 [==============================] - 57s 1ms/step - loss: 0.9268 - acc: 0.6724
Epoch 4/7
50000/50000 [==============================] - 57s 1ms/step - loss: 0.6892 - acc: 0.7567
Epoch 5/7
50000/50000 [==============================] - 57s 1ms/step - loss: 0.4671 - acc: 0.8358
Epoch 6/7
50000/50000 [==============================] - 57s 1ms/step - loss: 0.2840 - acc: 0.9012
Epoch 7/7
50000/50000 [==============================] - 57s 1ms/step - loss: 0.1801 - acc: 0.9377

Time: 401s

Epoch 1/10
50000/50000 [==============================] - 59s 1ms/step - loss: 5.9663 - acc: 0.3155
Epoch 2/10
50000/50000 [==============================] - 57s 1ms/step - loss: 1.2368 - acc: 0.5598
Epoch 3/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.9835 - acc: 0.6515
Epoch 4/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.7412 - acc: 0.7405
Epoch 5/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.4597 - acc: 0.8411
Epoch 6/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.2380 - acc: 0.9194
Epoch 7/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.1295 - acc: 0.9564
Epoch 8/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.0880 - acc: 0.9710
Epoch 9/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.0730 - acc: 0.9765
Epoch 10/10
50000/50000 [==============================] - 57s 1ms/step - loss: 0.0665 - acc: 0.9785


Time: 572s
"""