import pandas as pd
from lxml import etree
import xml.etree.ElementTree as et

def informacion_a_xml(fichero,dataframe, guardar):
    
    root=et.Element('TITULO')
    columnas= dataframe.columns.values
    fichero = et.SubElement(root, 'fichero', {fichero: 'nombre'})
    
    for j in range(len(columnas)):
        
        columna=et.SubElement(fichero,'columna',{'nombre_columna':columnas[j]})
        
        et.SubElement(columna,'NaN_columna',{'numero_NaN_columna':str(df[columnas[j]].isna().sum())}) #nans
        et.SubElement(columna,'Null_columna',{'numero_Null_columna':str(df[columnas[j]].isnull().sum())}) #nulls
        et.SubElement(columna,'tipo_dato',{'tipo_dato_columna':str(df[columnas[j]].dtype)}) #categoria de columns (df.types)
        
    tree = et.ElementTree(root)
    #identacion de python 
    et.indent(tree)
    tree.write(guardar, xml_declaration=True, encoding='utf-8')

if __name__ == '__main__':
    
    ficheros = ['order_details_2016.csv','orders_2016.csv','pizza_types.csv','pizzas.csv']
    for i in range(0,len(ficheros)):
            print('limpieza de ficheros')
            print(ficheros[i])
            if i == 0 or 2:
                df= pd.read_csv(ficheros[i],sep=";", encoding='LATIN-1')
            else:
                df= pd.read_csv(ficheros[i],sep=",", encoding='LATIN-1')
            print('\nNúmero de Nan por columna:')
            print(df.isna().sum())
            print('\nNúmero de nulls por columna:')
            print(df.isnull().sum())
            print("Los tipos de datos en las columnas son: ")
            print(df.dtypes)
            if i==0:
                guardar='analisis_xml_orderdetails.xml'
            elif i ==1:
                guardar='analisis_xml_orders.xml'
            elif i==2: 
                guardar='analisis_xml_pizzatypes.xml'
            else:
                guardar='analisis_xml_pizza.xml'
            informacion_a_xml(ficheros[i],df,guardar)

  