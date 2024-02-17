# -*- coding: utf-8 -*-
import arcpy

# Directorio base
base_dir = "D:\\IGAC_2024\\Procesamiento\\ZHF\\Variables\\Model_Builder\\Intermedios"

def select_and_copy(input_layer, output_shp, criteria):
    arcpy.SelectLayerByLocation_management(input_layer, "INTERSECT", criteria, "", "NEW_SELECTION", "NOT_INVERT")
    arcpy.CopyFeatures_management(input_layer, output_shp, "", "0", "0", "0")
    arcpy.SelectLayerByAttribute_management(input_layer, "CLEAR_SELECTION")

def erase_analysis(input_layer, erase_feature, output_shp):
    arcpy.Erase_analysis(input_layer, erase_feature, output_shp)

def main():
    # Definir variables locales
    R_TERRENO = "R_TERRENO"
    Criterio_1 = "Criterio_1"
    Criterio_2 = "Criterio_2"
    R_TB1_shp = base_dir + "\\PrediosxCriterio\\R_TB1.shp"
    R_TB2_shp = base_dir + "\\PrediosxCriterio\\R_TB2.shp"
    R_TERRENO_sinC1_shp = base_dir + "\\Insumos\\R_TERRENO_sinC1.shp"
    R_TERRENO_sinC2_shp = base_dir + "\\Insumos\\R_TERRENO_sinC2.shp"

    # Seleccionar y copiar según el primer criterio
    select_and_copy(R_TERRENO, R_TB1_shp, Criterio_1)
    erase_analysis(R_TERRENO, R_TB1_shp, R_TERRENO_sinC1_shp)

    # Verificar si el archivo resultante existe
    if arcpy.Exists(R_TERRENO_sinC1_shp,Criterio_2):
        # Seleccionar y copiar según el segundo criterio
        select_and_copy(R_TERRENO_sinC1_shp, R_TB2_shp, Criterio_2)
        erase_analysis(R_TERRENO_sinC1_shp, R_TB2_shp, R_TERRENO_sinC2_shp)
        print("La variable existe, aplicando otros procesos")
    else:
        print("La variable no existe")

if __name__ == "__main__":
    main()
