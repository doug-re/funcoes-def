

def exercicio1():
  m = float(input("Digite um valor em metros: "))  

  centimetros = m * 100  

  print(f"{m} metros equivalem a {centimetros} centímetros.")
def exercicio2():
  v_hora = float(input("Quanto você ganha por hora? "))
  h_trabalhadas = float(input("Quantas horas você trabalha por mês? "))

  salario = v_hora * h_trabalhadas

  print(f"Seu salário mensal é de R$ {salario:.2f}")

def exercicio3():
  temp_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

  temp_celsius = (5 * (temp_fahrenheit - 32) / 9)

  print(f"A temperatura em graus Celsius é: {temp_fahrenheit}F em Celsius é {temp_celsius:.2f}")

def exercicio4():
  alt = float(input("minha altura e de (m) ")) 
  peso = float(input("meu peso e de (kg)"))

  imc = peso / (alt ** 2)
  print('o imc dessa pessoa e de {:.2f}'.format(imc))

def exercicio5():
  limt = 30
  multa = 3.00
  exc = 0

  peso = float(input("peso total dos peixes:"))
  if peso > limt:
    exc = peso - limt
    multa = exc * multa
    print("peso acima do limite de", limt,"kg. multado em R$", multa,"pelo excesso de",exc,"kg.")

def exercicio6():
  v_hora = float(input("Quanto você ganha por hora? "))
  h_trabalhadas = float(input("Quantas horas você trabalha por mês? "))

  salario_B = v_hora * h_trabalhadas
  imposto_R = salario_B * 0.11
  INSS = salario_B * 0.08
  total_descont = imposto_R + INSS
  salario_liquido = salario_B - total_descont

  print("Seu salário bruto é R$ {:.2f}".format(salario_B))
  print("Seu salário líquido é R$ {:.2f}".format(salario_liquido))
  print("Você pagou R$ {:.2f} de imposto".format(imposto_R))
  print("Você pagou R$ {:.2f} de INSS".format(INSS))

def exercicio7():
  p_latas = 80 
  tam_latas = 18 

  area = float(input("Informe o tamanho da área em metros quadrados que será pintada: "))

  litros_nec = area / 3
  latas_nec = litros_nec / tam_latas
  if litros_nec % tam_latas > 0:
      latas_nec += 1
  total = latas_nec * p_latas

  print(f"Você precisará de {latas_nec:.0f} lata(s) de tinta, custando um total de R$ {total:.2f}.")
