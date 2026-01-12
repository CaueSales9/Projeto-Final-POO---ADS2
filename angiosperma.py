from base import Planta

class Angiosperma(Planta):
    def __init__(self, nome, subtipo, filotaxia, formato, margem, tem_latex):
        super().__init__()
        self.nome = nome
        self.subtipo = subtipo
        self.filotaxia = filotaxia
        self.formato = formato
        self.margem = margem
        self.tem_latex = tem_latex
        
    def tipo(self):
        return f"ANGIOSPERMA - {self.subtipo}"
    
    def info(self):
        return f"Folha {self.formato} com margem {self.margem}"