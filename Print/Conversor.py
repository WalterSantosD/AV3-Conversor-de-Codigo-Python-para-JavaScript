f = open('Entrada_print.txt','r')

dado_bruto = f.read().split()

print("Dado bruto {}".format(dado_bruto))


novo_print = []
adicionar = lambda dado : novo_print.append(dado)


conversor_print = lambda x,add : x[0]=="print" and add("console.log") or x[1] == "(" and add('(') or x[2] =='"' and add('"') or conteudo_string(x) or x[-1]==")" and add(')') or x[-2]=='"'  


def conteudo_string (list):

    for x in list[3:]:
          

        if x == ')':

            break

        adicionar(x)      


resultado = conversor_print(dado_bruto,adicionar)

if(resultado == False):

    print("Sintaxe invalida")
else:

    print("Conversor: {} ".format(resultado))

    print("Lista nova: {}".format(novo_print))


saida = open("saida.txt", "w")

saida.write('dados de saida')

saida.close()

