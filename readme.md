
# Visualização de Dados — Trabalho Final CIT7587 (20252)

Projeto final da disciplina Visualização de Dados (CIT7587, 20252). Conjunto de scripts em Python que gera visualizações interativas (Plotly) a partir de dados de uma pesquisa sobre dor aplicada ao curso de Fisioterapia.

**Arquivos importantes**
- **Dados:** `data\Dados e Estatisticas.xlsx` — contém os dados da pesquisa e as estatísticas aplicadas.
- **Scripts:** `scripts\gerar_visualisacoes.py` — ponto de entrada que executa os scripts para gerar as visualizações.
- **Visualizações geradas:** arquivos HTML em `output/`.
- **Página compilada:** `index.html` — página que compila e exibe todas as visualizações geradas.
- **Relatório e imagens:** pasta `doc/` — contém `main.tex` e `doc/img/` com figuras usadas no relatório.

**Como executar (Windows / PowerShell)**
**Requisitos:** Python 3.8+ (recomendado 3.11). As dependências estão listadas em `requirements.txt`.

```powershell
# Criar e ativar ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt

# Gerar todas as visualizações (executa os scripts em `scripts/`)
python .\scripts\gerar_visualisacoes.py
```

**Observações:**
- Você pode executar scripts individuais localizados em `scripts/` ou nos subdiretórios (por exemplo, `scripts\distribuicao_respostas-radar\QND-radar.py`).
- O script principal (`gerar_visualisacoes.py`) assume que o arquivo de dados está em `data\Dados e Estatisticas.xlsx`. Se usar outro caminho, edite o script conforme necessário.

**Resultados do projeto**
- **HTML interativos:** arquivos em `output/` — cada visualização é gerada como um HTML independente.
- **Página agregada:** `index.html` — reúne as visualizações em uma única página navegável.
- **Relatório:** fonte LaTeX em `doc/main.tex` e imagens em `doc/img/`.

**Estrutura do repositório (resumida)**
- `data/` — planilha com dados e estatisticas aplicadas sobre eles
- `scripts/` — geradores das visualizações (ponto de entrada: `gerar_visualisacoes.py`)
- `output/` — visualizações HTML geradas
- `doc/` — relatório e imagens
- `index.html` — página com todas as visualizações

**Dicas e próximos passos**
- Para atualizar as visualizações após alterar os dados, rode novamente `python .\scripts\gerar_visualisacoes.py`.
- Para debugar um gráfico específico, execute o script Python correspondente na pasta `scripts/` e abra o HTML gerado no navegador.

**Licença / Uso**
- Uso acadêmico / projeto de curso. Sinta-se à vontade para adaptar o código para estudos e replicação dos resultados.
- Autor: Luan Daniel (luandanielmelo@gmail.com).