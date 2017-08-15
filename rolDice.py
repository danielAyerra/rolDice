import random

tiposDado={"d4":4, "d6":6,"d8":8,"d10":10,"d12":12,"d20":20,"d100":100}

def tiradaDados(int dice, int typeDie):
	veces=0
	resultados=[None]
	if tipoDado!=None:
		while veces<dice:
			resultados.insert(0,random.randrange(1,(typeDie),1))
			veces=veces+1

		print(resultados)

	else:
		print("Error: No es dado valido")



dados=int(input("Introduzca numero de dados "))
tipoElegido=str(input("Que dado quiere tirar?(dX) "))
tipoDado=tiposDado[tipoElegido]
tiradaDados(dados,tipoDado)
