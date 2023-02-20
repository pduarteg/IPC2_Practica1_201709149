class Juego:
	code = None
	name = None
	platform_list = None
	next = None

	def __init__(self, code, name, p_list):
		self.code = code
		self.name = name
		self.platform_list = p_list