from briofitas import Briofita
from Pteridofita import Pteridofita
from Gimnoperma import Gimnosperma
from angiosperma import Angiosperma
from usuario import Usuario


class SistemaPlantas:
    def __init__(self):
        self.plantas = [
            {"id": "brio", "vaso condutor": False, "nome": "Briófita", "flores": False, "visual": "1"},
            {"id": "pterido", "vaso condutor": True, "nome": "Pteridófita", "flores": False, "visual": "2"},
            {"id": "gimno", "vaso condutor": True, "nome": "Gimnosperma", "flores": True, "fruto": False},
            {"id": "angio_mono", "vaso condutor": True, "nome": "Angiosperma Mono", "flores": True, "fruto": True, "folha": "1"},
            {"id": "angio_dicot", "vaso condutor": True, "nome": "Angiosperma Dicot", "flores": True, "fruto": True, "folha": "2"}
        ]


    def login(self):
        ident = input('Digite sua identificação\n> ')
        senha = input('Digite sua senha\n>  ')
        

    def rodar(self):
        possiveis = self.plantas


        tem_vascularidade = input('A planta possui vascularidade ? (s/n)\n> ').lower()
        escolha_vasc = True if tem_vascularidade == 's' else False

        filtro = []
        for i in possiveis:
            if i.get('vaso condutor') == escolha_vasc:
                filtro.append(i)
        
        possiveis = filtro

        
        tem_flor = input('A planta tem flores ou sementes ? (s/n)\n> ').lower()
        escolha_flor = True if tem_flor == 's' else False


        filtro = []
        for i in possiveis:
            if i.get('flores') == escolha_flor:
                filtro.append(i)
        
        possiveis = filtro