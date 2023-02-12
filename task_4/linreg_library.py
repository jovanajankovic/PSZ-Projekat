import pandas as pd
from numpy import asarray
import tkinter as tk
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import linear_model
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# reading data from csv file
dataset = pd.read_csv('cars.csv')
# relevant attributes for model training
chosen_attributes = ['marka', 'model', 'godiste', 'kilometraza', 'kubikaza', 'motor']
# attributes for encoding
encoding_columns = ['marka', 'model']

# endocing marka and model attribute since they are type of string
encoder = OrdinalEncoder()
dataset[encoding_columns] = encoder.fit_transform(dataset[encoding_columns])

# fetching data
x = dataset[['marka', 'model', 'godiste', 'kilometraza', 'kubikaza', 'motor']]
y = dataset['cena']
dataX = asarray(x[['marka', 'model', 'godiste', 'kilometraza', 'kubikaza', 'motor']])

#data scaling
scaler = StandardScaler()
x = scaler.fit_transform(dataX)

# spliting data into train and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# model = LinearRegression()
# Overall, this can result in a more accurate and
# robust model than using a simple linear regression 
# without polynomial features or regularization.
# 700 gave the best results
model = make_pipeline(PolynomialFeatures(2), linear_model.Ridge(alpha=700))

# dajemo mu podatke iz x_train i y_train seta da nauci
model.fit(x_train, y_train)

# cisto da vidimo kakve on izlaze dobija, da bismo mogli da ih uporedimo sa y_test
predictions = model.predict(x_test) 

# na test da je jako mali koeficijent determinacije, koliki procenat je upao na testu, a ovde je malo jer imamo jako malo podataka
# koliki procenat tacaka je upao na pravu
print('Coefficient of determination training set', model.score(x_train, y_train))
print('Coefficient of determination test set', model.score(x_test, y_test))

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

    # casting data from the form to type int 
    car['godiste'] = int(car['godiste'])
    car['kilometraza'] = int(car['kilometraza']) 
    car['kubikaza'] = int(car['kubikaza'])
    car['motor'] = int(car['motor'])  

    # encoding necessary data
    car[encoding_columns] = encoder.transform(car[encoding_columns])

    # data scaling 
    car_scaled = scaler.transform(car[chosen_attributes])
    car_price_prediction = model.predict(car_scaled)
    print('Cena automobila je ', car_price_prediction)

# create main window
root = tk.Tk()
root.title('Forma')
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
