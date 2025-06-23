import os
import numpy as np
import pandas as pd
from zipfile import ZipFile
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')


class ArbolDecision:

    dataset = ''
    modelo = ''
    precicion = ''

    def __init__(self):
        self.llenarDataset()
        self.traducirValores()
        self.entrenarModelo()
    
    def llenarDataset(self):
        for dir,_,files in os.walk(os.getcwd()):
            if dir.endswith('modelo'):
                with ZipFile(
                    os.path.join(dir,files[files.index('archive.zip')]),
                    'r'
                ) as datos:
                    self.dataset = pd.DataFrame(
                        pd.read_csv(
                            datos.open(
                                datos.namelist()[0]
                            )
                        ))

    def traducirValores(self):
        #Traducir columnas
        columnas = [
            'Nitrogeno',
            'Fosforo',
            'Potacio',
            'Temperatura',
            'Humedad',
            'ph',
            'Lluvia',
            'Etiqueta'
        ]
        self.dataset.columns = columnas

        #Traducir nombre de frutas y verduras
        self.dataset['Etiqueta'] = self.dataset['Etiqueta'].map({
            'rice':'arroz',
            'maize':'maiz',
            'chickpea':'garbanzo',
            'kidneybeans':'frijoles',
            'pigeonpeas':'arvejas',
            'mothbeans':'frijol de polilla',
            'mungbean':'frijol de mungo',
            'blackgram':'frijol negro',
            'lentil':'lentejas',
            'pomegranate':'granada',
            'banana':'banana',
            'mango':'mango',
            'grapes':'uva',
            'watermelon':'sandia',
            'muskmelon':'melon',
            'apple':'manzana',
            'orange':'naranja',
            'papaya':'papaya',
            'coconut':'coco',
            'cotton':'algodon',
            'jute':'jute',
            'coffee':'cafe'
        })

    def entrenarModelo(self):

        self.modelo = RandomForestClassifier(
            n_estimators=200,
            max_depth=None,
            random_state=42)

        X = self.dataset.drop(['Etiqueta'],axis=1)
        y = self.dataset['Etiqueta']

        X_train,X_test,y_train,y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.modelo.fit(X_train,y_train)
        y_pred = self.modelo.predict(X_test)
        
        self.precicion_modelo(y_test,y_pred)


    def precicion_modelo(self,y_test,y_pred):
        self.precicion = round(
            accuracy_score(
                y_test,y_pred
            ) * 100,2
        )

    def nAlternativas(self,datosSuelo,n):
        prob = self.modelo.predict_proba(datosSuelo)[0]
        nRes = np.argsort(prob)[::-1][:n]
        lista = list(zip(
                [i.upper() for i in self.modelo.classes_[nRes]],
                [round(i*100,2) for i in prob[nRes]]
        ))

        return lista
    
    def getPrecision(self):
        return self.precicion