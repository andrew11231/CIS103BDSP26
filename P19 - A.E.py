#Andrew Espinoza
import tkinter as tk
window = tk.Tk()
window.title("Program Graphics")
window.geometry('800x800')


canvas = tk.Canvas(window,width=800,height=800,bg='white')
canvas.place(x=0,y=0)


canvas.create_oval(150, 75,675,600, fill='', outline= 'lightgreen',width = 3)

canvas.create_oval(225, 150,375,300, fill='red',outline = '')

canvas.create_oval(450, 150,600,300, fill='blue',outline = '')

canvas.create_rectangle(300,370,525,405, fill = 'yellow', outline = '')

canvas.create_polygon(290,529,535,529,410,660, fill = '', outline = 'black', width = 34)



window.mainloop()
