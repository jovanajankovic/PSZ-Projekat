import pandas as pd
import matplotlib.pyplot as plt
from numpy import asarray
import tkinter as tk
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

# reading data from csv file
dataset = pd.read_csv('cars.csv')

# define the bin edges and labels
bins = [0, 1999, 4999, 9999, 14999, 19999, 24999, 29999, float('inf')]
labels = [1, 2, 3, 4, 5, 6, 7, 8]

# create a new column with the segment labels
dataset['opseg_cena'] = pd.cut(dataset['cena'], bins=bins, labels=labels, include_lowest=True)

# for searching the best hyperparameters GridSearchCV
'''param_grid = {
    'n_neighbors': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    'weights': ['uniform', 'distance'],
    'p': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
} '''

# attributes that are relevant for model training
chosen_attributes = ['marka', 'model', 'godiste', 'kilometraza', 'kubikaza', 'motor']

# chosen columns for encoding and data encoding
encoding_columns = ['marka', 'model']
encoder = OrdinalEncoder()
dataset[encoding_columns] = encoder.fit_transform(dataset[encoding_columns])

x = dataset[['stanje', 'marka', 'model', 'godiste', 'kilometraza', 'karoserija', 'gorivo', 'kubikaza', 'motor', 'menjac', 'broj_vrata', 'broj_sedista', 'klima', 'boja', 'ostecenje', 'lokacija']]
y = dataset['opseg_cena']

# for a machine learning algorithm that requires numpy arrays as input.
dataX = asarray(x[['stanje', 'marka', 'model', 'godiste', 'kilometraza', 'karoserija', 'gorivo', 'kubikaza', 'motor', 'menjac', 'broj_vrata', 'broj_sedista', 'klima', 'boja', 'ostecenje', 'lokacija']])

'''from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(x, y)
print('najvaznije osobina',model.feature_importances_) '''

# most valuable attributes based on model.feature_importances_
dataX = asarray(x[['marka', 'model', 'godiste', 'kilometraza', 'kubikaza', 'motor']])

# data scaling
scaler = StandardScaler()
x = scaler.fit_transform(dataX)

# splitting data into traing and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2)


# from sklearn.model_selection import GridSearchCV
# grid_search = GridSearchCV(model, param_grid, cv=5)

# fit the GridSearchCV object to the training data
#grid_search.fit(x_train, y_train)

# use the best estimator to predict on the test data
# y_pred = grid_search.best_estimator_.predict(x_test)

# get the best hyperparameters
# best_params = grid_search.best_params_
# print('Best hyperparameters:', best_params)

# for this model, these hyperparameters gave the best results
# model training
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 10, weights = 'distance', p = 1)
model.fit(x_train, y_train)
y_prediction = model.predict(x_test)

# displaying confusion matrix
confusion_matrix = confusion_matrix(y_test, y_prediction)
confusion_matrix_display = ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)
confusion_matrix_display.plot()
plt.show()

# average = 'micro' when there is a class imbalance
# micro-averaging gives more weight to the performance of the classes with more samples, 
# which is useful in scenarios where we want to prioritize the correct classification of the most frequent classes.
# While precision only considers the positive predictions made by the model,
# F1 score considers both positive and negative predictions. 
# In general, F1 score is a better choice than precision when we have imbalanced classes, 
# that is, when one class is much larger than the other, because F1 score takes into account both precision and recall.
f1_score = f1_score(y_test, y_prediction, average = 'micro')
print('F1 score:', f1_score)
precision = metrics.accuracy_score(y_test, y_prediction)
print('Precision:', precision)

def calculate_real_price(range):
    price_ranges = {
        1: '< 2000e',
        2: '2000-4999e',
        3: '5000-9999e',
        4: '10000-14999e',
        5: '15000-19999e',
        6: '20000-24999e',
        7: '25000-29999e'
    }
    return price_ranges.get(int(range), '> 30000e')
   
def submit_form():
    form_data = []
    marka = marka_entry.get()
    carmodel = model_entry.get()
    godiste = godiste_entry.get()
    kilometraza = kilometraza_entry.get()
    kubikaza = kubikaza_entry.get()
    motor = motor_entry.get()
    
    print(f"\nMarka: {marka}\nModel: {carmodel}")
    print(f"Godiste: {godiste}\nKilometraza: {kilometraza}")
    print(f"Kubikaza: {kubikaza}\nMotor: {motor}")

    form_data.append(marka)
    form_data.append(carmodel)
    form_data.append(godiste)
    form_data.append(kilometraza)
    form_data.append(kubikaza)
    form_data.append(motor)
    
    # creating new car object with data from the form
    car = dict(zip(chosen_attributes, form_data))
    car = pd.DataFrame([car])
    
    # casting necessary data into int
    car['godiste'] = int(car['godiste'])
    car['kilometraza'] = int(car['kilometraza']) 
    car['kubikaza'] = int(car['kubikaza'])
    car['motor'] = int(car['motor'])  

    # encoding necessary data 
    car[encoding_columns] = encoder.transform(car[encoding_columns])

    #data scaling
    car_scaled = scaler.transform(car[chosen_attributes])

    # new price prediction for the car from the form
    car_price_range_prediction = model.predict(car_scaled)
    print('Cena automobila se krece izmedju ', calculate_real_price(car_price_range_prediction))

# create main window
root = tk.Tk()
root.title('Forma za unos automobila')
heading_label = tk.Label(root, text="Forma za unos informacija o automobilu", font=("Arial", 16))
heading_label.grid(row=0, column=0, columnspan=2, padx = 10, pady=10)

# create form labels
marka_label = tk.Label(root, text="marka:", font=("Arial", 14))
model_label = tk.Label(root, text="model:", font=("Arial", 14))
godiste_label = tk.Label(root, text="godiste:", font=("Arial", 14))
kilometraza_label = tk.Label(root, text="kilometraza:", font=("Arial", 14))
kubikaza_label = tk.Label(root, text="kubikaza:", font=("Arial", 14))
motor_label = tk.Label(root, text="motor:", font=("Arial", 14))

# create form entries
marka_entry = tk.Entry(root, font=("Arial", 14))
model_entry = tk.Entry(root, font=("Arial", 14))
godiste_entry = tk.Entry(root, font=("Arial", 14))
kilometraza_entry = tk.Entry(root, font=("Arial", 14))
kubikaza_entry = tk.Entry(root, font=("Arial", 14))
motor_entry = tk.Entry(root, font=("Arial", 14))

# position labels and entries in the form
marka_label.grid(row=1, column=0, padx=10, pady=10)
marka_entry.grid(row=1, column=1, padx=10, pady=10)
model_label.grid(row=2, column=0, padx=10, pady=10)
model_entry.grid(row=2, column=1, padx=10, pady=10)
godiste_label.grid(row=3, column=0, padx=10, pady=10)
godiste_entry.grid(row=3, column=1, padx=10, pady=10)
kilometraza_label.grid(row=4, column=0, padx=10, pady=10)
kilometraza_entry.grid(row=4, column=1, padx=10, pady=10)
kubikaza_label.grid(row=5, column=0, padx=10, pady=10)
kubikaza_entry.grid(row=5, column=1, padx=10, pady=10)
motor_label.grid(row=6, column=0, padx=10, pady=10)
motor_entry.grid(row=6, column=1, padx=10, pady=10)

# create submit button
submit_button = tk.Button(root, text="Proceni cenu automobila", command=submit_form, width=20, bg="green", fg="white", font=("Arial", 14))
submit_button.grid(row=7, column=0, columnspan= 2, padx=10, pady=10, sticky="nsew")

# start the main loop
root.mainloop()

