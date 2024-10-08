# Solicitando o nome do usuário
print("Digite seu nome:")
nome= str(input())

print(f"Olá {nome}, agora digite seu peso atual:")
peso = float(input())

print("Agora digite sua altura:")
altura = float(input())

# Função que realiza o cálculo do IMC, onde as variáveis nome, peso e altura são passadas como parâmetros
def calculaIMC(nome, peso, altura):
    #Calculando o IMC
    resultado = peso/(altura * altura)
    # print(type(resultado))
    # print(resultado)
    #Verificando a faixa de IMC e exibindo a mensagem correspondente
    if resultado <= 18.5:
        print(f"{nome}, você está abaixo do peso, seu IMC é igual a: {resultado:.2f}")
    elif 18.5 < resultado <= 24.9:
        print(f"{nome}, seu peso está normal, seu IMC é igual a: {resultado:.2f}")
    elif 25 <= resultado <= 29.9:
        print(f"{nome}, você está com sobrepeso, seu IMC é igual a: {resultado:.2f}")
    elif 30 <= resultado <= 34.9:
        print(f"{nome}, você está com Obesidade Grau 1, seu IMC é igual a: {resultado:.2f}")
    elif 35 <= resultado <= 39.9:
        print(f"{nome}, você está com Obesidade Grau 2, seu IMC é igual a: {resultado:.2f}")
    else:
        print(f"{nome}, você está com Obesidade Grau 3, seu IMC é igual a: {resultado:.2f}")

# Chamando a função calculaIMC passando as variáveis como parâmetros
calculaIMC(nome, peso, altura)

# Array de objetos criado para testar automaticamente o código
pessoas = [
    {"nome": "Ana Silva", "peso": 45, "altura": 1.65},
    {"nome": "Bruno Oliveira", "peso": 70, "altura": 1.75},
    {"nome": "Carla Souza", "peso": 80, "altura": 1.70},
    {"nome": "Diego Ferreira", "peso": 95, "altura": 1.80},
    {"nome": "Elisa Costa", "peso": 105, "altura": 1.65},
    {"nome": "Felipe Lima", "peso": 120, "altura": 1.75},
    {"nome": "Gabriela Mendes", "peso": 130, "altura": 1.60}
]

# Testando o código com um laço de repetição que percorre cada objeto no array e passa as propriedades do objeto para a função calculaIMC
for pessoa in pessoas:
    calculaIMC(pessoa["nome"], pessoa["peso"], pessoa["altura"])