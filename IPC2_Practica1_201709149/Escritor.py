import Lector as LectorClass
import re
import os

class Escritor:
	def write_XML(self, p_list, g_list):
		dirA = os.getcwd()
		dirB = dirA + "\\SalidaOrdenada.xml"

		print(" *** Creando gráfica en ruta específicada...")
		try:
			file = open(dirB, "w")
		except:
			print(" *** La ruta específicada ha producido un error.")
			print(" *** Ruta en conflicto: " + str(dirB))
			print(" *** Creando gráfica en la ruta actual...")
			dirA = os.getcwd()
			dirB = dirA + "\\Grafica"
			file = open(dirB, "w")

		print(" *** Ruta de salida: " + str(dirB))

		# Inicia escritura
		file.write("<?xml version=\"1.0\"?>\n")
		file.write("	<JuegosViejos>\n")
		file.write("		<ListaPlataformas>\n")

		temp = p_list.first
		while temp != None:
			file.write("			<Plataforma>\n")
			file.write("				<codigo>" + str(temp.code) + "</codigo>\n")
			file.write("				<nombre>" + temp.name + "</nombre>\n")
			file.write("			</Plataforma>\n")
			temp = temp.next
		file.write("		</ListaPlataformas>\n")
		file.write("		<ListadoJuegos>\n")

		temp = g_list.first
		while temp != None:
			file.write("			<Juego>\n")			
			file.write("				<codigo>" + temp.code + "</codigo>\n")
			file.write("				<nombre>" + temp.name + "</nombre>\n")
			file.write("				<Plataformas>\n")

			temp2 = temp.platform_list.first
			while temp2 != None:
				file.write("					<Plataforma>\n")
				file.write("						<codigo>" + temp2.code + "</codigo>\n")
				file.write("					</Plataforma>\n")
				temp2 = temp2.next

			file.write("				</Plataformas>\n")
			file.write("			</Juego>\n")

			temp = temp.next
		file.write("		</ListadoJuegos>\n")
		file.write("	</JuegosViejos>\n")		
		file.close()
		file = open(dirB)
		dirC = str(dirB)
		print(" *** Escriura finalizada.")
		print(" *** Se abrirá el archivo:" + dirC)