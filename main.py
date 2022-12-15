from random import randint

cnpj = ''.join([str(randint(0, 9)) for _ in range(12)])

for i in range(2):
    digit = 0
    
    for idx, value in enumerate(cnpj[:4 + i][::-1], start=2):
        digit += idx * int(value)
    
    for idx, value in enumerate(cnpj[4 + i:][::-1], start=2):
        digit += idx * int(value)    
    
    digit = 11 - (digit % 11); 
    digit = 0 if digit > 9 else digit
    cnpj += str(digit)    
    
print(f'CNPJ gerado: {cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}')