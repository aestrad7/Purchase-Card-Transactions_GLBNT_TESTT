import sys
import pandas as pd
import numpy as np
import glob

sys.path.append('/home/grupodot/Documentos/Examen_globant/Purchase-Card-Transactions_GLBNT_TESTT/Data/')

class Explorer():
    """Esta clase compila las funciones de importacion y exploracion usadas en el ejercicio.
    (salvo algunas funciones triviales o de menor modularidad)
    """

    def __init__(self):
        """Initialize the class and generate the characteristic self.df as an instance. 
        """       

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