import wx
import wx.grid as gridlib
import gridview

personaje=2

app = wx.PySimpleApp()

gf=gridview.MyForm(personaje)

frame = gf.Show()
app.MainLoop()

