from base import Planta


class Gimnosperma(Planta):
    def tipo(self):
        return "GIMNOSPERMA (Ex: Pinheiros/Araucárias)"
    
    def info(self):
        return "Possuem sementes 'nuas' (sem fruto), geralmente em cones ou pinhas. Não têm flores coloridas."