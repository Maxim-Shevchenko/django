import tkinter as tk
window=tk.Tk()
window.geometry("650x500")
window.title("Цветные фигуры")
def draw_circle():
    canvas.create_oval(200, 200, 220, 220, fill="black")
canvas=tk.Canvas(window,bg="white",width=500,height=500)
canvas.place(x=0, y=0)
button_circle=tk.Button(window,width=17,text="Нарисовать круг",command=draw_circle)
button_circle.place(x=503,y=464)
button_square=tk.Button(window,width=17,text="Нарисовать квадрат")
button_square.place(x=503,y=430)
button_romb=tk.Button(window,width=17,text="Нарисовать ромб")
button_romb.place(x=503,y=400)


window.mainloop()
