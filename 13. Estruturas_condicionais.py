maior_idade = 18
idade_especial = 12
idade = int(input("Informe sua idade: "))

if idade >= maior_idade:
    print("Você é maior de idade e pode tirar a CNH")

if idade < maior_idade:
    print("Você NÃO é maior de idade e NÃO pode tirar a CNH")


if idade >= maior_idade:
    print("Você é maior de idade e pode tirar a CNH")
elif idade == idade_especial:
    print("Você pode fazer as aulas teóricas, mas não as aulas práticas")
else:
    print("Você NÃO é maior de idade e NÃO pode tirar a CNH")


