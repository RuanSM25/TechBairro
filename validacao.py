# ============================================================
# VALIDAÇÃO (Aula 21)
# ============================================================
# Responsabilidade: as regras de negócio do cadastro (RF01 a RF03).
# Este arquivo não sabe nada de janela nem de banco.


class ValidadorCliente:
    # Retorna o primeiro erro ou None se o cliente estiver válido.
    def validar(self, cliente):
        # RF01: campos vazios na mesma ordem exibida na tela.
        vazios = []
        if cliente.nome == "":
            vazios.append("Nome")
        if cliente.telefone == "":
            vazios.append("Telefone")
        if cliente.email == "":
            vazios.append("E-mail")
        if cliente.endereco == "":
            vazios.append("Endereço")
        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"

        # RF02: telefone com somente números.
        if not cliente.telefone.isdigit():
            return "Telefone inválido: use somente números."

        # RF03: e-mail no formato já aceito pela versão 3.3.0.
        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido: use o formato nome@dominio.com"
        return None

    def email_parece_valido(self, email):
        if "@" not in email:
            return False
        usuario, _, dominio = email.partition("@")
        return usuario != "" and "." in dominio
