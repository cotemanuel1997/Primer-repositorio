lista=[1,6,7,8]
def valores(indice):
	print(lista[indice])
	if indice==1:
		return lista[0]
	else:
		return valores(indice-1)
print(valores(len(lista)-1))