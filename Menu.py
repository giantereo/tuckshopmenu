Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import*

#main page
mainpage = Tk()
mainpage.title("Sacred Heart College Tuck Shop")
mainpage.geometry("600x600+0+0")
labell = Label(mainpage, bg = "snow", fg = "midnight blue", padx = 30, pady = 10,
               text = "Tuck Shop", font = ("helvetica","24", "bold"))
labell.pack()
mainpage.mainloop()
#code in the main page
mainpage.mainloop()
