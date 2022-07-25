import tkinter as tk

'''
#F3E9D2 - Egg
#C6DABF - Tea
#88D498 - Apple
#1A936F - Emerald
#114B5F - Blue
'''

wn = tk.Tk()
wn.title("Snake")

canvas = tk.Canvas(height=400,width=400)
canvas.pack()

big_frame = tk.Frame(height=300,width=300,bg='#114B5F')
big_frame.place(relheight=1, relwidth=1)

little_frame = tk.Frame(height=300,width=300,bg='#1A936F')
little_frame.place(rely=0.05,relx=0.05, relheight=0.9, relwidth=0.9)

wn.mainloop()