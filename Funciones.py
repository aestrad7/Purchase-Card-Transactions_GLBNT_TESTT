import sys
import pandas as pd
import numpy as np
import glob

from sklearn.preprocessing import OrdinalEncoder

sys.path.append('/home/grupodot/Documentos/Examen_globant/Purchase-Card-Transactions_GLBNT_TESTT/Data/')

class Explorer():
    """Esta clase compila las funciones de importacion y exploracion usadas en el ejercicio.
    (salvo algunas funciones triviales o de menor modularidad)
    """

    def __init__(self):
        """Initialize the class and generate the characteristic self.df as an instance. 
        """       
        self.ord_enc = OrdinalEncoder()

    def importar_d(self, data_dir):
        """Esta funcion importa todos los documentos usados durante el ejercicio

        Args:
            data_dir (string): constante que se define al inicio del ejercicio con una direccion especifica del path

        Returns:
            Pandas.DataFrame
        """        
        unidos = []
    
        for d in glob.glob(data_dir + "*.xls"):
            df = pd.read_excel(d)
            unidos.append(df)
        
        df = pd.concat(unidos, ignore_index="True")
        
        return df
    
    def limpieza(self, df, valor_remplazo):
        """Funcion de limpieza de nan y variable temporal.

        Args:
            df (Pandas.DataFrame): DataFrame
            valor_remplazo ([type]): Valor con el que se quiere remplazar los nan, por defecto viene con el valor "noreg" que hace referencia a "no registro"
        """        
        to_numeric = (df.select_dtypes(include=["object"]).copy()).columns
        df_f = df.fillna(valor_remplazo)
        df_f[to_numeric] = self.ord_enc.fit_transform(df_f[to_numeric])
        df_f = df_f.drop(["TRANS DATE"], axis = 1)

        return df_f
    
    def clean_import(self, data_dir, valor_remplazo="noreg"):
        df = self.importar_d(data_dir)
        df_f = self.limpieza(df,valor_remplazo)

        return df_f
    
    # def estandarizador(self,):

    # def graficador(self,):
    # def subgraficador(self,):
    # def KMeans_function(self,):
    # def PCA_function(self,):



