#Escreva um programa que pergunte a quant. de Km percorridos por um carro alugado e a quant. de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input("digite o numero de km percorridos: "))
dia = int(input("Por quantos dias voce alugou o carro? "))
custototal = (km*0.15) + (dia*60)

print("O preco total a pagar pelo aluguel e km percorridos é {}".format(custototal))                                                                                                                                                                                                    