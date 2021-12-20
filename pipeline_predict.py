import joblib
import config2 as cfg
import pandas as pd
import numpy as np

#Cargamos modelo y pipeline
salescustomer_model = joblib.load('salescustomer_pipeline.pkl')
print('Funciona bien el pipeline')

#Funcion para hacer predicciones.
def predict(X):
    predicts = salescustomer_model.predict(X)
    salida = np.exp(predicts)
    print(salida)
    return salida[0]


#predict(X_test)