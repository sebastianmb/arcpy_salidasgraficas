import arcpy
import time  # Importar el módulo time

# Obtener el MXD actual
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]

nombre_archivo_salida = r"D:\IGAC\Procesamiento_tematicas\Memorias dto\Guajira\variables"

# Definir la resolución y otras propiedades de salida
dpi = 130  # Puedes ajustar la resolución aquí


# Nombre de la capa existente que deseas modificar
contador=0
lista_grupos=  ['Barrancas','Distracción','El Molino','Hatonuevo','La Jagua Del Pilar','San Juan Del Cesar','Urumita','Villanueva']
lo_capas_y_consultas = {
    "RCaribeAndesNorte": "",
    
    "Dto Cesar":"DeNombre= 'Cesar'",

    "Rutas_line": "",

    "Rutas_punto":"",
}
#Consulta rutas y paradas
ru_capas_y_consultas = {

    "Rutas_line": "",

    "Rutas_punto":"",
}

nombre_etiqueta = "municipio"
nombre_etiqueta1 = "municipio1"




for grupo in lista_grupos:
    # Actualizar la consulta para la capa "clase_tierra" con el municipio actual
    lo_capas_y_consultas["RCaribeAndesNorte"] = "MpNombre = '{}'".format(grupo)
    
    # Iterar a través del diccionario de capas y consultas
    for nombre_capa, consulta in lo_capas_y_consultas.items():
        # Buscar la capa por su nombre
        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.name == nombre_capa:
                # Establecer la definición de consulta
                lyr.definitionQuery = consulta
                # Actualizar la capa
                arcpy.RefreshActiveView()
                """
                    Ya esta en el grupo de municipios
                    que conforman una ruta, se debe
                    buscar la ruta correspondiente a 
                    ese grupo


                """
                for nombre_capa, consulta in ru_capas_y_consultas.items():
                    ru_capas_y_consultas["Rutas_line"] = "MpNombre = '{}'".format(grupo)
                    ru_capas_y_consultas["Rutas_punto"] = "MpNombre = '{}'".format(grupo)
                    for lyr in arcpy.mapping.ListLayers(mxd):
                        if lyr.name == nombre_capa:
                            # Establecer la definición de consulta
                            lyr.definitionQuery = consulta
                            # Actualizar la capa
                            arcpy.RefreshActiveView()
                    

                if lyr.name  =="RCaribeAndesNorte":
                    # Hacer zoom a la extensión completa de la capa
                    df = arcpy.mapping.ListDataFrames(mxd)[0]
                    df.extent = lyr.getExtent()
                    time.sleep(5)  # Pausa de 2 segundos
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
                    arcpy.mapping.ExportToJPEG(mxd, nombre_archivo_salida+"/SEG_"+municipio+".jpg", resolution=dpi)
                # Exportar el mapa como una imagen JPG
                        

                    

                # Refrescar la vista del mapa
                arcpy.RefreshActiveView()

