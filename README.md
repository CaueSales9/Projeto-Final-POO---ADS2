# Sistema de chave dicotômica
Sistema interativo em Python para classificação botânica, utilizando lógica de filtragem para identificar grupos de plantas com base em suas características morfológicas.

# Explicação do código:
O sistema começa com uma lista de dicionários dentro da classe SistemaPlantas. Cada dicionário contém as "regras" (se tem vasos, se tem flores, etc.) que definem qual planta é qual.
No método rodar(), o código faz perguntas ao usuário e, a cada resposta, ele elimina as plantas que não se encaixam.

- Filtro 1: Vascularidade (s/n)
- Filtro 2: Flores e Sementes (s/n)
- Filtro 3: Detalhes visuais (frutos ou formato de folha)

Ao final da filtragem, se restar apenas uma planta na lista, o sistema deixa de usar apenas o "dicionário" e instancia um objeto real daquela classe.

# Tecnologias:
Python 3.x

Programação Orientada a Objetos

# Como usar:
Execute o arquivo principal ->

python3 main.py


# UML
![Texto Alternativo](UMLProjetoFinalPOO.png)
