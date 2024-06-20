import tensorflow as tf
import pandas as pd
import numpy as np

def change_value(x):
    new_value = abs(x) if x % 2 == 0 else -abs(x)
    return new_value

model = tf.keras.models.load_model('model.keras')

X = list(range(-20, 20))
df = pd.DataFrame(X, columns=['number'])

second = df['number'].astype('long').apply(change_value)
df['second'] = second

prediction = np.round(model.predict(df))
print('Prediction: ', prediction)