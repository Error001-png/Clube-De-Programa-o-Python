def VerificarJanelasPorComodo(resposta):
    if resposta == "S":
        return True
    else:
        return False

parede_quarto = float(input("Qual o tamanho da parede do quarto?\n"))
parede_cozinha  = float(input("Qual o tamanho da parede da conzinha?\n"))
parede_sala  = float(input("Qual o tamanho da parede da sala?\n"))
Qtd_janelas = int(input("Quantas janelas existe dentro dessa casa?\n"))
Matter_door = input("Qual sera o tipo de material usado para confeccionar a porta?\n") 
Name = input("Qual o nome do proprietario?\n")
casa = 'Esta casa é de :', Name, 'contem 3 comodos, sendo a parede de cada um deles diferente da outra, a cozinha tem: ', parede_cozinha, 'o quarto tem: ', parede_quarto, ' a sala tem: ', parede_sala, ' esta casa em geral terá ', Qtd_janelas, ' janelas no total, o material utlizado para confeccionar a porta é: ', Matter_door,'\n'
print(casa)

#Questão 2
perimetro_paredes = parede_sala+ parede_quarto + parede_sala
print(perimetro_paredes)

Qtd_janelas_novo = int(input("Quantas janelas você deseja retirar do valor atual?\n"))
print('Quantidades de janelas atulizado', Qtd_janelas - Qtd_janelas_novo)

verificar = input("Cada comodo tem pelo menos uma janela?(RESPONDA S/N)\n")

print(VerificarJanelasPorComodo(verificar))
