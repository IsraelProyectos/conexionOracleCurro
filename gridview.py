import wx
import wx.grid as gridlib

class MyForm(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self,numColumns,miLista):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Base de datos")
        panel = wx.Panel(self)
        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(len(miLista), numColumns)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)
        i=0
        
        for registro in miLista:
            #registro=miLista[i]
            #print(len(registro))
            y=0
            for datoPersonaje in registro:
                #print(len(datoPersonaje))
                #datosPersonaje=registro[y]
                datoPersonaje=str(datoPersonaje)
                datoPersonaje = unicode(datoPersonaje, "ISO-8859-1")
                myGrid.SetCellValue(i, y, datoPersonaje)
                
                y = y+1
        
            #print(i)
            i = i+1

 
