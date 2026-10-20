# ============================================================
# IMPORTAR PLANILHA ANTIGA (Desafio extra — Aula 21)
# ============================================================
# Importa um CSV com Nome, Telefone, E-mail e Endereço.
# Usa as mesmas classes e validações do cadastro da TechBairro.

import csv
import sys
from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PASTA_PROJETO))

from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente


def importar(caminho_csv, caminho_banco):
    validador = ValidadorCliente()
    gerenciador = GerenciadorClientes(str(caminho_banco))
    importados = 0
    recusados = 0

    with open(caminho_csv, encoding="utf-8-sig", newline="") as arquivo:
        amostra = arquivo.read(2048)
        arquivo.seek(0)
        separador = ";" if amostra.splitlines()[0].count(";") > amostra.splitlines()[0].count(",") else ","
        leitor = csv.DictReader(arquivo, delimiter=separador)
        colunas = {"Nome", "Telefone", "E-mail", "Endereço"}
        if not leitor.fieldnames or not colunas.issubset(set(leitor.fieldnames)):
            raise ValueError("A planilha precisa ter as colunas Nome, Telefone, E-mail e Endereço.")

        for numero, linha in enumerate(leitor, start=2):
            cliente = Cliente(*(str(linha.get(coluna) or "").strip() for coluna in ("Nome", "Telefone", "E-mail", "Endereço")))
            erro = validador.validar(cliente)
            if erro is not None:
                recusados += 1
                print(f"RECUSADO (linha {numero}) - {cliente.nome or '(sem nome)'}: {erro}")
                continue
            try:
                gerenciador.adicionar(cliente)
            except Exception as erro_banco:
                recusados += 1
                print(f"RECUSADO (linha {numero}) - {cliente.nome}: erro ao gravar no banco: {erro_banco}")
                continue
            importados += 1
            print(f"IMPORTADO (linha {numero}) - {cliente.nome}")

    print(f"Resumo: {importados} importados, {recusados} recusados.")
    return importados, recusados


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Uso: python scripts/importar_planilha_antiga.py planilha.csv [caminho_banco.db]")
        sys.exit(1)
    planilha = Path(sys.argv[1]).resolve()
    banco = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 else PASTA_PROJETO / "techbairro.db"
    try:
        importar(planilha, banco)
    except (OSError, ValueError, csv.Error) as erro:
        print(f"Erro ao importar: {erro}")
        sys.exit(1)
