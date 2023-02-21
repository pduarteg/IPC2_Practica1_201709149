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


	def sort_list(self):
		temp = self.first
		it_count = 0
		end = True
		has_changed = False
		anterior = None

		while True:
			it_count+=1
			# print("Iteración #", it_count)

			if temp != None:
				aux = temp.next

			if temp == self.first:
				if int(temp.code) > int(aux.code):
					has_changed = True
					self.first.next = aux.next
					aux.next = self.first
					self.first = aux				
				temp = self.first
			elif temp != None and aux != None:
				if aux.next != None:
					if int(temp.code) > int(aux.code):
						has_changed = True
						temp.next = aux.next
						aux.next = temp
						anterior.next = aux
				else:
					if int(temp.code) > int(aux.code):
						has_changed = True
						anterior.next = aux
						aux.next = temp
						temp.next = None
						anterior = temp
			
			# Verificando si hubo algún cambio
			if temp == None and has_changed:
				has_changed = False
				temp = self.first
				aux = None
				anterior = None
				continue
			elif temp == None and has_changed == False:
				break

			anterior = temp
			temp = temp.next