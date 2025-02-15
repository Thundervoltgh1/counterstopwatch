from tkinter import*
from time import*
from time import sleep
root=Tk()
root.geometry("500x500")
root.title("Stop watch")
hour=StringVar()
hour.set("00")
min=StringVar()
min.set("00")
sec=StringVar()
sec.set("00")
def g():
    try:
        j=int(hour.get())*3600+int(min.get())*60+int(sec.get())*1
    except:
        print("Please input the right value")
    while j>-1:
        mins,secs= divmod(j,60)#divmod helps us to store quotient and remainder of the division
        hours=00
        if mins>60:
            hours,min=divmod(min,60)
        hour.set("{00:2d}".format(hours))
        min.set("{00:2d}".format(mins))
        sec.set("{00:2d}".format(secs))
        root.update()
        time.sleep(1)

hourentry=Entry(root,width=3,font=("Arial",25,""),textvariable=hour)
minentry=Entry(root,width=3,font=("Arial",25,""),textvariable=min)
secentry=Entry(root,width=3,font=("Arial",25,""),textvariable=sec)
hourentry.place(x=100,y=100)
minentry.place(x=150,y=100)
secentry.place(x=200,y=100)
d=Button(root,text="Set your time",bd='5',command=g)
d.place(x=150,y=200)
root.mainloop()