from ecommerce.classes.Pedido import Pedido
from ecommerce.classes.Cliente import Cliente
from ecommerce.classes.Ecommerce import Loja


loja = Loja('Loja Nappster')
loja.add_estoque('123', 20, 15)
loja.add_estoque('1234', 25, 7)
pedido = Pedido(Cliente('José dos Santos'))
cliente = Cliente('John Does')
pedido2 = Pedido(cliente)

pedido.add_item(loja.comprar('1234'))
pedido.add_item(loja.comprar('123'))
pedido.add_item(loja.comprar('1234'))
pedido.add_item(loja.comprar('123'))
pedido2.add_item(loja.comprar('1234'))
pedido2.add_item(loja.comprar('123'))

loja.devolver_carrinho(pedido)
pedido2.checkout('dinheiro')
