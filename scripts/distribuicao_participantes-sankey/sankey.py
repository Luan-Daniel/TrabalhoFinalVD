import plotly.graph_objects as go

# Definição dos nós (sem os intermediários de não identificados IA/Videoaulas)
labels = [
    "Total (38)",
    "IA (19)",
    "Videoaulas (19)",
    "Identificados, IA (13)",
    "Identificados, Videoaulas (10)",
    "Não Identificados (15)",
    "Usaram, IA (5)",
    "Não aderiram, IA (8)",
    "Usaram, Videoaulas (2)",
    "Não aderiram, Videoaulas (8)",
    "Aderiram, sem identificação (3)",
    "Não aderiram, sem identificação (12)"
]

# Links diretos
sources = [
    0,  # Total → IA
    0,  # Total → Videoaulas
    1,  # IA → Identificados IA
    1,  # IA → Não Identificados (6)
    2,  # Videoaulas → Identificados Videoaulas
    2,  # Videoaulas → Não Identificados (9)
    3,  # Identificados IA → Usaram IA
    3,  # Identificados IA → Não aderiram IA
    4,  # Identificados Videoaulas → Usaram Videoaulas
    4,  # Identificados Videoaulas → Não aderiram Videoaulas
    5,  # Não Identificados (15) → Aderiram sem identificação
    5   # Não Identificados (15) → Não aderiram sem identificação
]

targets = [
    1,  # IA
    2,  # Videoaulas
    3,  # Identificados IA
    5,  # IA → Não Identificados (6)
    4,  # Identificados Videoaulas
    5,  # Videoaulas → Não Identificados (9)
    6,  # Usaram IA
    7,  # Não aderiram IA
    8,  # Usaram Videoaulas
    9,  # Não aderiram Videoaulas
    10, # Aderiram sem identificação
    11  # Não aderiram sem identificação
]

values = [
    19, # Total → IA
    19, # Total → Videoaulas
    13, # IA → Identificados IA
    6,  # IA → Não Identificados
    10, # Videoaulas → Identificados Videoaulas
    9,  # Videoaulas → Não Identificados
    5,  # Identificados IA → Usaram IA
    8,  # Identificados IA → Não aderiram IA
    2,  # Identificados Videoaulas → Usaram Videoaulas
    8,  # Identificados Videoaulas → Não aderiram Videoaulas
    3,  # Não Identificados → Aderiram sem identificação
    12  # Não Identificados → Não aderiram sem identificação
]

# Criando o Sankey
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
)])

fig.update_layout(title_text="Fluxo de Participantes no Estudo", font_size=12)

output_file = "output/sankey_simplificado.html"
fig.write_html(output_file)
fig.write_image("doc/img/sankey_simplificado.png", width=1200, height=900)