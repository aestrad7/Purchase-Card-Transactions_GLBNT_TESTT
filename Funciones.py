import sys
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

from sklearn.preprocessing import OrdinalEncoder

sys.path.append('/home/grupodot/Documentos/Examen_globant/Purchase-Card-Transactions_GLBNT_TESTT/Data/')

class Explorer():
    """Esta clase compila las funciones de importación y exploración usadas en el ejercicio.
    (salvo algunas funciones triviales o de menor modularidad)
    """

    def __init__(self):
        """Initialize the class and generate the characteristic self.df as an instance. 
        """       
        self.ord_enc = OrdinalEncoder()

    def importar_d(self, data_dir):
        """Esta función importa todos los documentos usados durante el ejercicio

        Args:
            data_dir (string): constante que se define al inicio del ejercicio con una dirección especifica del path

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
        """Función de limpieza de nan y variable temporal.

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
        """Remplaza los NaN por la string "valor_remplazo"

        Args:
            data_dir (string): string con la direccion en el path para todo el conjunto de datos
            valor_remplazo (str, optional): Valor con el que seran remplazados los NaN. Defaults to "noreg".

        Returns:
            DataFrame: Pandas DataFrame
        """     
        df = self.importar_d(data_dir)
        df_f = self.limpieza(df,valor_remplazo)

        return df_f
    
    def graficador(self, df_var, size = (12,6), tipo ="plot", tittle =""):
        """Función para gráficas unitarias de pyplot

        Args:
            df_var (DataFrame de dimension 1 o array): En esta función se requiere que se decrete de una vez el nombre de la variable del DataFrame, ej: df["variable1"]
            tipo (str, optional): [description]. Defaults to "plot".
            tittle (str, optional): [description]. Defaults to "".
            size (tuple, optional): [description]. Defaults to (12,16).
        """        

        plt.figure(figsize=size)
        
        if tipo == "plot":
            plt.plot(df_var)

        elif tipo =="hist":
            plt.hist(df_var)
        
        plt.title(tittle)
        plt.grid()
        plt.show()

    def comparador (self, variable, df1, df2, df3):
        """Esta función me permite visualizar gráficamente la distribución la misma variable en tres DataFrames diferentes.
        Es obligatorio que os DataFrame tengan el mismo nombre en las variables.

        Args:
            variable (string): Es el nombre de la columna del DataFram a comparar
            df1 (DataFrame): DataFrame
            df2 (DataFrame): DataFrame
            df3 (DataFrame): DataFrame
        """        

        mnd1 = min(df1[variable])
        mxd1 = max(df1[variable])
        mnd2 = min(df2[variable])
        mxd2 = max(df2[variable])
        mnd3 = min(df3[variable])
        mxd3 = max(df3[variable])
        
        minimo=min(mnd1, mnd2, mnd3)
        maximo= max(mxd1, mxd2, mxd3)
        
        plt.style.use('bmh')
        plt.hist(df1[variable], histtype="stepfilled", bins=15, alpha=0.8, density=True, range=(minimo-1, maximo+1), label=0)
        plt.hist(df2[variable], histtype="stepfilled", bins=15, alpha=0.8, density=True, range=(minimo-1, maximo+1), label=1)
        plt.hist(df3[variable], histtype="stepfilled", bins=15, alpha=0.8, density=True, range=(minimo-1, maximo+1), label=2)
        plt.legend()
        plt.title(variable)
        plt.show()

    # def estandarizador(self,):

    # def subgraficador(self,):
    # def KMeans_function(self,):
    # def PCA_function(self,):



