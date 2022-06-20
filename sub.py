from tkinter import *
class VUZ:
    predmet=''
    hours=0
    course=0
    vid=''

def die():
    root.destroy()

def grafic(data):
    canv=Canvas(root, height=242, width=496, bg="white")
    canv.place(x=20,y=320)
    lby1=Label(canv,text="экзамен",bg="lavenderblush")
    lby1.place(x=45,y=100)
    lby2=Label(canv,text="зачёт",bg="lavenderblush")
    lby2.place(x=45,y=50)
    lbx=Label(canv,text="кол-во часов",bg="lavenderblush")
    lbx.place(x=400,y=220)

    canv.create_line(40, 230, 40, 10, width=2, arrow=LAST)
    canv.create_line(10, 210, 480, 210, width=2, arrow=LAST)
    data.sort()
    coords=[]
    for c in range(len(data)):
        coords.append([])
        coords[c].append(((data[c][0])-50)*3+20)
        if data[c][1]=="зачет":
            coords[c].append(60)
        else: coords[c].append(110)
    canv.create_line(coords)
    
def find():
    def calc():
        lb2.config(text=("Часов в курсе: "+str(sumHours)))
        
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
    but2.config(command=calc)
    kurs=entr1.get()
    if kurs=="":
        kurs=-1
    sumHours=0
    txt.delete(0,1000) #очистка виджета Textbox
    for i in range(len(ray)):
        if int(ray[i][2])==int(kurs):
            req=VUZ #создание экземпляра класса
            req.predmet=ray[i][0]
            req.hours=int(ray[i][1])
            req.course=int(ray[i][2])
            req.vid=ray[i][3]
            arr.append(ray[i])
            sumHours+=req.hours
    arr=sorted(arr, key=lambda stra: int(stra[1]))#сортировка по часам
    txt.insert(END,"Список дисциплин:")
    txt.insert(END,"_________________")
    if arr:
        v=0
        for i in arr:
            txt.insert(END,i[0])
            txt.insert(END,"Часов: "+i[1])
            txt.insert(END,"Вид отчётности: "+i[3])
            txt.insert(END,"_________________")

            data.append([])
            data[v].append(int(i[1]))
            data[v].append(i[3])
            v+=1
        root.geometry("550x600")
        canv.destroy
        grafic(data)
           
    else:
        txt.insert(END,"Некорректное")
        txt.insert(END,"значение")
        lb2.config(text="")
    arr.clear()

root=Tk()
root.title ("Получение сведений о дисциплинах")
root.geometry("550x300")
root.configure(background="RosyBrown1")

entr0=Entry(font=("Arial",14),bg="lavenderblush")
entr0.place(x=60, y=45, width=120, height = 23)
entr0.focus()

lb3=Label(text="Файл:",font=("Arial",14), bg="pink2")
lb3.place(x=5, y=40)

but3=Button(text="Ввод", bg="steelblue", fg="lavenderblush", command=find)
but3.place(x=200,y=44,width=45)

lb0=Label(text="Комарова Дарья Алексеевна 19-ИЭ-1",font=("Arial",14),bg="pink2")
lb0.place(x=5, y=5)

lb1=Label(text="Введите курс:",font=("Arial",16), bg="pink2",)
lb1.place(x=5, y=110)

entr1=Entry(font=("Arial",16),bg="lavenderblush")
entr1.place(x=10, y=140, width=20, height = 24)

but0=Button(text="Выйти", bg="steelblue",fg="lavenderblush",command=die)
but0.place(x=5,y=240)

but1=Button(text="Найти", bg="steelblue",command=find,fg="lavenderblush")
but1.place(x=40,y=140)

but2=Button(text="Всего",height=3,bg="steelblue",fg="lavenderblush")
but2.place(x=280,y=240)

txt=Listbox(width=20, height=10, font=("Arial", 12),bg="lavenderblush")
txt.place(x=320,y=35)

lb2=Label(font=("Arial",12), wraplength=190, justify=LEFT, height=3,width=20,bg="lavenderblush")
lb2.place(x=322, y=229)

lb4=Label(text="График зависимости кол-ва часов от вида отчётности:",font=("Arial",12),bg="pink2")
lb4.place(x=600, y=15)

scroll=Scrollbar(command=txt.yview)
scroll.place(x=504, y=35, height=194)

txt.config(yscrollcommand=scroll.set)
canv=Canvas(root, height=242, width=496, bg="lavenderblush")
root.mainloop()
