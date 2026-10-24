# TechBairro

A TechBairro é um programa simples para cadastrar, consultar, alterar e excluir clientes de uma associação de moradores.

**Versão:** 3.3.1  
As mudanças de cada versão estão no [CHANGELOG](CHANGELOG.md).

## O que o programa faz

- Cadastra clientes com nome, telefone, e-mail e endereço.
- Mostra os clientes cadastrados.
- Permite alterar e excluir um cadastro.
- Confere se os campos foram preenchidos, se o telefone tem somente números e se o e-mail parece válido.

## O que é necessário

- Python 3 instalado.
- Tkinter disponível para abrir as janelas.
- Não é preciso instalar bibliotecas externas para a aplicação.

O programa precisa de uma conexão com a internet para baixar o projeto. Depois de baixar, a internet não é necessária para usar a aplicação. Em algumas distribuições Linux, o Tkinter precisa ser instalado separadamente pelo sistema.

## Como instalar e abrir

### Opção 1 — Clonar com Git

Abra o terminal e execute:

```bash
git clone https://github.com/RuanSM25/techbairro.git
cd techbairro
python -m pip install -r requirements.txt
python techbairro.py
```

### Opção 2 — Baixar o ZIP

1. Abra o repositório no GitHub.
2. Clique em **Code** e depois em **Download ZIP**.
3. Extraia o arquivo ZIP e abra um terminal dentro da pasta extraída.
4. Execute:

```bash
python -m pip install -r requirements.txt
python techbairro.py
```

O arquivo `requirements.txt` está incluído para registrar as dependências. Como o projeto não usa bibliotecas externas, o comando não precisa baixar pacotes da aplicação.

Ao abrir, aparece a janela **TechBairro — Cadastro de Cliente**. No terminal, o programa mostra `Banco em uso:` e o caminho do arquivo de banco de dados.

## Banco de dados

O programa cria o arquivo `techbairro.db` na pasta onde está `techbairro.py`, se o banco ainda não existir. Os cadastros ficam nesse arquivo.

**Não publique `techbairro.db` no GitHub**, porque ele pode guardar nomes, telefones, e-mails e endereços de pessoas. Para fazer uma cópia de segurança, feche o programa e copie o arquivo para um local protegido.

## Como usar

Veja o [Manual de uso](docs/manual_de_uso.md), com instruções para cadastrar, consultar, alterar e excluir clientes.

## Arquivos principais

- `techbairro.py`: janela e ações do programa.
- `cliente.py`: representa os dados de um cliente.
- `banco.py`: grava, consulta, altera e remove os registros no SQLite.
- `validacao.py`: confere os campos preenchidos.
- `requirements.txt`: informa as dependências do projeto.
- `CHANGELOG.md`: registra as mudanças feitas nas versões.
- `scripts/`: contém ferramentas auxiliares.
- `docs/`: contém a documentação de uso.

## Autor

Ruan Marques — Técnico em Desenvolvimento de Sistemas, Senac DF.
