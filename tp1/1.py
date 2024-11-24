# 1. Escreva um código usando list comprehension em Python que retorne
# os caracteres individuais de uma string que não são caracteres de espaço em branco.
# Aplique-a à string "Sítio do pica-pau amarelo \n 2023”.

s = "Sítio do pica-pau amarelo \n 2023"

# List comprehension to get non-whitespace characters
chars = [c for c in s if not c.isspace()]

print(chars)

