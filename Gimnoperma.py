from base import Planta


class Gimnosperma(Planta):
    def tipo(self):
        return "GIMNOSPERMA"
    
    def info(self):
        return "Possuem sementes 'nuas' (sem fruto), geralmente em cones ou pinhas. Não têm flores coloridas"
    
    def ficha_tecnica(self):
        return {
                "Vasos Condutores": "Vasculares",
                "Reprodução": "Sementes"
            }