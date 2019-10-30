from tkinter import Label, Entry, Button, Tk, Frame
import re

def get_mail(email, root): 
    if not re.match(r'\S+@\S+', email):
        error = Label(root, text="e n t e r   a   v a l i d   e m a i l   a d d r e s s *", font=("Helvetica", 10, "italic"), fg="red", bg="#090b10")
        error.place(x=302, y=340)
    else:
        with open("user_mail.zxt", 'w') as f:
            f.write(email)
        cover = Frame(t, width=900, height=500, bg="#090b10")    
        cover.place(x=0,y=0)
        ack = Label(root, text="y o u   c a n   n o w   r u n   t h e   m a i n   f i l e :)", font=("Helvetica", 10, "italic"), fg="#2df0a0", bg="#090b10")
        ack.place(x=300, y=200)

t = Tk()
t.geometry('900x500')
t.config(bg='#090b10')

frame_insert = Frame(t, height="15", width="80", bd=2,
                     bg="#2df0a0", highlightbackground="#090b10")
insert_new = Entry(frame_insert, width="50", font=("Helvetica", 13), bg="#090b10",
                   fg="#2df0a0", bd="4", relief="flat", insertbackground="#2df0a0")
frame_insert.place(x=200, y=230)
insert_new.grid(column=2)

l1 = Label(t, text="E n t e r   E - M a i l   t o   r e c i e v e   N o t i f i c a t i o n",
           font=("Helvetica", 12), fg="#2df0a0", bg="#090b10")
l1.place(x=240, y=190)

l2 = Label(t, text="c u r r e n t l y   w o r k s   o n   f l i p k a r t   p r o d u c t s   o n l y   o t h e r   s i t e s   w i l l   b e   a d d e d   s o o n",
           font=("Helvetica", 8), fg="#2df0a0", bg="#090b10")
l2.place(x=150, y=400)


submit2 = Button(t, text="s u b m i t   e - m a i l", width="55", height="1", font=("Helvetica", 10, "bold"), fg="#090b10", bg="#2df0a0", activebackground="#1a1a1a",
                 activeforeground="#8fdcdf", command=lambda: get_mail(insert_new.get(), t))
submit2.config(highlightbackground="#8fdcdf",
               highlightcolor="#2df0a0", highlightthickness=10, relief="solid")
submit2.place(x=198, y=280)


t.mainloop()
