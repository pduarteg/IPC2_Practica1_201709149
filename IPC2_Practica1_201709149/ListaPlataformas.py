class ListaPlataformas:

	first = None

	def __init__(self):
		print(" * Nueva lista de plataformas creada.")

	def add_to_list(self, new_node):
		if self.first == None:
			self.first = new_node
		else:
			temp = self.first
			while temp.next != None:
				temp = temp.next

			temp.next = new_node

	def sort_list(self):
		pass

	def print_self(self):
		temp = self.first
		n = 1
		print("-------------------------------------------------------------------")
		while temp != None:
			if temp.name != None:
				print(f' --- Plataforma #{n}, código: {temp.code} y nombre: {temp.name}.')
			else:
				print(f' --- Plataforma #{n}, código: {temp.code}.')
			temp = temp.next
			n += 1
		print("-------------------------------------------------------------------")