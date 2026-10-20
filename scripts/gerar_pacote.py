from pathlib import Path
import re
import zipfile

RAIZ = Path(__file__).resolve().parent.parent
PASTA_SAIDA = RAIZ / "dist"
PASTAS_EXCLUIR = {"dist", "__pycache__"}
EXTENSOES_EXCLUIR = {".db", ".pyc"}


def ler_versao():
    texto = (RAIZ / "techbairro.py").read_text(encoding="utf-8")
    encontrada = re.search(r'^VERSAO\s*=\s*[\"\']([^\"\']+)[\"\']\s*$', texto, re.MULTILINE)
    if not encontrada:
        raise SystemExit("ERRO: não foi encontrada a linha VERSAO = no techbairro.py")
    return encontrada.group(1)


def verificar_changelog(versao):
    changelog = RAIZ / "CHANGELOG.md"
    if not changelog.exists():
        raise SystemExit("ERRO: CHANGELOG.md não encontrado.")
    texto = changelog.read_text(encoding="utf-8")
    if not re.search(rf'^## v{re.escape(versao)}\b', texto, re.MULTILINE):
        raise SystemExit(f"ERRO: não existe entrada para v{versao} no CHANGELOG.md")


def deve_ignorar(caminho: Path):
    partes_rel = caminho.relative_to(RAIZ).parts
    if any(parte in PASTAS_EXCLUIR for parte in partes_rel[:-1]):
        return True
    if caminho.suffix.lower() in EXTENSOES_EXCLUIR:
        return True
    if caminho.name.startswith("TechBairro-") and caminho.suffix == ".zip":
        return True
    return False


def main():
    versao = ler_versao()
    verificar_changelog(versao)
    destino = PASTA_SAIDA / f"TechBairro-{versao}.zip"
    PASTA_SAIDA.mkdir(exist_ok=True)

    incluidos = []
    deixados = []
    for caminho in sorted(RAIZ.rglob("*")):
        if caminho.is_dir():
            continue
        rel = caminho.relative_to(RAIZ)
        if caminho == destino:
            deixados.append((str(rel), "pasta de saída / próprio pacote"))
            continue
        if deve_ignorar(caminho):
            motivo = "pasta excluída" if any(p in PASTAS_EXCLUIR for p in rel.parts[:-1]) else "tipo de arquivo excluído"
            deixados.append((str(rel), motivo))
            continue
        incluidos.append(str(rel))

    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel in incluidos:
            zf.write(RAIZ / rel, arcname=rel)

    print(f"Versão: {versao}")
    print(f"Pacote: {destino}")
    print("\nArquivos incluídos:")
    for rel in incluidos:
        print(f"  + {rel}")
    print("\nArquivos deixados de fora:")
    for rel, motivo in deixados:
        print(f"  - {rel} ({motivo})")


if __name__ == "__main__":
    main()
