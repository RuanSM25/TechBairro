# TechBairro

A TechBairro é um programa para cadastrar, consultar, alterar e excluir clientes da associação de moradores.

**Versão atual:** 3.3.1 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastrar clientes com nome, telefone, e-mail e endereço.
- Consultar, alterar e excluir cadastros.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows, macOS ou Linux com ambiente gráfico. |
| Python | Python 3 (versão indicada na release: 3.13.5). |
| Tkinter | Necessário para abrir as janelas; no Ubuntu/Debian pode ser preciso instalar com `sudo apt install python3-tk`. |
| Bibliotecas externas | Nenhuma. |
| Internet | Necessária para baixar o projeto; depois, não é obrigatória. |

## Instalação

### Opção A — Git

```bash
git clone https://github.com/RuanSM25/techbairro.git
cd techbairro
python techbairro.py
```

### Opção B — Download ZIP

No GitHub, clique em **Code → Download ZIP** e extraia o arquivo. Abra um terminal e execute:

```bash
python techbairro.py
```

## Configuração do banco de dados

O programa cria `techbairro.db` na primeira execução, na mesma pasta de `techbairro.py`. O caminho em uso aparece no terminal com a mensagem `Banco em uso:`. O arquivo pode conter dados pessoais e por isso não deve ser publicado. Para fazer uma cópia de segurança, feche o programa e copie o arquivo para um local protegido.

## Como usar

Consulte o [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

- `techbairro.py`: tela principal.
- `cliente.py`: dados do cliente.
- `banco.py`: grava e consulta os registros.
- `validacao.py`: valida os campos.
- `scripts/`: ferramentas auxiliares.
- `docs/`: documentação.

## Autor

Ruan Marques — Técnico em Desenvolvimento de Sistemas, Senac DF.
