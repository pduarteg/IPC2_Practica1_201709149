class JuegosViejos:

	listaPlataformas = None
	listaJuegos = None

	def __init__(self):
		print("")
		print("Creando información inicial de \"JuevosViejos\"")

	def setPlataformas(self, nueva_lista):
		self.listaPlataformas = nueva_lista

	def setJuegos(self, nueva_lista):
		self.listaJuegos = nueva_lista

	def print_data(self):
		print("")
		print(" ~~~~~~~~~~~~~~~~~~~~~~~~ INFORMACIÓN DE PLATAFORMAS ~~~~~~~~~~~~~~~~~~~~~~~~")
		self.listaPlataformas.print_self()
		print("")
		print(" ~~~~~~~~~~~~~~~~~~~~~~~~ INFORMACIÓN DE JUEGOS ~~~~~~~~~~~~~~~~~~~~~~~~")
		self.listaJuegos.print_self()
		print("")