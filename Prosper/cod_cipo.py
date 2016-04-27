#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
App Name:       CSV-Converter
Version:        1.0
Developer:      Paulo Vazquez
Release Date:   27/04/2016
Last Mod Date:  27/04/2016
License:        MIT LICENSE
"""

import sys
import glob

#Global Definitions
nombre_archivo_entrada = ""     #Input file name
nombre_archivo_salida = ""      #Output file name
ar_input = None                 #Input file
ar_output = None                #Output file
cod_cipo = []                   #Array of codes

#############################################################################
############################### FUNCTIONS ###################################
#############################################################################

#Main Function and program entry point
def main():

    #Call function check_arguments()
    check_arguments()
    #Call function read_codigo_cipo()
    read_codigo_cipo()
    #Call function write_output_file()
    write_output_file(ar_input, cod_cipo)
    return 0

#This function validates the number of arguments
def check_arguments():
    #Check if number of arguments are right
    if len(sys.argv) == 2:
        obtain_file_names()
    else:
        print_menu()

def print_menu():
    global nombre_archivo_entrada

    index = 0
    selected_file = 0
    #Searches into the dir for *.csv files
    files = glob.glob("*.csv")

    if len(files) > 0:
        print()
        print("Bienvenido a Prosper CSV Converter:")
        print("***********************************")
        print()
        print("Elija el fichero a convertir: ")
        print()

        for f in files:
            print("[" + str(index) + "] => " + f)
            index += 1

        print()

        try:
            while True:
                selected_file = input("Fichero a convertir: ")
                if int(selected_file) <= len(files) - 1:
                    break

            nombre_archivo_entrada = files[int(selected_file)]
        except:
            print("\nSe produjo un error intentando abrir el archivo seleccionado.\n")
            quit()
    else:
        print("\nNo hay ficheros que convertir.\n")
        quit()

def obtain_file_names():
    global nombre_archivo_entrada
    global nombre_archivo_salida
    #Get the argument passed by console
    nombre_archivo_entrada = sys.argv[1]
    #Create the  output's file name
    nombre_archivo_salida = nombre_archivo_entrada.replace('.csv', '') + "_cipo.csv"

def read_codigo_cipo():
    global ar_input
    global ar_output
    global cod_cipo

    #Open file for read
    ar_input = open(nombre_archivo_entrada, "r")
    #Open file for write, if not exist then create it
    ar_output = open(nombre_archivo_entrada.replace('.csv', '') + "_cipo.csv", "w+")
    #Counter for loops

    contador = 0

    for linea in ar_input.readlines():
        contador += 1
        #First we're gonna read the "codigo_cipo" column from the last 5000 lines
        if contador >= 15002:
            arreglo_linea = linea.split(',')
            #Save the code into the cod_cipo array
            cod_cipo.append(arreglo_linea[2].replace("\n", ''))
    #Move the cursor to the beginning of the file
    ar_input.seek(0)

def write_output_file(ar_input, cod_cipo):
    global ar_output

    contador = 0
    indice_codigo = 0

    #WRITE HEADING
    ar_output.write("Codigo_Barra,Identificador,Codigo_Amigo,Codigo_Cipo\n")

    for linea in ar_input.readlines():
        contador += 1
        #Read 5000 lines from line 10002
        if contador >= 10002 and contador < 15002:
            #Write the code_cipo field into the file
            ar_output.write(linea.replace("\n", '') + "," + cod_cipo[indice_codigo] + "\n")
            #Move to the next element into the cod_cipo array
            if indice_codigo < len(cod_cipo) - 1:
                indice_codigo += 1

    #Close both files
    ar_input.close()
    ar_output.close()

    print("\nEstado: ")
    print("*******")
    print("\n========================================================================>100%\n")
    print("*** Se finalizó de escribir el archivo: " + nombre_archivo_salida + "\n")
    print("Presione una tecla para continuar...", end = "")
    input()

#############################################################################
############################# MAIN PROGRAM ##################################
#############################################################################

#Call to main
main()
