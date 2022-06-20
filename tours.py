from tkinter import *
class Tours:
    country=''
    time=0
    price=''
    month=''

def die(): #закрытие окна графического интерфейса
    root.destroy()

def grafic(data):
    canv=Canvas(root, height=242, width=496, bg="white")
    canv.place(x=6,y=260) #поле для графика
    canv.create_line(40, 230, 40, 10, width=2, arrow=LAST)
    canv.create_line(10, 210, 480, 210, width=2, arrow=LAST)
    r=1
    for c in range(60,490,36): #цифры от 1 до 12 на графике
        canv.create_text(c, 220, text=r)
        r+=1
    data.sort()
    coords=[]
    for c in range(len(data)):
        coords.append([]) #вычисление координат
        coords[c].append(44+data[c][0]*30)
        coords[c].append(330-(data[c][1]/200))
    canv.create_line(coords)
    
def find():
    f=open(entr0.get(),'r')
    arr=f.readlines()
    ray=[]
    data=[]
    h=0
    for i in range(0,len(arr),5):
        ray.append([]) #
        for j in range(4):
            ray[h].append(arr[i+j]) #создание двумерного массива
            if i!=len(arr)-4 or j!=3:
                ray[h][j]=ray[h][j][:-1]
        h=h+1
    arr.clear() #очистка списка с неотсортированными данными
    
    def calc(): #вставка в виджет Label максимальной продожительности тура
        but2.config(state="disabled") 
        lb2.config(text=("Максимальная продолжительность тура (дни):"+str(maxT)))

    but2.config(command=calc)
    strana=entr1.get().capitalize()
    maxT=0
    txt.delete(0,1000) #очистка виджета Textbox
    for i in range(len(ray)):
        if ray[i][0]==strana:
            req=Tours #создание экземпляра класса
            req.country=ray[i][0]
            req.time=int(ray[i][1])
            req.price=ray[i][2]
            req.month=ray[i][3]
            arr.append(ray[i])
            if req.time>maxT: #определение максимальной продожительности тура
                maxT=req.time
    arr=sorted(arr, key=lambda stra: int(stra[1]))#сортировка по количеству дней
    txt.insert(END,"Список туров:")
    txt.insert(END,"____________________")
    if arr:
        v=0
        but2.config(state=NORMAL)
        for i in arr:
            txt.insert(END,"Дней:"+i[1])
            txt.insert(END,i[2])
            txt.insert(END,i[3])
            txt.insert(END,"____________________")
            
            data.append([])             #заполние двумерного списка
            data[v].append(int(i[1]))   #данными для построения графика
            data[v].append(int(i[2][:-6]))
            v+=1
        canv.destroy
        grafic(data)
           
    else:
        txt.insert(END,"Туры в данную")
        txt.insert(END,"страну отсутсвуют")
        but2.config(state="disabled")
        lb2.config(text="") #очистка виджета Label 
    arr.clear()

root=Tk()
root.title ("Получение сведений о маршрутах")
root.geometry("512x512")
root.configure(background="#1fa5ed")

entr0=Entry(font=("Arial",14))
entr0.place(x=173, y=24, width=122, height = 24)

lb3=Label(text="Введите имя файла:",font=("Arial",10), bg="#1fa5ed",fg="white")
lb3.place(x=174, y=3, width=122, height = 24)

but3=Button(text="Ввод", bg="lightgrey", command=find)
but3.place(x=259,y=50)

lb0=Label(text="Богданов М.Д. 19-ИЭ-1",font=("Arial",11),bg="white")
lb0.place(x=0, y=0)

lb1=Label(text="Введите страну",font=("Arial",12), bg="#1fa5ed",fg="white")
lb1.place(x=42, y=90, width=120, height = 24)

entr1=Entry(font=("Arial",14))
entr1.place(x=48, y=112, width=150, height = 24)

but0=Button(text="Завершить", bg="lightgrey",command=die)
but0.place(x=4,y=226)

but1=Button(text="Найти", bg="lightgrey",command=find)
but1.place(x=50,y=140)

but2=Button(text="Максимум", bg="lightgrey",state="disabled")
but2.place(x=100,y=140)

txt=Listbox(width=24, height=10, font=("Arial", 10))
txt.place(x=323,y=20)

lb2=Label(font=("Arial",10), wraplength=190, justify=LEFT, height=3, width=18)
lb2.place(x=323, y=194)

lb4=Label(text="График зависимости цены от времени:",font=("Arial",10),bg="#1fa5ed",fg="white")
lb4.place(x=85, y=240)

scroll=Scrollbar(command=txt.yview)
scroll.place(x=480, y=20, height=174)
txt.config(yscrollcommand=scroll.set)
canv=Canvas(root, height=242, width=496, bg="white")
canv.place(x=6,y=260) #поле для графика
root.mainloop()
