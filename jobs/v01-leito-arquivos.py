emails = []

with open('d:/Users/igorf/Documents/MeusProjetos/Python/jobs/dados.txt', 'r') as arquivo:
    for linha in arquivo:
        email = linha.strip()
        emails.append(email)

with open('resultados.txt', 'w') as arquivo_resultado:
    for email in emails:
        arquivo_resultado.write(f"txt_email like '%{email}%'\n")

print("Lista de Endereços de E-mail salva em 'resultados.txt'")