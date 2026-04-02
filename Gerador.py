import random
import string
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits
    senha = random.choices(caracteres, k=tamanho)
    senha = "".join(senha)
    return senha
tamanho = int(input("tamanho da senha:"))
print(gerar_senha(tamanho))