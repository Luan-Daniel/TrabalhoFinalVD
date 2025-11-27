#!/usr/bin/env python3
"""Runner para gerar visualizações HTML.

Este script executa os scripts de `scripts/` que produzem arquivos HTML
na pasta `output/`. Ele roda cada script com o mesmo interpretador Python
usado aqui e reporta se o arquivo de saída esperado foi gerado.

Uso: python scripts/gerar_visualisacoes.py
"""

from pathlib import Path
import subprocess
import sys
import webbrowser
import os


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


SCRIPTS = [
	(Path("scripts/distribuicao_participantes-sankey/sankey.py"), Path("output/sankey_simplificado.html")),
	(Path("scripts/distribuicao_respostas-radar/QND-radar.py"), Path("output/QND_distribuicao_respostas_radar.html")),
	(Path("scripts/distribuicao_respostas-radar/QVC-radar.py"), Path("output/QVC_distribuicao_respostas_radar.html")),
	(Path("scripts/pontuação_media-barras/média_por_adesão.py"), Path("output/adesao_pontuacao_media.html")),
	(Path("scripts/pontuação_media-barras/média_por_grupo.py"), Path("output/grupo_pontuacao_media.html")),
]


def run_script(script_path: Path, cwd: Path) -> subprocess.CompletedProcess:
	cmd = [sys.executable, str(script_path)]
	print(f"Executando: {' '.join(cmd)} (cwd={cwd})")
	try:
		completed = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, check=False)
	except Exception as e:
		print(f"Falha ao executar {script_path}: {e}")
		raise
	return completed


def main():
	any_fail = False
	for script_rel, expected_out_rel in SCRIPTS:
		script = ROOT / script_rel
		if not script.exists():
			print(f"Aviso: script não encontrado: {script}")
			any_fail = True
			continue

		completed = run_script(script, cwd=ROOT)
		if completed.returncode != 0:
			print(f"Script retornou código {completed.returncode}")
			print("--- stdout ---")
			print(completed.stdout)
			print("--- stderr ---")
			print(completed.stderr)
			any_fail = True
		else:
			print(f"Concluído: {script} (saida: retorno 0)")

		if expected_out_rel is not None:
			expected = ROOT / expected_out_rel
			if expected.exists():
				print(f"Gerado: {expected}")
			else:
				print(f"Aviso: saída esperada não encontrada: {expected}")
				any_fail = True

		print("---")

	if any_fail:
		print("Alguns scripts falharam ou saídas estão faltando.")
		sys.exit(2)
	print("Todos os scripts executados — verifique 'output/' para os HTML gerados.")
	
	file_path = os.path.abspath("index.html")
	url = f"file://{file_path}"
	webbrowser.open(url)


if __name__ == '__main__':
	main()
