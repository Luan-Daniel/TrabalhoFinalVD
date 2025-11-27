import plotly.graph_objects as go
import plotly.subplots as sp

# Pontuação média agrupada apenas por adesão

# Dados para QND (Min-Max: 0-12)
qnd_groups = ["Sem adesão (n=30)", "Adesão parcial (n=4)", "Adesão total (n=6)"]
qnd_means = [6.13, 6.50, 7.50]
qnd_std = [2.57, 1.29, 1.05]
qnd_median = [6.50, 6.50, 7.50]

# Dados para QVC (Min-Max: 0-10)
qvc_groups = ["Sem adesão (n=30)", "Adesão parcial (n=4)", "Adesão total (n=6)"]
qvc_means = [7.97, 8.25, 7.67]
qvc_std = [1.56, 1.50, 1.03]
qvc_median = [8.00, 8.00, 8.00]

# Criar subplots lado a lado
fig = sp.make_subplots(
  rows=1, cols=2,
  subplot_titles=(
    "QND - Pontuação média por grupo", 
    "QVC - Pontuação média por grupo")

)

# Gráfico QND
fig.add_trace(go.Bar(
    x=qnd_groups,
    y=qnd_means,
    error_y=dict(type='data', array=qnd_std, visible=True),
    marker_color='indianred',
    name="Média QND"
), row=1, col=1)

# Adicionar medianas como pontos
fig.add_trace(go.Scatter(
    x=qnd_groups,
    y=qnd_median,
    mode="markers",
    marker=dict(color="black", symbol="diamond", size=10),
    name="Mediana QND"
), row=1, col=1)

# Gráfico QVC
fig.add_trace(go.Bar(
    x=qvc_groups,
    y=qvc_means,
    error_y=dict(type='data', array=qvc_std, visible=True),
    marker_color='steelblue',
    name="Média QVC"
), row=1, col=2)

# Adicionar medianas como pontos
fig.add_trace(go.Scatter(
    x=qvc_groups,
    y=qvc_median,
    mode="markers",
    marker=dict(color="black", symbol="circle", size=10),
    name="Mediana QVC"
), row=1, col=2)

# Layout
fig.update_layout(
    title_text="Comparação de desempenho por adesão nos testes QND e QVC",
    showlegend=True,
    height=450,
    width=1200,
    margin=dict(l=40, r=40, t=80, b=40),
    legend=dict(orientation="h", y=-0.2)
)

# Escalas adequadas para cada subplot
fig.update_yaxes(title_text="Pontuação (0-12)", range=[0, 12], row=1, col=1)
fig.update_yaxes(title_text="Pontuação (0-10)", range=[0, 10], row=1, col=2)

# Rótulos do eixo X
fig.update_xaxes(title_text="Grupos de adesão", row=1, col=1)
fig.update_xaxes(title_text="Grupos de adesão", row=1, col=2)

output_file = "output/adesao_pontuacao_media.html"
fig.write_html(output_file)
fig.write_image("doc/img/adesao_pontuacao_media.png")