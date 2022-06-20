from tkinter import *
class Auto:
    mark=''
    country=''
    year=0
    price=0

def die(): #закрытие окна графического интерфейса
    root.destroy()

def grafic(data):
    canv=Canvas(root, height=242, width=496, bg="white")
    canv.place(x=550,y=40) #поле для графика
    lby=Label(canv,text="Цена")
    lby.place(x=460,y=217)
    lbx=Label(canv,text="Год выпуска")
    lbx.place(x=45,y=10)

    
    canv.create_line(40, 230, 40, 10, width=2, arrow=LAST)
    canv.create_line(10, 210, 480, 210, width=2, arrow=LAST)
    data.sort()
    coords=[]
    for c in range(len(data)):
        coords.append([]) #вычисление координат
        coords[c].append((data[c][0]-2000)*25)
        coords[c].append((data[c][1])/30000)
    canv.create_line(coords)
    
def find():
    f=open(entr0.get(),'r')
    arr=f.readlines()
    ray=[]
    data=[]
    h=0
    for i in range(0,len(arr),5):
        ray.append([])
        for j in range(4):
            ray[h].append(arr[i+j]) #создание двумерного массива
            if i!=len(arr)-4 or j!=3:
                ray[h][j]=ray[h][j][:-1]
        h=h+1
    arr.clear() #очистка списка с неотсортированными данными
    
    def calc():
        but2.config(state="disabled") 
        lb2.config(text=("Самый новый автомобиль: \n"+str(maxM)))
    but2.config(command=calc)
    avto=entr1.get()
    if avto=="":
        avto=-1
    maxY=0
    maxM=''
    txt.delete(0,1000) #очистка виджета Textbox
    for i in range(len(ray)):
        if int(ray[i][3])<=int(avto):
            req=Auto #создание экземпляра класса
            req.mark=ray[i][0]
            req.country=ray[i][1]
            req.year=int(ray[i][2])
            req.price=int(ray[i][3])
            arr.append(ray[i])
            if req.year>maxY: #определение самого нового авто
                maxY=req.price
                maxM=req.mark
    arr=sorted(arr, key=lambda stra: int(stra[3]))#сортировка по цене
    txt.insert(END,"Список автомобилей:")
    txt.insert(END,"_________________")
    if arr:
        v=0
        but2.config(state=NORMAL)
        for i in arr:
            txt.insert(END,i[0])
            txt.insert(END,i[1])
            txt.insert(END,i[2]+" г")
            txt.insert(END,i[3]+" руб.")
            txt.insert(END,"_________________")
            
            data.append([])             #заполние двумерного списка
            data[v].append(int(i[2]))   #данными для построения графика
            data[v].append(int(i[3]))
            v+=1
        root.geometry("1070x300")
        canv.destroy
        grafic(data)
           
    else:
        txt.insert(END,"Вы ввели некорректное")
        txt.insert(END,"значение")
        but2.config(state="disabled")
        lb2.config(text="") #очистка виджета Label 
    arr.clear()

root=Tk()
root.title ("Получение сведений об автомобилях")
root.resizable(0,0)
root.geometry("550x300")
root.configure(background="orange")

entr0=Entry(font=("Arial",14))
entr0.place(x=60, y=45, width=120, height = 23)
entr0.focus()

lb3=Label(text="Файл:",font=("Arial",14), bg="orange")
lb3.place(x=5, y=40)

but3=Button(text="Ввод", bg="bisque", command=find)
but3.place(x=200,y=44,width=45)

lb0=Label(text="Кошевой Дмитрий Андреевич 19-ИЭ-1",font=("Arial",14),bg="orange")
lb0.place(x=5, y=5)

lb1=Label(text="Введите стоимость:",font=("Arial 14 underline"), bg="orange",)
lb1.place(x=5, y=90)

entr1=Entry(font=("Arial",14))
entr1.place(x=5, y=120, width=120, height = 24)

but0=Button(text="Завершить", bg="bisque",command=die)
but0.place(x=5,y=240)

but1=Button(text="Найти", bg="bisque",command=find)
but1.place(x=10,y=150,width=50)

but2=Button(text="Максимум", bg="bisque",state="disabled")
but2.place(x=70,y=150)

txt=Listbox(width=20, height=10, font=("Arial", 12),bg="white")
txt.place(x=320,y=35)

lb2=Label(font=("Arial",10), wraplength=190, justify=LEFT, height=3, width=23)
lb2.place(x=320, y=229)

lb4=Label(text="График зависимости стоимости от года выпуска:",font=("Arial",12),bg="orange")
lb4.place(x=610, y=15)

lb5=Label(text="руб.",font=("Arial",14),bg="orange")
lb5.place(x=130,y=115)

scroll=Scrollbar(command=txt.yview)
scroll.place(x=504, y=35, height=194)

txt.config(yscrollcommand=scroll.set)
canv=Canvas(root, height=242, width=496,bg="white")
canv.place(x=550,y=40)
root.mainloop()
