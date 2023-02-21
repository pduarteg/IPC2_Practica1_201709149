from tkinter import filedialog
from tkinter import *
from xml.dom import minidom

import JuegosViejos
import ListaPlataformas
import ListaJuegos
import Juego
import Plataforma

class Lector:

    file_root = None
    file = None
    read_done = False
    procesed_data = False

    JuegosViejos = None

    def open_a_file(self):
        print("Se cargará un archivo...")
        open_correctly = True
        try:
            root = Tk()
            root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                filetypes=(("Input Files [IPC2]", "*.xml"), ("all files", "*.*")))            
            self.file_root = root.filename            
        except:
            print("Error de directorio")
            open_correctly = False

        if open_correctly == True:
            if self.file_root == "":
                print("Dirección vacía.")
                print("")

        return open_correctly
    
    def read_file(self):
        load_correctly = True
        print("")
        print("Se leerá el directorio...")
        try:
            self.file = minidom.parse(self.file_root)
        except:
            print("Archivo no encontrado o no válido.")
            print("")
            load_correctly = False

        return load_correctly

    def proces_file(self):
        self.juegosViejos = JuegosViejos.JuegosViejos()

        if self.procesed_data == False:

            print(" *** Procesando información de \"JuegosViejos\"...")

            # Procesado de plataformas

            print(" *** Procesando información de \"ListaPlataformas\"...")
            print("")            
            lect_plataformas = self.file.getElementsByTagName("ListaPlataformas")            
            lect_plataformas = lect_plataformas[0].getElementsByTagName("Plataforma")
            platforms_cant = len(lect_plataformas)
            print(" *** Se encontraron", platforms_cant, "plataformas.")

            new_platforms_list = ListaPlataformas.ListaPlataformas()
            
            if platforms_cant != 0:

                for i in range(platforms_cant):
                    print(" *** Guardando datos de la plataforma: #" + str(i+1) + "...")
                    print("     Verificando datos iniciales...")

                    try:
                        code = lect_plataformas[i].getElementsByTagName("codigo")[0].childNodes[0].data
                        name = lect_plataformas[i].getElementsByTagName("nombre")[0].childNodes[0].data
                    except:
                        print("No se han encontrado los atributos requerridos para la plataforma. ")
                        print("La plataforma será omitida.")
                        continue
                   
                    # Recoleección de datos para el i-ésima plataforma:
                    print(f' Se encontró el codigo {code} y nombre {name}')
                    new_platform = Plataforma.Plataforma(code, name)
                    new_platforms_list.add_to_list(new_platform)

                print("")
                self.juegosViejos.setPlataformas(new_platforms_list)
                print(" *** Información de plataformas procesada correctamente.")
                print("")

            else:
                print("")
                print("No se han encontrado plataformas.")
                print("")

            # Procesado de juegos

            print(" *** Procesando información de \"ListadoJuegos\"...")
            print("")            
            lect_games = self.file.getElementsByTagName("ListadoJuegos")            
            lect_games = lect_games[0].getElementsByTagName("Juego")
            games_cant = len(lect_games)
            print(" *** Se encontraron", games_cant, "juegos.")

            new_games_list = ListaJuegos.ListaJuegos()

            if games_cant != 0:

                for i in range(games_cant):
                    print(" *** Guardando datos del juego: #" + str(i+1) + "...")
                    print("     Verificando datos iniciales...")

                    try:
                        code = lect_games[i].getElementsByTagName("codigo")[0].childNodes[0].data
                        name = lect_games[i].getElementsByTagName("nombre")[0].childNodes[0].data
                    except:
                        print("No se han encontrado los atributos requerridos para la plataforma. ")
                        print("La plataforma será omitida.")
                        continue
                   
                    # Recolección de plataformas
                    print(f' Se encontró el codigo {code} y nombre {name}')
                    lect_sub_platforms = lect_games[i].getElementsByTagName("Plataforma")
                    new_platforms_list = ListaPlataformas.ListaPlataformas()

                    for j in lect_sub_platforms:
                        p_code = j.getElementsByTagName("codigo")[0].childNodes[0].data
                        new_platform = Plataforma.Plataforma(p_code, None)
                        new_platforms_list.add_to_list(new_platform)

                    new_game = Juego.Juego(code, name, new_platforms_list)
                    new_games_list.add_to_list(new_game)


                print("")
                self.juegosViejos.setJuegos(new_games_list)
                print(" *** Información de juegos procesada correctamente.")
                print("")

                self.juegosViejos.print_data()

            else:
                print("")
                print("No se han encontrado juegos.")
                print("")
            self.procesed_data = True
        else:
            print("Ya se han procesado los datos para el actual archivo cargado en memoria.")
            print("")

    def reset_all_r(self):
        self.file_root = None
        self.file = None
        self.read_done = False        
        self.procesed_data = False
        self.JuegosViejos = None
        