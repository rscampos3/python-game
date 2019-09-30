import random

def jogar():
  print("*********************************")
  print("Bem Vindo ao Jogo de adivinhação!")
  print("*********************************")

  print("Qual o nível de dificuldade?")
  print("(1) Fácil (2) Médio (3) Difícil")

  nivel = int(input("Defina o nível: "))

  if (nivel == 1):
      tentativas = 20
  elif (nivel == 2):
      tentativas = 10
  else:
      tentativas = 5

  pontos = 1000

  #numero_secreto = round(random.random()*100)
  numero_secreto = random.randrange(1, 101)

  for rodada in range(1, tentativas + 1):
      print(f"Tentativa {rodada} de {tentativas}")
      chute_str = input("Digite o seu número: ")

      print(f"Você digitou: {chute_str}")
      chute = int(chute_str)

      acertou = numero_secreto == chute
      maior = chute > numero_secreto
      menor = chute < numero_secreto

      if (acertou):
          print(f"Você acertou e fez {pontos} pontos!")
          break
      else:
          if (maior):
              print("Você errou! O seu chute foi maior que o número secreto.")
          elif (menor):
              print("Você errou! O seu chute foi menor que o número secreto.")
          pontos_perdidos = abs(numero_secreto - chute)
          pontos = pontos - pontos_perdidos

      if (rodada == tentativas):
          print(f"O número secreto era {numero_secreto}. Você fez {pontos}")

  print(f"Fim do jogo!")

if(__name__ == "__main__"):
  jogar()