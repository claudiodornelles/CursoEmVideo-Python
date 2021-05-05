
while True:
    num = input("Digite um número: ")
    try:
        num = int(num)
    except:
        print("Não inteiro.")
        break
print("Saiu do while")
