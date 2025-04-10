class contabancaria:
    def __init__(self, nome, saldo, titular, limite):
        self.nome = nome
        self.saldo = saldo
        self.titular = titular
        self.limite = limite
        #criar uma classe chamada conta bancária com nome e saldo além de ter
        #atributos _titular(privado) _saldo(privado) _limite(privado)
        #métodos Depositar(valor) sacar(valor) get_saldo() set_limite(novo_limite)