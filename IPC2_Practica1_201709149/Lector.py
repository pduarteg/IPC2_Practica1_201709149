from tkinter import filedialog
from tkinter import *
from xml.dom import minidom

class Lector:

    file_root = None
    file = None
    read_done = False
    procesed_data = False

    lista_de_pisos_procesados = None    

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
        if self.procesed_data == False:

            print("Procesando información de patrones de pisos...")
            print("")
            self.lista_de_pisos_procesados = Lista_pisos.Lista_pisos()
            lista_de_pisos = self.file.getElementsByTagName("piso")        
            cant_pisos = len(lista_de_pisos)

            if cant_pisos != 0:

                for i in range(cant_pisos):
                    print("Creando el piso: #" + str(i+1) + "...")
                    print("     Verificando datos iniciales...")

                    try:
                        name = lista_de_pisos[i].attributes["nombre"].value
                    except:
                        print("No se han encontrado los atributos requerridos para el piso. ")
                        print("El piso será omitido.")
                        continue
                   
                    # Recoleección de datos para el i-ésimo piso desde aquí:

                    R = int(lista_de_pisos[i].getElementsByTagName("R")[0].childNodes[0].data)
                    C = int(lista_de_pisos[i].getElementsByTagName("C")[0].childNodes[0].data)
                    F = int(lista_de_pisos[i].getElementsByTagName("F")[0].childNodes[0].data)
                    S = int(lista_de_pisos[i].getElementsByTagName("S")[0].childNodes[0].data)

                    pInicial = lista_de_pisos[i].getElementsByTagName("patron")[0]
                    codI = pInicial.attributes["codigo"].value
                    patI = pInicial.childNodes[0].data

                    pFinal = lista_de_pisos[i].getElementsByTagName("patron")[1]
                    codF = pFinal.attributes["codigo"].value
                    patF = pFinal.childNodes[0].data
                  
                    nuevo_piso = Piso.Piso(name, R, C, F, S, codI, patI, codF, patF)
                    self.lista_de_pisos_procesados.agregar(nuevo_piso)

                print("")
                print("Información de teerrenos procesada correctamente.")
                print("")

            else:
                print("")
                print("No se han encontrado pisos.")
                print("")
        else:
            print("Ya se han procesado los datos para el actual archivo cargado en memoria.")
            print("")

    def reset_all_r(self):
        self.file_root = None
        self.file = None
        self.read_done = False
        self.lista_de_pisos_procesados = None
        self.procesed_data = False
        