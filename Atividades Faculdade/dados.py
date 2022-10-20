#rola dados e printa na tela

import random
jog1 = random.randint(1,6)
comp1 = random.randint(1,6)
jog2 = random.randint(1,6)
comp2 = random.randint(1,6)

#rolagens do jogador

if (jog1 == 1):
  print("primeiro dado jogador")
  print(".......")
  print(".     .")
  print(".  *  .")
  print(".     .")
  print(".......")
if (jog1 == 2):
  print("primeiro dado jogador")
  print(".......")
  print(".*    .")
  print(".     .")
  print(".    *.")
  print(".......")
if (jog1 == 3):
  print("primeiro dado jogador")
  print(".......")
  print(".*    .")
  print(".  *  .")
  print(".    *.")
  print(".......")
if (jog1 == 4):
  print("primeiro dado jogador")
  print(".......")
  print(".*   *.")
  print(".     .")
  print(".*   *.")
  print(".......")
if (jog1 == 5):
  print("primeiro dado jogador")
  print(".......")
  print(".*   *.")
  print(".  *  .")
  print(".*   *.")
  print(".......") 
if (jog1 == 6):
  print("primeiro dado jogador")
  print(".......")
  print(".*   *.")
  print(".*   *.")
  print(".*   *.")
  print(".......")

# jogadas jogador 2

if (jog2 == 1):
  print("segundo dado jogador")
  print(".......")
  print(".     .")
  print(".  .  .")
  print(".     .")
  print(".......")
if (jog2 == 2):
  print("segundo dado jogador")
  print(".......")
  print("..    .")
  print(".     .")
  print(".    ..")
  print(".......")
if (jog2 == 3):
  print("segundo dado jogador")
  print(".......")
  print("..    .")
  print(".  .  .")
  print(".    ..")
  print(".......")
if (jog2 == 4):
  print("segundo dado jogador")
  print(".......")
  print("..   ..")
  print(".     .")
  print("..   ..")
  print(".......")
if (jog2 == 5):
  print("segundo dado jogador")
  print(".......")
  print("..   ..")
  print(".  .  .")
  print("..   ..")
  print(".......") 
if (jog2 == 6):
  print("segundo dado jogador")
  print(".......")
  print("..   ..")
  print("..   ..")
  print("..   ..")
  print(".......")

#comp 1

if (comp1 == 1):
  print("primeiro dado computador")
  print(".......")
  print(".     .")
  print(".  .  .")
  print(".     .")
  print(".......")
if (comp1 == 2):
  print("primeiro dado computador")
  print(".......")
  print("..    .")
  print(".     .")
  print(".    ..")
  print(".......")
if (comp1 == 3):
  print("primeiro dado computador")
  print(".......")
  print("..    .")
  print(".  .  .")
  print(".    ..")
  print(".......")
if (comp1 == 4):
  print("primeiro dado computador")
  print(".......")
  print("..   ..")
  print(".     .")
  print("..   ..")
  print(".......")
if (comp1 == 5):
  print("primeiro dado computador")
  print(".......")
  print("..   ..")
  print(".  .  .")
  print("..   ..")
  print(".......") 
if (comp1 == 6):
  print("primeiro dado computador")
  print(".......")
  print("..   ..")
  print("..   ..")
  print("..   ..")
  print(".......")
  
#comp 2

if (comp2 == 1):
  print("segundo dado computador")
  print(".......")
  print(".     .")
  print(".  .  .")
  print(".     .")
  print(".......")
if (comp2 == 2):
  print("segundo dado computador")
  print(".......")
  print("..    .")
  print(".     .")
  print(".    ..")
  print(".......")
if (comp2 == 3):
  print("segundo dado computador")
  print(".......")
  print("..    .")
  print(".  .  .")
  print(".    ..")
  print(".......")
if (comp2 == 4):
  print("segundo dado computador")
  print(".......")
  print("..   ..")
  print(".     .")
  print("..   ..")
  print(".......")
if (comp2 == 5):
  print("segundo dado computador")
  print(".......")
  print("..   ..")
  print(".  .  .")
  print("..   ..")
  print(".......") 
if (comp2 == 6):
  print("segundo dado computador")
  print(".......")
  print("..   ..")
  print("..   ..")
  print("..   ..")
  print(".......")

# fim do codigo
if (jog1 + jog2) > (comp1 + comp2):
 print("Jogador Ganhou!")
elif (comp1 + comp2) > (jog1 + jog2):
 print("Computador Ganhou!")
else:
 print("Empate!")
print("Fim do Jogo!")