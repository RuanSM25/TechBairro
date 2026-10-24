# Manual de uso da TechBairro

Este manual mostra como usar a TechBairro para cadastrar e cuidar dos registros de clientes.

## 1. Abrir o programa

O programa precisa de Python 3 e do Tkinter, que abre as janelas. Depois de baixar e extrair o projeto, abra o terminal dentro da pasta e execute:

```bash
python -m pip install -r requirements.txt
python techbairro.py
```

O arquivo `requirements.txt` não instala bibliotecas externas, porque a TechBairro usa módulos que já vêm com Python. Em algumas instalações do Linux, pode ser necessário instalar o Tkinter pelo próprio sistema.

Ao abrir, aparece a janela **TechBairro — Cadastro de Cliente**, com os campos **Nome**, **Telefone**, **E-mail** e **Endereço**, além dos botões **Salvar**, **Cancelar** e **Consultar**. No canto inferior aparece a versão do programa.

No terminal também aparece a mensagem `Banco em uso:`, seguida do caminho do arquivo `techbairro.db`. Esse arquivo guarda os cadastros.

## 2. Cadastrar um cliente

1. Preencha Nome, Telefone, E-mail e Endereço.
2. Confira se os dados estão corretos.
3. Clique em **Salvar**.
4. Se o cadastro der certo, aparece uma mensagem de sucesso e o contador de clientes é atualizado.

Todos os campos precisam estar preenchidos. O telefone deve ter somente números. O e-mail deve ter um texto antes do `@` e um ponto depois dele, como `nome@dominio.com`.

## 3. Consultar os cadastros

Clique em **Consultar**. A janela **Consulta de Clientes** mostra os registros em uma lista, em ordem alfabética pelo nome.

Se ainda não houver cadastros, aparece **Nenhum cliente cadastrado**. Para editar ou excluir, selecione um cliente na lista.

## 4. Alterar um cadastro

1. Na janela de consulta, selecione o cliente.
2. Clique em **Editar selecionado** ou dê dois cliques no cliente.
3. Os dados voltam para os campos da janela principal.
4. Altere o que precisar e clique em **Salvar edição**.

Para desistir, clique em **Cancelar**. A mensagem informa que a edição foi cancelada e que nada foi alterado.

## 5. Excluir um cadastro

1. Na janela de consulta, selecione o cliente.
2. Clique em **Excluir selecionado** ou pressione a tecla **Delete**.
3. Confira o nome, o telefone e o e-mail exibidos na confirmação.
4. Só confirme se tiver certeza. A exclusão não pode ser desfeita.

Depois da exclusão, a lista e o contador são atualizados.

## 6. Mensagens que podem aparecer

- **Preencha o(s) campo(s): ...** — falta preencher um ou mais campos indicados.
- **Telefone inválido: use somente números.** — retire espaços, sinais e letras do telefone.
- **E-mail inválido: use o formato nome@dominio.com** — confira o e-mail digitado.
- **Cliente 'nome' salvo com sucesso!** — o novo cadastro foi salvo.
- **Cliente 'nome' atualizado com sucesso!** — a alteração foi salva.
- **Cliente 'nome' excluído com sucesso!** — o cadastro foi removido.
- **Selecione um cliente antes de editar/excluir.** — selecione uma linha da lista antes de usar uma dessas opções.
- **Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.** — o cadastro deixou de existir antes de salvar a edição.

## 7. Dúvidas comuns

**O que faço se aparecer uma mensagem de campo vazio?**  
Preencha todos os campos indicados e tente salvar novamente.

**Posso colocar pontos, traços ou espaços no telefone?**  
Não. Nesta versão, o telefone aceita somente números.

**Onde ficam os cadastros? Posso apagar o arquivo do banco?**  
Os cadastros ficam no arquivo `techbairro.db`, na pasta do projeto. Não apague esse arquivo se precisar manter os registros. Para fazer uma cópia de segurança, feche o programa e copie o arquivo para um local protegido. Como ele pode ter dados pessoais, não publique esse arquivo no GitHub.

## 8. Cuidados

Use dados reais somente quando houver autorização para isso. Não compartilhe telefone, e-mail ou endereço de clientes. Antes de fazer mudanças ou transferir o projeto para outro computador, feche o programa e faça uma cópia de segurança do banco de dados.
