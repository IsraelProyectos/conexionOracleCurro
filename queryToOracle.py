import accesoOracle
from sqlalchemy.sql import func
import wx
import wx.grid as gridlib
import gridview
miLista=[ ]

query="select distinct * from vaesa_externo.maestro_tmaimg WHERE UPPER(desc_modelo) LIKE upper('xl1')"

ao=accesoOracle.connectToOracle(query)

numColums=0

try:
	cursorData=ao.connect()

	for personaje in cursorData:

		miLista.append(personaje)
		

		numColums=len(personaje)

	print(len(miLista))
	#print(usuario)
except TypeError:
	print("No se pueden sacar resultados")


app = wx.PySimpleApp()
gv=gridview.MyForm(numColums,miLista)

frame = gv.Show()
app.MainLoop()