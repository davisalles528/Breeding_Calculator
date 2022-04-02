# a calculadora considera casais monogâmicos
# apesar das previsões feitas pela ferramenta, o comportamento reprodutivo de um animal é algo consideravelmente imprevisível

cKOmouse = int(input("Quantos animais nocaute condicionais serão necessários?")) #cKOmouse = CD11c-Cre+/- STATfl/fl
RC = int(input("Quantos filhotes cada fêmea gera a cada gestação?")) #RC = reproduction capacity

F2 = cKOmouse*4 #total F2 (25% of F2 is cKO)
bfF2 = F2/RC #females require to generate F2
bmF2 = bfF2 #males require to generate F2
tbF2 = bfF2 + bmF2 #total breeders to generate F2
crestatgF2 = tbF2/2 #total Cre+/- STATfl/- to genereate F2

F1 = crestatgF2*2 #total F1 (50% of F1 is CD11c-Cre+/- STATfl/-)
bfF1 = F1/RC #females require to generate F1
bmF1 = bfF1 #males require to generate F1
tbF1 = bfF1 + bmF1 #total breeders to generate F1
cregF1 = tbF1/2 #total Cre+/- to generate F1

print()
print("Animais necessários para o primeiro cruzamento")

print("Camundongos Cre+/- machos =", cregF1/2)
print("Camundongos Cre+/- fêmeas =", cregF1/2)
print("Camundongos STATfl/fl machos =", bmF1/2)
print("Camundongos STATfl/fl fêmeas =", bfF1/2)
print("Camundongos F1 =", F1)

print()
print("Animais necessários para o segundo cruzamento")

print("Camundongos Cre+/- STATfl/- machos =", crestatgF2/2)
print("Camundongos Cre+/- STATfl/- fêmeas =", crestatgF2/2)
print("Camundongos STATfl/fl machos =", bmF2/2)
print("Camundongos STATfl/fl fêmeas =", bfF2/2)
print("Camundongos F2 =", F2)
input()