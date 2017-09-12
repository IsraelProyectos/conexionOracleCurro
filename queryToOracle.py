import accesoOracle
miLista=[ ]

query="select * from sko_exec_transactions"

ao=accesoOracle.connectToOracle(query)

try:
	cursorData=ao.connect()

	for personaje in cursorData:

		miLista.append(personaje)

	print(miLista[1])
	#print(usuario)
except TypeError:
	print("No se pueden sacar resultados")