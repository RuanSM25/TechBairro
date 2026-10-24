# Manual de uso da TechBairro

Este manual explica como a atendente pode cadastrar e cuidar dos registros dos clientes na TechBairro.

## A tela principal

A janela tem quatro campos para preencher: **Nome**, **Telefone**, **E-mail** e **Endereço**. Abaixo dos campos aparece uma mensagem sobre a última ação e o contador **Clientes cadastrados**. Na parte de baixo ficam os botões **Salvar**, **Cancelar** e **Consultar**. O número da versão aparece no canto inferior direito.

## Cadastrar um cliente

1. Na tela principal, preencha Nome, Telefone, E-mail e Endereço.
2. Confira se todos os campos estão preenchidos, se o telefone tem somente números e se o e-mail está no formato `nome@dominio.com`.
3. Clique em **Salvar**.
4. Se o cadastro estiver correto, aparecerá uma mensagem como `Cliente 'Maria' salvo com sucesso!`, e o contador aumentará.
5. Os campos serão limpos para o próximo cadastro.

Se aparecer uma mensagem vermelha, leia o aviso e corrija o que estiver indicado antes de tentar salvar novamente.

## Consultar os clientes cadastrados

1. Na tela principal, clique em **Consultar**.
2. A janela **Consulta de Clientes** mostrará a lista de clientes, com nome, telefone, e-mail e endereço.
3. Se ainda não houver cadastros, aparecerá `Nenhum cliente cadastrado`.
4. Clique uma vez no cliente que deseja selecionar. Para alterar ou excluir, use os botões **Editar selecionado** ou **Excluir selecionado**.
5. Para fechar a consulta, use o botão de fechar da própria janela.

## Alterar os dados de um cliente

1. Clique em **Consultar**.
2. Selecione o cliente e clique em **Editar selecionado**. Também é possível dar dois cliques no nome do cliente.
3. Os dados serão carregados nos campos da tela principal, e aparecerá a mensagem `Editando cliente: Maria`.
4. Altere o que for necessário e clique no botão **Salvar edição**.
5. Se os dados estiverem corretos, aparecerá uma mensagem como `Cliente 'Maria' atualizado com sucesso!`.

Para desistir da alteração, clique em **Cancelar**. A mensagem será `Edição cancelada. Nada foi alterado.`.

## Excluir um cliente

1. Clique em **Consultar**.
2. Selecione o cliente que deseja excluir.
3. Clique em **Excluir selecionado**. Também é possível selecionar o cliente e apertar a tecla **Delete**.
4. Leia a janela **Confirmar exclusão**, que mostra o nome, o telefone e o e-mail do cliente.
5. Se tiver certeza, confirme a exclusão. Essa ação não pode ser desfeita.
6. A lista será atualizada e aparecerá uma mensagem como `Cliente 'Maria' excluído com sucesso!`.

Se mudar de ideia, escolha **Não** na confirmação. O cadastro será mantido.

## Regras de preenchimento

| Campo | Obrigatório? | Regra |
|---|---|---|
| Nome | Sim | Não deixe em branco. Digite o nome do cliente. |
| Telefone | Sim | Digite somente números, sem espaços, parênteses, hífen ou outros caracteres. |
| E-mail | Sim | Informe um endereço com `@` e um ponto depois do `@`, por exemplo `maria@email.com`. |
| Endereço | Sim | Não deixe em branco. Informe o endereço do cliente. |

## Mensagens do sistema

| Mensagem | O que significa | O que fazer |
|---|---|---|
| `Cliente 'Maria' salvo com sucesso!` | O novo cadastro foi salvo. | Confira o contador ou abra **Consultar** para verificar o registro. |
| `Cliente 'Maria' atualizado com sucesso!` | As alterações foram salvas. | Abra **Consultar** se quiser conferir os dados. |
| `Cliente 'Maria' excluído com sucesso!` | O cadastro foi excluído. | A lista é atualizada automaticamente. |
| `Preencha o(s) campo(s): Nome, Telefone, E-mail, Endereço` | Um ou mais campos obrigatórios estão vazios. | Preencha os campos listados e tente salvar de novo. |
| `Telefone inválido: use somente números.` | O telefone contém algo além de números. | Apague espaços, sinais e letras; deixe somente os números. |
| `E-mail inválido: use o formato nome@dominio.com` | O e-mail não está no formato aceito. | Confira se há texto antes do `@` e um ponto depois dele. |
| `Formulário limpo` | Os campos foram apagados. | Preencha os dados do próximo cliente, se necessário. |
| `Edição cancelada. Nada foi alterado.` | A alteração foi cancelada. | O cadastro antigo foi mantido. Para editar, comece novamente pela consulta. |
| `Selecione um cliente antes de editar.` | Nenhum cliente foi selecionado para alteração. | Clique em um cliente na lista e depois em **Editar selecionado**. |
| `Selecione um cliente antes de excluir.` | Nenhum cliente foi selecionado para exclusão. | Clique em um cliente na lista e depois em **Excluir selecionado**. |
| `Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.` | O cadastro deixou de existir antes de a alteração ser salva. | Abra **Consultar** novamente e confira se o cliente continua cadastrado. |

## Dúvidas frequentes

**O que faço se o cadastro não for salvo?**

Leia a mensagem que aparece abaixo dos campos. Confira se os quatro campos estão preenchidos, se o telefone tem somente números e se o e-mail está no formato indicado. Depois, clique em **Salvar** novamente.

**Como encontro um cliente que já cadastrei?**

Clique em **Consultar**. Os clientes aparecem em uma lista. Use a barra ao lado da lista para percorrê-la, se precisar.

**Posso recuperar um cadastro depois de excluí-lo?**

A exclusão não pode ser desfeita pela tela. Por isso, confira o nome antes de confirmar e mantenha cópias de segurança protegidas.

**Por que o contador não mostra o número que eu esperava?**

Abra **Consultar** para conferir os cadastros existentes. Se o programa estiver usando um arquivo de cadastros novo, os clientes de outro computador não aparecerão nele.

**Preciso de internet para usar a TechBairro?**

Não. Depois de baixar os arquivos e preparar o Python com o Tkinter, o programa funciona sem internet.
