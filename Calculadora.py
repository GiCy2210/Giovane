#Operações
def soma(a, b): 
    return a + b 

def subtrair(a, b): 
    return a - b 

def multiplicação(a, b): 
    return a * b 

def divisão(a, b): 
    if divisão == '0': 
        print("Divisão inválida!") 
    else: 
        return a / b 

#Menu
def menu(): 
    print("Ben-vindo á nossa calculadora!") 
    print("Estas são nossaas opções de operações:") 
    print("1. Soma") 
    print("2. Subtração") 
    print("3. Multiplicação") 
    print("4. Divisão") 
    print("5. Sair")  

#Executor
def executor(): 
    while True: 
        menu() 
        escolha = input("Escolha a operação desejada:")         

        if escolha in ['1', '2', '3', '4']: 
            num1 = float(input("Digite o primeiro valor:")) 
            num2 = float(input("Digite o segundo valor:"))              

            if escolha == '1': 
                print(f"{num1} + {num2} = {soma(num1, num2)}") 
            elif escolha == '2': 
                print(f"{num1} - {num2} = {subtrair(num1, num2)}") 
            elif escolha == '3': 
                print(f"{num1} * {num2} = {multiplicação(num1, num2)}") 
            elif escolha == '4': 
                print(f"{num1} / {num2} = {divisão(num1, num2)}") 
        elif escolha == '5': 
            print("Saindo...") 
            break 
        else: 
            print("Operação inválida!") 
            print("Tente novamente!")                 

executor() 
