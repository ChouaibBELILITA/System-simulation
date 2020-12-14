from tkintertable.Tables import TableCanvas
from tkinter import *


def draw(tab_arrive,temps_file,temp_system):
    dictio={}
    j=0
    for i in range(len(tab_arrive)):
        dictio2={}
        dictio2["t_arrive"]='{:.4f}'.format(tab_arrive[i])
        dictio2["t_file"]='{:.4f}'.format(temps_file[i])
        dictio2["t_service"]='{:.4f}'.format(tab_arrive[i]+temps_file[i])
        dictio2["t_depart"]='{:.4f}'.format(tab_arrive[i]+temp_system[i])
        j=i+1
        dictio[j]=dictio2


    master = Tk()

    tframe = Frame(master)
    tframe.pack()
    table = TableCanvas(tframe)

    table = TableCanvas(tframe, data=dictio)

    model = table.model
    model.importDict(dictio)
    table.sortTable(columnName="t_arrive")
    table.show()
    master.mainloop()

