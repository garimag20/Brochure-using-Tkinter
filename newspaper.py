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
Heading = Label(text="Delhi Times", font="Elephant 30 bold", bg="black",
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


# Right Text-2
T2 = Label(text='''A recognised UNESCO World Heritage Site, the Qutub Minar is one of the tallest minars of India. In fact, it has been recognised 
as the tallest minar of India! The striking monument in Delhi is constructed out of red sandstone and marble. It is actually one of the 
highlights of some of the monuments in Delhi. Most of them come with a red sandstone appeal that derives strength and robust nature. ''', bg="black", fg="white", padx=5, pady=5)
T2.place(x=380, y=180)
T3 = Label(text='''Built as a war memorial for the 70,000 soldiers of the British Indian Army who sacrificed their lives in World War I, India Gate was 
built in Delhi's Janpat neighbourhood.Built atop a black marble plinth, with reversed rifle and capped with a war helmet bounded by four 
eternal flames beneath the Memorial archway is the Amar Jawan Jyoti, which also holds a very important message.''', bg="black", fg="white",padx = 5, pady=5)
T3.place(x=380, y=240)
T4 = Label(text='''Just as the name suggests, the exteriors of the historical monument Red Fort in Delhi is painted in red and is practically a fort. It was built 
by Shah Jahan and was even considered as the political center for quite some time. With lush greenery and such historical values, 
you would be amazed by Red Fort, for sure!''', bg="black", fg="white",padx = 5, pady=5)
T4.place(x=380, y=300)
T5 = Label(text='''The ancient astronomical instrument Jantar Mantar was constructed by Maharaja Jai Singh of Jaipur.Basically, based on the position of the 
ṇsun during the day, one can speculate the time. The monument has had very insightful roles to play in the past and is of prime 
importance to the history of India and Delhi. ''', bg="black", fg="white",padx = 5, pady=5)
T5.place(x=380, y=360)
# image
photo1 = PhotoImage(file="news2.png")
P2 = Label(image=photo1)
P2.place(x=50, y=170)

root.mainloop()
