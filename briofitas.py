from base import Planta


class Briofita(Planta):
    def tipo(self):
        return "BRIÓFITA"
    
    def info(self):
        return "As Briófitas (como os musgos) são plantas pequenas, sem vasos condutores e dependentes de ambientes úmidos."
    
    def ficha_tecnica(self):
        return {
                "Vasos Condutores": "Não possui",
                "Reprodução": "Esporos"
            }