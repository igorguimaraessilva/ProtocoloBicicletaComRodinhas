import secrets
import string
import uuid


def gerar_senha_letras(comprimento):
    password_characters = string.ascii_letters
    password = ''.join(secrets.choice(password_characters)
                       for i in range(comprimento))
    return password


def gerar_senha_letras_numeros(comprimento):
    password_characters = string.ascii_letters+string.digits
    password = ''.join(secrets.choice(password_characters)
                       for i in range(comprimento))
    return password


def gerar_senhas_letras_numeros_simbolos(comprimento):
    password_characters = string.ascii_letters+string.digits+string.punctuation
    password = ''.join(secrets.choice(password_characters)
                       for i in range(comprimento))
    return password


def gerar_senha_hexadecimal(metade_comprimento):
    password = secrets.token_hex(metade_comprimento)
    return password


def gerar_senha_uuid():
    password = uuid.uuid4()
    return password


if __name__ == '__main__':
    senha = gerar_senha_letras(16)
    print(senha)
    senha = gerar_senhas_letras_numeros_simbolos(16)
    print(senha)
    senha = gerar_senha_hexadecimal(12)
    print(senha)
    senha = gerar_senha_uuid()
    print(senha)
