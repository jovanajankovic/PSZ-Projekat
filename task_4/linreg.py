import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas as pd
import matplotlib.pyplot as plt
from numpy import asarray
import numpy as np

marke, encoded_marke = [], []
#saving the max value that appeared in the dataset for each attribute
attributes_max_values = [0] * 6
trainset, testset = [], []

dataset = pd.read_csv('cars.csv')
# x = dataset[['marka', 'model', 'godiste', 'kilometraza', 'kubikaza', 'motor']]
# y = dataset['cena']
# dataX = asarray(x[['marka', 'model', 'godiste', 'kilometraza', 'kubikaza', 'motor']])
# dataY = asarray(y)
data = asarray(dataset[['marka', 'godiste', 'kilometraza', 'kubikaza', 'motor', 'cena']])
marke = list(set(dataset['marka']))

#print('data', data)
#print('Marke', marke)

encoded_marke = [i for i in range(len(marke))]

#print('Marke vrednosti', encoded_marke)
#print('Velicina dataseta', len(data))
#print('data pre enkodovanja', data)

for i in range(len(data)):
    for j in range(len(marke)):
        if data[i][0] == marke[j]:
            data[i][0] = encoded_marke[j]
            break

#print('data posle enkodovanja', data)

# ovaj deo je za skaliranje vrednosti, pronalazi max vrednost iz celog niza i deli
attributes_max_values = np.max(data, axis=0)

# Scale the data by dividing each column by its maximum value
data = data / attributes_max_values

#print('data posle skaliranja', data)
#print('max values', attributes_max_values)

# saving maximum price, so that it can be used in the end for returning to the real value
max_price_value = attributes_max_values[5]
# Set the index of the price value to 5
price_value_index = 5

random.shuffle(data)
trainset = data[:round(0.8*len(data))]
testset = data[round(0.8*len(data)):]

# temporary weight vector to all 0s
w_temp = [0, 0, 0, 0, 0, 0]
# weight vector [w0, w1, w2, w3, w4, w5, w6]
w = [1, 0.2, 0.4, 0.5, 0.6, 0.3]

#learning rate 0.1 or 0.01
alpha = 0.01

def h(x):
    return w[0] + sum([w[i]*x[i-1] for i in range(1, len(w))])

def gradient_descent(dataset):
    derivatives  = []
    # for each w in weight vector
    for i in range(len(w)):
        derivative_weight_sum  = 0
        # for each row in dataset
        for j in range(len(dataset)):
            predicted_price = h(dataset[i])
            actual_price = dataset[j][price_value_index]
            subtraction = (predicted_price - actual_price)
            # additional x data 
            if i != 0:
                subtraction*=dataset[j][i-1]
            
            derivative_weight_sum +=subtraction
        
        derivative_weight_sum  = derivative_weight_sum /len(dataset)
        w_temp[i] = w[i] - alpha*derivative_weight_sum 
        derivatives.append(derivative_weight_sum)
    
    for i in range(len(w)):
        w[i] = w_temp[i]

    return derivatives
    
def train_model(dataset):
    i = 0
    derivatives = [1] * 6
    while any(abs(d) > 0.0000005 for d in derivatives):
        derivatives = gradient_descent(dataset)
        i += 1
        print(f'Iteration {i}: derivatives = {derivatives}')
    return
    
train_model(trainset)

predictions = [h(testset[i]) * max_price_value for i in range(len(testset))]
actual_values = [testset[i][5] * max_price_value for i in range(len(testset))]

for pred, true in zip(predictions[:5000], actual_values[:5000]):
    print(f"Predictions: {pred} / Actutual values: {true}")

plt.plot(actual_values, predictions, color='blue')
plt.show()
