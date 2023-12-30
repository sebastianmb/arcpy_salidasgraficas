import arcpy
import time  # Importar el módulo time

# Obtener el MXD actual
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]

nombre_archivo_salida = r"D:\IGAC\Procesamiento_tematicas\Memorias dto\Cesar\variables"

# Definir la resolución y otras propiedades de salida
dpi = 130  # Puedes ajustar la resolución aquí


# Nombre de la capa existente que deseas modificar
contador=0
lista_municipios=  ['Gamarra','Aguachica']
capas_y_consultas = {
    "clase_tierra": "",
    
    "Dto_Cesar":"DeNombre= 'Cesar'",
}

nombre_etiqueta = "municipio"
nombre_etiqueta1 = "municipio1"




for municipio in lista_municipios:
    # Actualizar la consulta para la capa "clase_tierra" con el municipio actual
    capas_y_consultas["clase_tierra"] = "MpNombre = '{}'".format(municipio)
    # Iterar a través del diccionario de capas y consultas
    for nombre_capa, consulta in capas_y_consultas.items():
        # Buscar la capa por su nombre
        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.name == nombre_capa:
                # Establecer la definición de consulta
                lyr.definitionQuery = consulta
                # Actualizar la capa
                arcpy.RefreshActiveView()

                if lyr.name  =="clase_tierra":
                    # Hacer zoom a la extensión completa de la capa
                    df = arcpy.mapping.ListDataFrames(mxd)[0]
                    df.extent = lyr.getExtent()
                    time.sleep(2)  # Pausa de 2 segundos
                    arcpy.RefreshActiveView()
                    # Buscar la etiqueta por su nombre
                    for elem in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
                        if elem.name == nombre_etiqueta:
                            print("se encontro la etiqueta "+nombre_etiqueta+ municipio)
                            # Establecer el texto deseado en la etiqueta
                            elem.text=lista_municipios[contador]
                            
                        if elem.name == nombre_etiqueta1:
                            print("se encontro la etiqueta "+nombre_etiqueta+ municipio)
                            # Establecer el texto deseado en la etiqueta
                            elem.text=lista_municipios[contador]
                    
                    contador += 1
                    arcpy.mapping.ExportToJPEG(mxd, nombre_archivo_salida+"/VP"+municipio+".jpg", resolution=dpi)
                # Exportar el mapa como una imagen JPG
                        

                    

                # Refrescar la vista del mapa
                arcpy.RefreshActiveView()

