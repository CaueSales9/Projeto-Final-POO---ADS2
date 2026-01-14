from base import Planta


class Pteridofita(Planta):
    def tipo(self):
        return "PTERIDÓFITA"
    
    def info(self):
        return "As Pteridófitas (como as samambaias) já possuem vasos condutores, mas ainda se reproduzem por esporos, sem sementes."
    
    def ficha_tecnica(self):
        return {
                "Vasos Condutores": "Vasculares",
                "Reprodução": "Esporos"
            }