import accesoOracle
from sqlalchemy.sql import func
import wx
import wx.grid as gridlib
import gridview
miLista=[ ]

query="select * from BASTIDORES_DEVUELTOS_ABRIL"

ao=accesoOracle.connectToOracle(query)

numColums=0

try:
	cursorData=ao.connect()

	for personaje in cursorData:

		miLista.append(personaje)
		

		numColums=len(personaje)

	#print(miLista)
	#print(usuario)
except TypeError:
	print("No se pueden sacar resultados")


app = wx.PySimpleApp()
gf=gridview.MyForm(numColums,miLista)

frame = gf.Show()
app.MainLoop()