from os import pathsep
from tkinter import *

root = Tk()

# Title of the application
root.title("First Project Using Tkinter")

# Window Size
root.geometry("1110x850")
root.minsize(1110, 850)
root.maxsize(1110, 850)

# Heading
Heading = Label(text="Daily Times", font="Elephant 30 bold", bg="black",
                fg="white", borderwidth=3, padx=5, pady=5, relief=SUNKEN)
Heading.pack(fill=X)

# Date
Date = Label(text="Date:-04.10.2021", bg="black", fg="white",
             borderwidth=3, padx=5, pady=5, relief=SUNKEN)
Date.place(x=1000, y=70)

# Left text-1
T1 = Label(text="""Delhi is of great historical significance as an important commercial, transport, and cultural hub, as well as the political
centre of India. One of the country’s largest urban agglomerations, Delhi sits astride (but primarily on the west bank of) 
the Yamuna River, a tributary of the Ganges (Ganga) River, about 100 miles (160 km) south of the Himalayas.""" ,bg="black", fg="white", padx=5, pady=5)
T1.place(x=50, y=100)
#Image
photo = PhotoImage(file="news1.png")
P1 = Label(image = photo)
P1.place(x=700, y=70)

root.mainloop()
