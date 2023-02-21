import Lector as LectorClass
import Escritor as WriterClass
import sys
from tkinter import filedialog
from tkinter import *
import re
import os

class Menu:

    lector_obj = LectorClass.Lector()
    writer_obj = WriterClass.Escritor()

    def __init__(self, exit):
        self.exit = exit

    def imprimir_menu(self):
        print(" ****************************************************************************")
        print(" *                              MENÚ PRINCIPAL                              *")
        print(" ****************************************************************************")
        print("")
        print("  [1] Cargar archivo")
        print("  [2] Procesar información de XML de entrada")
        print("  [3] Ordenar y generar archivo de salida")
        print("  [4] Mostrar estructuras actualmente.")
        print("  [5] Salir")
        print("")
        print("Escriba el número de acuerdo a la opción que desee: ")

    def imprimir_menu_de_carga(self):
        print("")
        print("---------------- Carga de archivos: ----------------")
        print("")
        print(" [1] Escribir dirección")
        print(" [2] Seleccionar archivo")
        print(" [3] Regresar al menú principal")
        print("")
        print("Escriba el número de acuerdo a la opción que desee: ")

    def iniciar_menu(self):
        print("")
        while(self.exit == False):
            self.imprimir_menu()
            try:
                selected_option = int(input())
            except:
                print(" Error de entrada. Intente de nuevo")
                print("")
                continue
            if selected_option == 1:
                back = False
                while back == False:
                    self.imprimir_menu_de_carga()
                    selected_option_l = 0
                    try:
                        selected_option_l = int(input())
                    except:
                        print(" Error de entrada. Intente de nuevo")
                        print("")
                        continue

                    if selected_option_l == 1:
                        if self.lector_obj.read_done:
                            print(" Borrando datos anterioes...")
                        self.lector_obj.reset_all_r()

                        print(" Escriba una ruta específica:")
                        root = input()
                        if root == "":
                            print(" Dirección vacía.")
                            print("")
                        else:
                            self.lector_obj.file_root = root
                            if self.lector_obj.read_file():
                                print(" Carga realizada exitosamente.")
                                print("")
                                self.lector_obj.read_done = True                                
                                back = True
                    elif selected_option_l == 2:
                        if self.lector_obj.read_done:
                            print(" Borrando datos anterioes...")
                        self.lector_obj.reset_all_r()

                        print(" Elija el archivo para cargarlo:")

                        if self.lector_obj.open_a_file():
                            if self.lector_obj.read_file():
                                print(" Carga realizada exitosamente.")
                                print("")
                                self.lector_obj.read_done = True
                                back = True
                    elif selected_option_l == 3:
                        print(" Regresando al menú principal.")
                        print("")
                        back = True
                    else:
                        print("La opción no es válida, intente de nuevo.")
                        print("")                
            elif selected_option == 2:
                if self.lector_obj.read_done:
                    print(" __________________ Se procesará la información del archivo de entrada...")
                    self.lector_obj.proces_file()
                else:
                    print("")
                    print(" [!] Aún no se ha cargado un archivo de entrada en memoria.")
                    print("")
            elif selected_option == 3:
                if self.lector_obj.procesed_data:
                    p_list = self.lector_obj.juegosViejos.listaPlataformas
                    g_list = self.lector_obj.juegosViejos.listaJuegos

                    print(" __________________ Se realizará el ordenamiento...")
                    p_list.sort_list()
                    g_list.sort_list()
                    print(" *** Ordenamiento realizado.")
                    print("")
                    print(" __________________ Se realizará la escritura del archivo de salida...")

                    self.writer_obj.write_XML(p_list, g_list)
                    print(" _____________________________________________________________________")
                    print("")
                    print("")
                    print("")
                else:
                    print("")
                    print(" [!] Aún no se ha procesado un archivo de entrada.")
                    print("")
            elif selected_option == 4:
                if self.lector_obj.procesed_data:
                    print(" __________________ Se mostrarán los datos en memoria...")
                    print("")
                    self.lector_obj.juegosViejos.print_data()
                else:
                    print("")
                    print(" [!] Aún no se ha procesado un archivo de entrada.")
                    print("")
            elif selected_option == 5:
                self.exit = True
                print("")
                print("Se cerrará el programa.")
                print(". . .")
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")