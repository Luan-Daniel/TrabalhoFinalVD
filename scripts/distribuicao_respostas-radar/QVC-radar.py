import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Categorias A/B/C (A sempre correta)
categories = ["A", "B", "C"]

# Dados QVC (v01..v10) com alternativas completas e percentuais por grupo
dados = {
    "v01": {
        "Sem adesão": [80.00, 10.00, 10.00],
        "IA c/ adesão": [100.00, 0.00, 0.00],
        "Aula c/ ades.": [100.00, 0.00, 0.00],
        "alternativa_correta": 0,
        "texto": "Qual deve ser o foco clínico principal na fase inicial?",
        "alternativas": [
            "Reduzir medo e restaurar confiança no movimento com exposição gradual",
            "Reduzir a dor antes de qualquer movimento",
            "Restringir flexão lombar por pelo menos 6 semanas"
        ]
    },
    "v02": {
        "Sem adesão": [96.67, 0.00, 3.33],
        "IA c/ adesão": [60.00, 0.00, 40.00],
        "Aula c/ ades.": [100.00, 0.00, 0.00],
        "alternativa_correta": 0,
        "texto": "Qual frase é mais coerente com educação em dor para essa paciente?",
        "alternativas": [
            "A dor pode estar mais relacionada a um sistema de alarme sensível do que a um machucado ativo.",
            "Sua protusão explica toda a sua dor e por isso você não deve pegar peso.",
            "Se doer você deve parar e ficar em repouso até melhorar."
        ]
    },
    "v03": {
        "Sem adesão": [93.33, 3.33, 3.33],
        "IA c/ adesão": [100.00, 0.00, 0.00],
        "Aula c/ ades.": [100.00, 0.00, 0.00],
        "alternativa_correta": 0,
        "texto": "Pensando em prescrição de exercício, a conduta mais adequada é:",
        "alternativas": [
            "Iniciar com movimentos toleráveis e progredir carga e amplitude de forma graduada",
            "Evitar todos os exercícios de flexão por tempo indeterminado",
            "Fazer alongamento lombar"
        ]
    },
    "v04": {
        "Sem adesão": [93.33, 6.67, 0.00],
        "IA c/ adesão": [100.00, 0.00, 0.00],
        "Aula c/ ades.": [100.00, 0.00, 0.00],
        "alternativa_correta": 0,
        "texto": "Ela relata mais medo de agachar e pegar peso. Qual estratégia melhor representa exposição graduada?",
        "alternativas": [
            "Começar com agachamento sem carga, em amplitude confortável, e ir aumentando conforme confiança",
            "Mandar ela agachar com 20 kg logo na primeira sessão ‘pra perder o medo de uma vez’",
            "Evitar realizar o movimento que aciona o medo"
        ]
    },
    "v05": {
        "Sem adesão": [90.00, 3.33, 6.67],
        "IA c/ adesão": [80.00, 0.00, 20.00],
        "Aula c/ ades.": [50.00, 0.00, 50.00],
        "alternativa_correta": 0,
        "texto": "Qual dessas falas piora medo e catastrofização?",
        "alternativas": [
            "Essas imagens mostram que sua coluna está gasta, então evite pegar peso.",
            "Seu corpo pode ficar mais forte pra esse tipo de tarefa.",
            "Vamos treinar o movimento que te dá medo, mas de um jeito seguro."
        ]
    },
    "v06": {
        "Sem adesão": [83.33, 3.33, 13.33],
        "IA c/ adesão": [100.00, 0.00, 0.00],
        "Aula c/ ades.": [100.00, 0.00, 0.00],
        "alternativa_correta": 0,
        "texto": "Ela trabalha em hospital. O que faz mais sentido como recomendação funcional?",
        "alternativas": [
            "Manter o trabalho com adaptação gradual de tarefas e treino semelhante ao trabalho",
            "Afastamento completo até a dor zerar",
            "Liberar somente para atividades sentadas"
        ]
    },
    "v07": {
        "Sem adesão": [40.00, 6.67, 53.33],
        "IA c/ adesão": [20.00, 0.00, 80.00],
        "Aula c/ ades.": [0.00, 50.00, 50.00],
        "alternativa_correta": 0,
        "texto": "Diante da RM antiga mostrando protusão, a melhor interpretação é:",
        "alternativas": [
            "Muitas protusões são achados comuns e não explicam sozinhas a dor, podemos treinar mesmo assim",
            "A imagem mostra lesão grave atual, então o exercício está contraindicado",
            "A piora da dor significa piora da protusão e precisamos orientar a paciente"
        ]
    },
    "v08": {
        "Sem adesão": [83.33, 16.67, 0.00],
        "IA c/ adesão": [100.00, 0.00, 0.00],
        "Aula c/ ades.": [50.00, 50.00, 0.00],
        "alternativa_correta": 0,
        "texto": "Um dos objetivos da educação em dor é:",
        "alternativas": [
            "Diminuir a interpretação de ameaça associada à dor e aumentar senso de controle",
            "Mostrar modelos anatômicos para explicar sua lesão",
            "Ensinar ao paciente que dor é psicológica"
        ]
    },
    "v09": {
        "Sem adesão": [86.67, 0.00, 13.33],
        "IA c/ adesão": [80.00, 20.00, 0.00],
        "Aula c/ ades.": [100.00, 0.00, 0.00],
        "alternativa_correta": 0,
        "texto": "Durante a intervenção com exercício, o paciente relata aumento leve de dor, mas sem piora de função. Qual conduta é mais apropriada?",
        "alternativas": [
            "Explicar que um leve aumento de dor pode ser esperado na adaptação, monitorar resposta e ajustar volume/intensidade se necessário",
            "Suspender totalmente o exercício",
            "Parar o exercício atual e sugerir um outro exercício para reduzir os sintomas"
        ]
    },
    "v10": {
        "Sem adesão": [50.00, 26.67, 23.33],
        "IA c/ adesão": [40.00, 0.00, 60.00],
        "Aula c/ ades.": [50.00, 0.00, 50.00],
        "alternativa_correta": 0,
        "texto": "Qual das opções abaixo pode ser um fator importante e de maior relevância na experiência dolorosa:",
        "alternativas": [
            "Medo do movimento",
            "Muitas horas em pé no trabalho",
            "Carga alta no exercício"
        ]
    }
}

