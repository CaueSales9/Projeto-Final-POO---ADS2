class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.historico = []

    def adicionar_ao_historico(self, planta_nome):
        self.historico.append(planta_nome)
        print(f"Planta {planta_nome} salva no histórico de {self.nome}!")