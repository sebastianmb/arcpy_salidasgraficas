import arcpy


# Función para suavizar el shapefile por área
def suavizar_por_area(input_shapefile, output_shapefile, area_limite):
        # Eliminar el archivo de salida si ya existe
    if arcpy.Exists(output_shapefile):
        arcpy.Delete_management(output_shapefile)
    # Crear una capa de entidad a partir del archivo de entrada
    arcpy.MakeFeatureLayer_management(input_shapefile, output_shapefile)
    # Calcular el área del campo SHAPE@AREA en metros cuadrados
    arcpy.CalculateField_management(output_shapefile, "area", "!SHAPE.AREA@SQUAREMETERS!", "PYTHON")

    arcpy.SelectLayerByAttribute_management(input_shapefile, "NEW_SELECTION", area_limite)
    
    # Ejecutar la herramienta Eliminate para unir los polígonos restantes a los más cercanos
    arcpy.Eliminate_management(input_shapefile, output_shapefile, "AREA")


    print("Proceso completado. ")


def main():
    # Definir variables locales
    
    input_shapefile = "Sample"
    output_shapefile = "salida"
    output_iteracion0_5="iteracion0_5.shp"
    output_iteracion1_0="iteracion1_0.shp"
    output_iteracion1_5="iteracion1_5.shp"
    output_iteracion2_0="iteracion2_0.shp"

    # Definir las áreas de eliminación
    areas_eliminar = [0.5, 1.0, 1.5, 2.0]
    #areas_eliminar_text=['0_5','1_0','1_5','2_0']


    #suavizar_por_area(input_shapefile, temp_output_shapefile, area_limite)
    suavizar_por_area(input_shapefile, output_iteracion0_5, '"area"<0.5*1000')
    if arcpy.Exists(output_iteracion0_5):
        suavizar_por_area(output_iteracion0_5, output_iteracion1_0, '"area"<1*1000')
        """
        suavizar_por_area(input_shapefile, temp_output_shapefile, area_limite)
        suavizar_por_area(input_shapefile, temp_output_shapefile, area_limite)
        suavizar_por_area(input_shapefile, temp_output_shapefile, area_limite)
        """
        print("La variable existe, aplicando otros procesos")
    else:
        print("La variable no existe")        

    

if __name__ == "__main__":
    main()