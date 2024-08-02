# import tkinter
# from tkinter import messagebox
# app=tkinter.Tk()
# def data():
#     if v_c1.get()==1:
#         print("mal")
#     if v_c2.get()==1:
#         print("eng")
#     print(vr1.get())
#     # messagebox.askretrycancel("display",v1.get())
#     # messagebox.askokcancel("display",v1.get())
#     # messagebox.showinfo("display",v1.get())
#     # l2.config(text=v1.get())
# app.title("synnefo")
# app.minsize(400,400)
# app.maxsize(600,600)
# app.config(bg="blue")
# l1=tkinter.Label(app,text="welcome",bg="blue",fg="black")
# l1.pack()
# v1=tkinter.StringVar()
# e1=tkinter.Entry(app,textvariable=v1)
# e1.pack()
# v_c1=tkinter.IntVar()
# v_c2=tkinter.IntVar()
# c1=tkinter.Checkbutton(app,text="mal",variable=v_c1)
# c1.pack()
# c2=tkinter.Checkbutton(app,text="eng",variable=v_c2)
# c2.pack()
# vr1=tkinter.IntVar()
# r1=tkinter.Radiobutton(app,text="male",value=1,variable=vr1)
# r2=tkinter.Radiobutton(app,text="female",value=2,variable=vr1)
# r1.pack()
# r2.pack()
# b1=tkinter.Button(app,text="save",bg="black",fg="white",activebackground="red",activeforeground="black",padx=8,pady=5,command=data)
# b1.pack()
# l2=tkinter.Label(app)
# l2.pack()
# app.mainloop()




import tkinter
app=tkinter.Tk()
c=tkinter.Canvas(app,width=400,height=400,bg="blue")
c.create_line(0,150,350,150)
c.create_rectangle(100,100,350,350,fill="white")
c.create_oval(100,100,350,350,fill="red")
c.pack()
app.mainloop()
