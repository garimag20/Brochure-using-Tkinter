from os import pathsep
from tkinter import *

root = Tk()

# Title of the application
root.title("First Project Using Tkinter")

# Window Size
root.geometry("1110x790")
root.minsize(1110, 790)
root.maxsize(1110, 790)

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


#Left text-2
T6 = Label(text="""Janpath and Tibetan Market is a very popular and lively Delhi market has something for everyone. You'll find goods 
from everywhere in India and Tibet here.""", bg="black", fg="white",padx = 5, pady=5)
T6.place(x=50, y = 455)
T7 = Label(text="""The shopping district of Chandni Chowk has been in existence for hundreds of years. The lanes of Chandni Chowk 
are divided into bazaars with different areas of specialization.""", bg="black", fg="white",padx = 7, pady=5)
T7.place(x=50, y = 500)
T8 = Label(text="""Sarojini Nagar is most famous for its really cheap designer clothes and reputable brands that have been rejected from 
export, either because of surplus quantity or small manufacturing defects.""", bg="black", fg="white",padx = 5, pady=5)
T8.place(x=50, y = 545)
T9 = Label(text="""Khan Market is a small U-shaped market that's one of Delhi's classiest. Bargain hunters are likely to be disappointed 
at this market. It's got a loyal following who go there to shop at its branded outlets.""", bg="black", fg="white",padx = 5, pady=5)
T9.place(x=50, y = 590)
T10 = Label(text="""The hectic Lajpat Nagar market provides an interesting glimpse into Indian culture. It's one of the oldest markets in 
India and is abuzz with middle-class Indian shoppers, all swarming around its roadside stalls and showrooms. """, bg="black", fg="white",padx = 5, pady=5)
T10.place(x=50, y = 635)
T11 = Label(text="""Meena Bazaar is historic market, which lines passageway into the Red Fort, used to house the most exclusive royal 
tailors and merchants in the 17th century. It's one of the oldest markets in the city.""", bg="black", fg="white",padx = 7, pady=5)
T11.place(x=50, y = 680)
# image
photo2 = PhotoImage(file="news3.png")
P3 = Label(image=photo2)
P3.place(x=670, y=440)
root.mainloop()
