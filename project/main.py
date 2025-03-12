from PIL import Image,ImageTk
import tkinter as tk
def answer(canvas):
    city = textField.get()
    if city == '1':
      import Api
    elif city == '2':
        import rainfall
        rainfall.possible_rain()
    elif city == '3':
        import rainfall
        rainfall.analyze()
if __name__ == "__main__":
    canvas = tk.Tk()
    canvas.title("Weather App")
    canvas.configure(bg='#6b8e23')
    f = ("poppins", 15, "bold")
    t = ("poppins", 35, "bold")
    label1 = tk.Label(canvas,borderwidth = 1,font=f)
    label1.pack()
    title = "\n" + "WEATHER REPORT " + "\n"
    swi	=	"\n"	+ "***********************************************************************"
    switch = title + swi + "\n" + "1:Current weather report for specific city " + "\n" + swi + "\n" + "2:Do you need to predict rainfall tomorrow?" + "\n" + swi + "\n"+ "3:Analyze the avarage rainfall every month for india"
    label1.config(text = switch,foreground = "white",bg="#6b8e23") 
    textField = tk.Entry(canvas, justify='center', width = 20, font = t, foreground="red")
    textField.configure(bg="#C04000", insertbackground='black')
    textField.pack(pady = 20)
    textField.focus()
    textField.bind('<Return>', answer)
    #label2 = tk.Label(canvas, font=f)
    #label2.pack() [139]
    canvas.mainloop()