# Criar subplots (3 linhas x 4 colunas) + tabela na última linha
fig = make_subplots(
    rows=4, cols=4,
    specs=[[{'type':'polar'}]*4]*3 + [[{'type':'table','colspan':4}, None, None, None]],
    subplot_titles=[f"Questão {k[1:]}" for k in list(dados.keys())] + [""],
)

# Cores por grupo
cores = {"Sem adesão":"indianred", "IA c/ adesão":"steelblue", "Aula c/ ades.":"seagreen"}

# Adicionar traços para cada questão (cada questão tem 3 traces: Sem adesão, IA, Aula)
for i, q in enumerate(dados.keys()):
    row = i//4 + 1
    col = i%4 + 1

    categorias_adaptadas = categories.copy()
    categorias_adaptadas[dados[q]["alternativa_correta"]] += " ✔️"

    # adicionar as três séries, mantendo a ordem consistente com cores
    for j, grupo in enumerate(cores.keys()):
        valores = dados[q].get(grupo)
        if valores is None:
            # se a chave tiver pequena variação no nome, tente ajustar (compatibilidade)
            continue
        fig.add_trace(
            go.Scatterpolar(
                r=valores,
                theta=categorias_adaptadas,
                fill='toself',
                name=grupo,
                marker_color=cores[grupo],
                visible=True,
                showlegend=True if i==0 else False
            ),
            row=row, col=col
        )

# Dropdown para alternar grupos (coloca 'Sobrepostos' como primeira/ativa)
buttons = []
# Botão para ver todos sobrepostos (padrão)
vis_todos = [True] * (len(dados) * len(cores))
buttons.append(dict(label="Sobrepostos", method="update", args=[{"visible":vis_todos}, {"title":"Distribuição respostas - Todos"}]))

for grupo in cores.keys():
    vis = []
    for _q in dados.keys():
        for g in cores.keys():
            vis.append(g == grupo)
    buttons.append(dict(label=grupo, method="update", args=[{"visible":vis}, {"title":f"Distribuição respostas - {grupo}"}]))

# Layout
fig.update_layout(
    title_text="Distribuição respostas - Todos",
    updatemenus=[dict(type="dropdown", buttons=buttons, x=1.2, y=1.1, active=0)],
    showlegend=True,
    height=1100, width=1200
)

# Ajustar eixos polares
layout_updates = {}
for i, _q in enumerate(dados.keys()):
    key = "polar" if i+1 == 1 else f"polar{i+1}"
    layout_updates[key] = dict(radialaxis=dict(visible=True, range=[0, 100]))
fig.update_layout(**layout_updates)

# Construir tabela com perguntas e alternativas por coluna (mais legível)
ids = list(dados.keys())
questoes = [dados[k]["texto"] for k in ids]
alt_A = [dados[k]["alternativas"][0] for k in ids]
alt_B = [dados[k]["alternativas"][1] for k in ids]
alt_C = [dados[k]["alternativas"][2] for k in ids]

fig.add_trace(
    go.Table(
        header=dict(values=["ID", "Questão", "A (correta)", "B", "C"], fill_color="lightgrey", align="left"),
        cells=dict(values=[ids, questoes, alt_A, alt_B, alt_C], align="left", format=[None, None, None, None, None])
    ),
    row=4, col=1
)

fig.update_layout(height=1600, width=1200)

output_file = "output/QVC_distribuicao_respostas_radar.html"
fig.write_html(output_file)
fig.write_image("doc/img/QVC_distribuicao_respostas_radar.png")