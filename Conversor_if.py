from teste import Print


f = open('Entrada_if.txt','r')

dado_bruto =  f.read().split() 

print("Dado bruto {}".format(dado_bruto))


novo_if = []
adicionar = lambda dado: novo_if.append(dado)

conversor_if = lambda x,add : x[0] =='if' and (add('if') or add('(') or conteudo_logico(x))


def conteudo_logico(list):
    for x in list[1:]:

        if x=="or":
            adicionar('||')
            continue
        if x=="and":
            adicionar('&&')
            continue
        if x ==":":
            adicionar(')')
            adicionar('{')

            print("ponto de quebra: {} ".format(dado_bruto.index(x)) )
            conteudo_codigo(list,dado_bruto.index(x))
            break
        else:
            adicionar(x)

def conteudo_codigo(list,inicio):
    for x in list[inicio+1:]:
        if x==')':
            termina = list.index(x)
            print("termina em: {} = {}".format(list.index(x),x))
       
    for x in list[inicio+1:termina+1]:
        if x=="print": 
            adicionar(Print(list[inicio+1:termina+1]))          



resultado = conversor_if(dado_bruto,adicionar)

if(resultado == False):
    print("Sintaxe invalida")
else:
    print(resultado)
    print("Lista nova: {}".format(novo_if))