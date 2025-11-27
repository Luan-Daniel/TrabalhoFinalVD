import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Categorias
categories = ["Verdade", "Falso", "Não sei"]

# Dados exemplo (apenas 3 questões para ilustrar)
dados = {
    "q01": {
        "Sem adesão": [90.00, 0.00, 10.00],
        "IA c/ adesão": [100.00, 0.00, 0.00],
        "Aula c/ adesão": [100.00, 0.00, 0.00],
        "alternativa_correta": 0,  # Verdade
        "texto": "Questão 01"
    },
    "q02": {
        "Sem adesão": [16.67, 66.67, 16.67],
        "IA c/ adesão": [20.00, 80.00, 0.00],
        "Aula c/ adesão": [0.00, 100.00, 0.00],
        "alternativa_correta": 1,  # Falso
        "texto": "Questão 02"
    },
    "q03": {
        "Sem adesão": [80.00, 0.00, 20.00],
        "IA c/ adesão": [100.00, 0.00, 0.00],
        "Aula c/ adesão": [100.00, 0.00, 0.00],
        "alternativa_correta": 0,  # Verdade
        "texto": "Questão 03"
    },
    "q04": {
        "Sem adesão": [13.33, 70.00, 16.67],
        "IA c/ adesão": [20.00, 80.00, 0.00],
        "Aula c/ adesão": [0.00, 100.00, 0.00],
        "alternativa_correta": 1,  # Falso
        "texto": "Questão 04"
    },
    "q05": {
        "Sem adesão": [36.67, 40.00, 23.33],
        "IA c/ adesão": [40.00, 40.00, 20.00],
        "Aula c/ adesão": [50.00, 50.00, 0.00],
        "alternativa_correta": 0,  # Verdade
        "texto": "Questão 05"
    },
    "q06": {
        "Sem adesão": [36.67, 3.33, 60.00],
        "IA c/ adesão": [40.00, 0.00, 60.00],
        "Aula c/ adesão": [50.00, 50.00, 0.00],
        "alternativa_correta": 0,  # Verdade
        "texto": "Questão 06"
    },
    "q07": {
        "Sem adesão": [20.00, 53.33, 26.67],
        "IA c/ adesão": [60.00, 40.00, 0.00],
        "Aula c/ adesão": [0.00, 100.00, 0.00],
        "alternativa_correta": 1,  # Falso
        "texto": "Questão 07"
    },
    "q08": {
        "Sem adesão": [40.00, 33.33, 26.67],
        "IA c/ adesão": [60.00, 40.00, 0.00],
        "Aula c/ adesão": [50.00, 50.00, 0.00],
        "alternativa_correta": 1,  # Falso
        "texto": "Questão 08"
    },
    "q09": {
        "Sem adesão": [3.33, 16.67, 80.00],
        "IA c/ adesão": [0.00, 20.00, 80.00],
        "Aula c/ adesão": [0.00, 0.00, 100.00],
        "alternativa_correta": 1,  # Falso
        "texto": "Questão 09"
    },
    "q10": {
        "Sem adesão": [23.33, 53.33, 23.33],
        "IA c/ adesão": [80.00, 20.00, 0.00],
        "Aula c/ adesão": [0.00, 0.00, 100.00],
        "alternativa_correta": 1,  # Falso
        "texto": "Questão 10"
    },
    "q11": {
        "Sem adesão": [63.33, 23.33, 13.33],
        "IA c/ adesão": [80.00, 20.00, 0.00],
        "Aula c/ adesão": [50.00, 50.00, 0.00],
        "alternativa_correta": 1,  # Falso
        "texto": "Questão 11"
    },
    "q12": {
        "Sem adesão": [53.33, 10.00, 36.67],
        "IA c/ adesão": [80.00, 0.00, 20.00],
        "Aula c/ adesão": [100.00, 0.00, 0.00],
        "alternativa_correta": 0,  # Verdade
        "texto": "Questão 12"
    }
}

