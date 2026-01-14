from base import Planta


class Angiosperma(Planta):
    def __init__(self, nome, subtipo, filotaxia, formato, margem):
        super().__init__()
        self.nome = nome
        self.subtipo = subtipo
        self.filotaxia = filotaxia
        self.formato = formato
        self.margem = margem
        
    def tipo(self):
        return f"ANGIOSPERMA - {self.subtipo}"
    
    def info(self):
        return f"Folha {self.formato} com margem {self.margem} e filotaxia {self.filotaxia}"
    
    def ficha_tecnica(self):
        return {
            "Vasos Condutores": "Vasculares",
            "Reprodução": "Sementes"
        }