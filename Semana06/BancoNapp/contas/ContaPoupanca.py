from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
    """
    Classe representa a conta corrente de pessoa física.
    Limite padrão da conta: R$ 500,00

    Args:
        Conta ([type]): [description]
    """
    def __init__(self,  **kwargs):
        """
        Construtor da classe ContaPoupanca.
        Extrai do dicionário kwargs a profissao do correntista.
        """
        super(ContaPoupanca, self).__init__(**kwargs)
        self.profissao = kwargs.get('profissao', '')
        self.limite = kwargs.get('limite', 0)

    def rendimento_aniversario(self, valor):
        if valor < 0 or valor > 1:
            raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
        self.saldo += self.saldo*valor

    def deposito(self, valor):
        """
        Método para realizar depósito.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do depósito

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.
        """
        if isinstance(valor, (float, int)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo = self.saldo + valor
            self.extrato.append(('D', valor))
            return
        raise TypeError('O depósito precisa ser numérico')

    def saque(self, valor):
        """
        Método para realizar saque.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do saque

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.

        Returns:
            Float: Valor do saque realizado.
        """
        if isinstance(valor, (float, int)):
            if self.limite:
                if valor > (self.saldo + self.limite):
                    raise ValueError('Valor do saque supera seu saldo e seu limite')
                    return
            else:
                if valor > self.saldo:
                    raise ValueError('Valor do saque supera seu saldo.')
                    return
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')

    def get_extrato(self):
        """
        Retorna a lista dos saques e depósitos feitos na conta.

        Returns:
            List: Lista de operações
        """
        return self.extrato