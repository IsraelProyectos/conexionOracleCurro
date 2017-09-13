import accesoOracle
from sqlalchemy.sql import func
import wx
import wx.grid as gridlib
import gridview
miLista=[ ]

query="select * from SKO_MANT_GRATUITO_MAIL_TOFF"

connectionString='WORK_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH'

ao=accesoOracle.connectToOracle(query,connectionString)
app=wx.App()
numColums=0

try:
	cursorData=ao.connect()

	for registro in cursorData:

		miLista.append(registro)
		

		numColums=len(registro)

	#print(len(miLista))
	#print(usuario)


	gv=gridview.MyForm(numColums,miLista)
	frame = gv.Show()
	app.MainLoop()

except TypeError:
	print("No se pueden sacar resultados")	
	wx.MessageBox('No se pueden sacar resultados', 'Informacion', 
    wx.OK | wx.ICON_INFORMATION)



