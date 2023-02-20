class ListaJuegos:

	first = None

	def add_to_list(self, new_node):
		if self.first == None:
			self.first = new_node
		else:
			temp = self.first
			while temp.next != None:
				temp = temp.next

			temp.next = new_node

	def print_self(self):
		temp = self.first
		n = 1
		print("-------------------------------------------------------------------")
		while temp != None:			
			print(f'Juego #{n}, código: {temp.code} y nombre: {temp.name}')
			print("     Printing platforms list information: ")			
			temp.platform_list.print_self()
			print("")
			temp = temp.next
			n += 1
		print("-------------------------------------------------------------------")