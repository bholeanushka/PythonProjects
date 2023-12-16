window=Tk()
window.title("Guessing Game")
window.minsize(300,300)
window.config(bg='pink')

global random_num
random_num=random.randint(1,10)

lbl=Label(window,text="Welcome to guessing game",font=("Garamond",20))
lbl.pack(ipadx=100,pady=10)
entry=Entry(window,width=20)
entry.insert(0,"Enter the guess")
entry.pack(pady=10)
entry.bind("<FocusIn>",clear_text)

bt = Button(window,text="Submit",command=get_value)
bt.pack(pady=10)

result="Result Will be displayed here !"
resultlabel=Label(window,text=result,font=("Garamond",15))
resultlabel.pack(pady=10)
window.mainloop()
