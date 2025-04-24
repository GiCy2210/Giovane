#Converssor de medidas
def conversão_cm_para_m(centimetros):
    return centimetros / 100
def conversão_m_para_cm(metros):
    return metros * 100

#Converssor de temperaturas
def conversão_Cel_para_Fah(celsius):
    return (celsius * 9/5) + 32
def conversão_Fah_para_Cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

#Menu
def menu():
    print("Olá, seja bem-vindo ao nosso site de conversão de dados!")
    print("Aqui estão nossas opções de converssões:")
    print("1. Coversão de centímetros para metros")
    print("2. Conversão de metros para centímetros")
    print("3. Conversão de Celsius para Fahrenheit")
    print("4. Conversão de Fahrenheit para Celsius")
    print("5. Sair")

#Executor
def executor_dados():
    while True:
        menu()
        escolha = input("Selecione a opção que deseja converter:")
     
        if escolha == '1':
            centímetros = float(input("Digite sua medida em centímetros:"))
            print(f"{centímetros}cm são em {conversão_cm_para_m (centímetros)} metros.")
        elif escolha == "2":
            metros = float(input("Digite sua medida em metros:"))
            print(f"{metros}m são em {conversão_m_para_cm (metros)} centímetros.")
        elif escolha == '3':
            celsius = float(input("Digite sua temperatura em Celsius:"))
            print(f"{celsius}°C são em {conversão_Cel_para_Fah(celsius)}°F.")
        elif escolha == '4':
            Fahrenheit = float(input("Digite sua temperatura em Fahrenheit:"))
            print(f"{Fahrenheit}°F são em {conversão_Fah_para_Cel(Fahrenheit)}°C.")
        elif escolha == '5':
            print("Saindo ...")
            break
        else:
            print("Opção inválida! Tente novamente:")
         
executor_dados()
