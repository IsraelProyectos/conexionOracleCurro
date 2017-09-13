import accesoOracle
from sqlalchemy.sql import func
import wx
import wx.grid as gridlib
import gridview
miLista=[ ]

query="select distinct * from SKO_PRE_ITV_MAIL_TOFF"

ao=accesoOracle.connectToOracle(query)

numColums=0

try:
	cursorData=ao.connect()

	for registro in cursorData:

		miLista.append(registro)
		

		numColums=len(registro)

	print(len(miLista))
	#print(usuario)
except TypeError:
	print("No se pueden sacar resultados")


app = wx.PySimpleApp()
gv=gridview.MyForm(numColums,miLista)

frame = gv.Show()
app.MainLoop()