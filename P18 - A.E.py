#Andrew Espinoza
import tkinter as tk
window = tk.Tk()
window.title("Temperature Conversion")
window.geometry('800x800')

frame = tk.Frame(window, width=400, height=500, bd=2, relief= 'solid')
frame.place(x=200,y=100)

#--------functions--------
def calc():
    kelv = txt_kel.get()
    try:
        kelv = float(kelv)
        if kelv <= 0:
            txt_err.insert(0,'Number cannot be 0 or negative')
    except:       
           txt_err.insert(0,'Invalid Input') 
            
            
            
#---------labels--------
lbl_main = tk.Label(window, text= 'Temperature Converstion',font=('Arial',12,'bold'))
lbl_main.place(x=300,y=120)

lbl_kelvin = tk.Label(window, text= 'Kelvin:',font=('Arial',12,'bold'))
lbl_kelvin.place(x=220,y=190)

lbl_celsius = tk.Label(window, text= 'Celsius:',font=('Arial',12,'bold'))
lbl_celsius.place(x=220,y=260)

lbl_fahren = tk.Label(window, text= 'Fahrenheit:',font=('Arial',12,'bold'))
lbl_fahren.place(x=220,y=330)

#------txtbox-------
txt_kel = tk.Entry(window,font=('Arial',12,'bold'))
txt_kel.place(x=370, y=190)

txt_cel = tk.Entry(window,font=('Arial',12,'bold'))
txt_cel.place(x=370, y=260)

txt_fah = tk.Entry(window,font=('Arial',12,'bold'))
txt_fah.place(x=370, y=330)

txt_err = tk.Entry(window, width=40,font=('Arial',12,'bold'))
txt_err.place(x=260, y=400)

#-----buttons----
btn_calc = tk.Button(window, text='CALC',font=('Arial',12,'bold'),command= calc)
btn_calc.place(x=260,y=500)

btn_clr = tk.Button(window, text='CLEAR',font=('Arial',12,'bold'),command= 'clear')
btn_clr.place(x=460,y=500)




window.mainloop()
