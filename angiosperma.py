from base import Planta


class Angiosperma(Planta):
    def __init__(self, subtipo):
        self.subtipo = subtipo
        
    def tipo(self):
        return f"ANGIOSPERMA - {self.subtipo}"
    
    def info(self):
        return "Planta com flores verdadeiras e frutos que protegem as sementes."