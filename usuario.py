class Usuario:
    def __init__(self, nome):
        self.__nome = nome
        self.__historico = []

    def adicionar_ao_historico(self, planta_nome):
        self.__historico.append(planta_nome)
        print(f"Planta {planta_nome} salva no histórico de {self.__nome}")

    def get_historico(self):
        return self.__historico