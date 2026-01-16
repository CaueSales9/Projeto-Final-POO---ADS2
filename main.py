from briofitas import Briofita
from Pteridofita import Pteridofita
from Gimnoperma import Gimnosperma
from angiosperma import Angiosperma
from usuario import Usuario


class SistemaPlantas:
    def __init__(self, usuario):
        self.usuario = usuario
        self.plantas = [
            {"id": "brio", "vaso condutor": False, "nome": "Briófita", "flores": False, "visual": "1"},
            {"id": "pterido", "vaso condutor": True, "nome": "Pteridófita", "flores": False, "visual": "2"},
            {"id": "gimno", "vaso condutor": True, "nome": "Gimnosperma", "flores": True, "fruto": False},
            {"id": "angio_mono", "vaso condutor": True, "nome": "Angiosperma Mono", "flores": True, "fruto": True, "folha": "1"},
            {"id": "angio_dicot", "vaso condutor": True, "nome": "Angiosperma Dicot", "flores": True, "fruto": True, "folha": "2"}
        ]


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


        if not escolha_flor:
                    opcao = input('Qual a estrutura visual?\n1 - Pequena/Musgo\n2 - Samambaia\n> ')
                    
                    final = []
                    for i in possiveis:
                        if i.get('visual') == opcao:
                            final.append(i)
                    possiveis = final
        
        else:
            tem_fruto = input('A semente fica dentro de um fruto? (s/n)\n> ').lower()
            escolha_fruto = True if tem_fruto == 's' else False
            
            temp = []
            for i in possiveis:
                if i.get('fruto') == escolha_fruto:
                    temp.append(i)
            possiveis = temp

            if escolha_fruto and len(possiveis) > 1:
                folha_opcao = input('Tipo de folha\n1 - Paralela\n2 - Ramificada\n> ')
                
                temp_folha = []
                for i in possiveis:
                    if i.get('folha') == folha_opcao:
                        temp_folha.append(i)
                possiveis = temp_folha

        if len(possiveis) == 1:
            item = possiveis[0]
            obj = None

            if item['id'] == "brio":
                obj = Briofita()
            elif item['id'] == "pterido":
                obj = Pteridofita()
            elif item['id'] == "gimno":
                obj = Gimnosperma()
            elif "angio" in item['id']:
                subtipo_real = item['nome']
                obj = Angiosperma(item['nome'], subtipo_real, "Alterna", "Comum", "Lisa")

            if obj:
                print(f"Tipo: {obj.tipo()}")
                print(f"Info: {obj.info()}")
                print(f"Ficha tecnica: {obj.ficha_tecnica()}")
                self.usuario.adicionar_ao_historico(item['nome'])
        else:
            print('Planta nao identificada')
        
        
if __name__ == "__main__":
    user = input('Digite seu nome\n> ')
    user_iden = Usuario(user)
    plantas = SistemaPlantas(user_iden)
    plantas.rodar()
    while True:
        retornar = input('\nDeseja fazer outra analise ? (s/n)\n> ').lower()
        if retornar == 's':
            plantas.rodar()

        else:
            print(f'Sistema desligado\nSeu historico {user_iden.historico}')
            break