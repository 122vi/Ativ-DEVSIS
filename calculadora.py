#calculadora
number1 = 0
number2 = 0 
result = 0
string = ''

number1 = int(input('Digite o número 1:'))
string = input('Digite a operação: ')
number2 = int(input('Digite o número 2:'))

if string == '+' :
    result = number1 + number2
elif string == '-' :
    result = number1 - number2
elif string == '/' :
    result = number1 / number2
elif string == '*' :
    result = number1 * number2
else:
    result = 'Operação inválida'

print(str(number1) + ' ' + str(string) + ' ' + str(number2) + ' = ' + str(result))
