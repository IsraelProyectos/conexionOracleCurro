import wx
import wx.grid as gridlib
 
########################################################################
class MyForm(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self,numColumns,miLista):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Base de datos")
        panel = wx.Panel(self)
 
        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(500, numColumns)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)
        i=0
        
        for personaje in miLista:
            personaje=miLista[i]
            #print(len(personaje))
            y=0
            for datoPersonaje in personaje:
                #print(len(datoPersonaje))
                datosPersonaje=personaje[y]
                myGrid.SetCellValue(i, y, str(datoPersonaje))
                y = y+1
        
            #print(i)
            i = i+1

 
