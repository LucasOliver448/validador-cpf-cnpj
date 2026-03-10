def validar_cpf(cpf_limpo):
    nove_digitos = cpf_limpo[:9]
    soma = 0
    peso = 10

    for numero in nove_digitos:
        soma += int(numero) * peso
        peso -= 1  

    resto = soma % 11
    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    dez_digitos = cpf_limpo[:10]
    soma = 0
    peso = 11

    for numero in dez_digitos:
        soma += int(numero) * peso
        peso -= 1  

    resto = soma % 11
    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    if primeiro_digito == int(cpf_limpo[9]) and segundo_digito == int(cpf_limpo[10]):
        print("CPF Válido! ")
    else:
        print("CPF Inválido! ")
                  
def validar_cnpj(cnpj_limpo):
   doze_digitos = cnpj_limpo[:12]
   pesos_primeiro = [5,4,3,2,9,8,7,6,5,4,3,2]

   soma = 0
   for i in range(12):
       soma += int(doze_digitos[i]) *pesos_primeiro[i]

   resto = soma % 11
   if resto < 2:
       primeiro_digito = 0
   else:
       primeiro_digito = 11 - resto 

   treze_digitos = cnpj_limpo[:13]
   pesos_segundo = [6,5,4,3,2,9,8,7,6,5,4,3,2]
   
   soma = 0
   for i in range(13):
       soma += int(treze_digitos[i]) * pesos_segundo[i]
   
   resto = soma % 11
   if resto <2:
       segundo_digito = 0 
   else:
       segundo_digito = 11 - resto  
       
   if primeiro_digito == int(cnpj_limpo[12]) and segundo_digito == int(cnpj_limpo[13]):
        print("CNPJ Válido! ")
   else:
        print("CNPJ Inválido! ")
            
   

   
        

documento = input("Digite seu CPF ou CNPJ:")

documento_limpo = documento.replace(".", "").replace("-", "").replace("/", "")
if len(documento_limpo) ==11:
    validar_cpf(documento_limpo)
elif len(documento_limpo) ==14:
    validar_cnpj(documento_limpo)
else:
    print("Documento Inválido")