# Criar subplots (3 linhas x 4 colunas) + tabela
fig = make_subplots(
    rows=4, cols=4,
    specs=[[{'type':'polar'}]*4]*3 + [[{'type':'table','colspan':4}, None, None, None]],
    subplot_titles=[f"Questão {i+1:02}" for i in range(12)]
)

# Adicionar traços para cada questão
cores = {"Sem adesão":"indianred", "IA c/ adesão":"steelblue", "Aula c/ adesão":"seagreen"}

for i, q in enumerate(dados.keys()):
    row = i//4 + 1
    col = i%4 + 1

    categorias_adaptadas = categories.copy()
    categorias_adaptadas[dados[q]["alternativa_correta"]] += "✔️"
    for j, (grupo, valores) in enumerate(dados[q].items()):
        if grupo == "texto" or grupo == "alternativa_correta": continue
        fig.add_trace(
            go.Scatterpolar(
                r=valores,
                theta=categorias_adaptadas,
                fill='toself',
                name=grupo,  # legenda única
                marker_color=cores[grupo],
                    visible=True,
                showlegend=True if i==0 else False  # só mostra na primeira questão
            ),
            row=row, col=col
        )

# Dropdown para alternar grupos (coloca 'Sobrepostos' como primeira/ativa)
buttons = []
# Botão para ver todos sobrepostos (padrão)
vis_todos = [True] * (len(dados) * len(cores))
buttons.append(dict(label="Sobrepostos", method="update", args=[{"visible":vis_todos}]))

for grupo in cores.keys():
    vis = []
    for q in dados.keys():
        for g in cores.keys():
            vis.append(g==grupo)  # True só para o grupo selecionado
    buttons.append(dict(label=grupo, method="update", args=[{"visible":vis}]))

# Adicionar menu
fig.update_layout(
    title_text="Distribuição respostas - Todos",
    updatemenus=[dict(type="dropdown", buttons=buttons, x=1.2, y=1.1, active=0)],
    showlegend=True,   # aqui você pode ativar legenda global
    height=900, width=1200
)

# Ajustar layout polar
layout_updates = {}
for i, _q in enumerate(dados.keys()):
    key = "polar" if i+1 == 1 else f"polar{i+1}"
    layout_updates[key] = dict(radialaxis=dict(visible=True, range=[0, 100]))
fig.update_layout(**layout_updates)

# Adicionar tabela com questões e respostas corretas
questoes = [
    "Quando parte do seu corpo está lesionado, receptores especiais da dor levam a mensagem da dor para seu cérebro.",
    "Dor somente ocorre quando você está lesionado ou está correndo risco de se lesionar.",
    "Nervos especiais na sua medula espinhal levam mensagens de perigo para o seu cérebro.",
    "Dor ocorre sempre que você está lesionado.",
    "O cérebro decide quando você vai sentir dor.",
    "Os nervos se adaptam aumentando seu nível de excitabilidade em repouso.",
    "Dor crônica significa que uma lesão não foi curada corretamente.",
    "Piores lesões resultam sempre em pior dor.",
    "Neurônios descendentes são sempre inibitórios.",
    "Quando você se lesiona, o ambiente em que você está não afetará a quantidade de dor que você sente, desde que a lesão seja exatamente a mesma.",
    "É possível sentir dor e não saber disso.",
    "Quando você está lesionado, receptores especiais levam a mensagem de perigo para a sua medula espinhal."
]

questoes = [f"Questão {i+1}: {questoes[i]} ({categories[dados[f'q{i+1:02}']['alternativa_correta']]})" for i in range(len(questoes))]
fig.add_trace(
    go.Table(
        header=dict(values=["Questão"], fill_color="lightgrey", align="left"),
        cells=dict(values=[questoes], align="left")
    ),
    row=4, col=1
)

fig.update_layout(height=1600, width=1200)

output_file = "output/QND_distribuicao_respostas_radar.html"
fig.write_html(output_file)
fig.write_image("doc/img/QND_distribuicao_respostas_radar.png")