from tkinter import *

ws = Tk()
ws.title('Assignment #2')
ws.geometry('300x275')

frame1 = Frame(ws, padx=5, pady=5)
frame1.grid(row=0, column=1,)

Label(frame1, text='What is your name?', padx=5, pady=5).pack()
Label(frame1, text='How old are you?', padx=5, pady=5).pack()
Label(frame1, text='Where do you live?', padx=5, pady=5).pack()
 

frame2 = Frame(ws, padx=5, pady=5)
frame2.grid(row=0, column=2)

Entry(frame2).pack(padx=5, pady=5)
Entry(frame2).pack(padx=5, pady=5)
Entry(frame2).pack(padx=5, pady=5)


Button(ws, text='DONE!', padx=10).grid(row=1, columnspan=5, pady=5)


ws.mainloop()
