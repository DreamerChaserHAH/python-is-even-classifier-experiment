import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

data = pd.read_csv('dataset.csv')
val_data = pd.read_csv('testset.csv')

def change_value(x):
    new_value = abs(x) if x % 2 == 0 else -abs(x)
    return new_value

X_train_second = data['number'].astype('long').apply(change_value)
X_train = data.drop('value', axis=1)
X_train['second'] = X_train_second
Y_train = data['value'].astype('category').cat.codes

X_val_second = val_data['number'].astype('long').apply(change_value)
X_val = val_data.drop('value', axis=1)
X_val['second'] = X_val_second
Y_val = val_data['value'].astype('category').cat.codes

print(X_train.head())
print(f'Status: Data Loaded ${X_train.shape[1]} features')

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

print('Status: Model Building Completed')

model.compile(optimizer='adam',
              loss='binary_crossentropy',  # Use binary crossentropy for binary classification
              metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=5, batch_size=32, validation_data=(X_val, Y_val))

loss, accuracy = model.evaluate(X_val, Y_val, verbose=2)
print(f'Evaluation loss: {loss}, accuracy: {accuracy}')

model.save('model.keras')
print('Status: Model Saved')