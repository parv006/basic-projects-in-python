import tkinter as tk
win=tk.Tk()
win.title('km to miles converter')
win.minsize(width=300,height=300)
win.config(padx=0, pady=30, background='')
ans=tk.Label(text='miles=0')
ans.pack(side='bottom')
def conv():
    x=inpu.get()
    x=float(x)
    mile=x*0.621371
    ans.config(text=f'miles={mile}')

lab=tk.Label(text='enter the km here ⬇️⬇️ ')
lab.pack()

button=tk.Button(text='calc', command=conv )
button.place(x=140,y=150)

inpu=tk.Entry()
inpu.place(x=100,y=50)



win.mainloop()
