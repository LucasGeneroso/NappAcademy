from datetime import datetime

class Username:
	name: str
	username: str
	credit_card: str
	credit_card_expire: str
	birthdate: datetime
	gender: str

	def __init__(self, name: str, username: str, credit_card: str, credit_card_expire: str, birthdate: datetime, gender: str) -> None:
		self.name = name
		self.username = username
		self.credit_card = credit_card
		self.credit_card_expire = credit_card_expire
		self.birthdate = birthdate
		self.gender = gender

	def is_subtring_credit_card(self, parametro='322') -> bool:
		"""
		Função que recebe a lista com todos os registros carregados de um
		arquivo CSV via Reader e busca a string 'parâmetro' como substring
		do campo 'Cartão de Crédito'.
		Args:
			lista (List): [description]
			parametro (str, optional): Substring a ser encontrada. Padrão '322'.
		Returns:
			List: Lista com os nomes de pessoas que possuam substring
			no cartão de crédito
		"""
		if parametro in self.credit_card:
			return True
		return False

	def is_start_subtring_credit_card(self, parametro='303') -> bool:
		"""
		Função que recebe a lista com todos os registros carregados de um
		arquivo CSV via Reader e busca a string 'parâmetro' como início
		do campo 'Cartão de Crédito'.
		Args:
			lista (List): [description]
			parametro (str, optional): Substring a ser encontrada. Padrão '303'.
		Returns:
			List: Lista com os nomes de pessoas que possuam substring
			no cartão de crédito
		"""
		if self.credit_card.startswith(parametro):
			return True
		return False