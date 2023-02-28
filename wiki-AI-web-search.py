from tkinter import *
from tkinter import messagebox
import pyttsx3
import wikipedia

app = Tk()
app.geometry('500x430')
app.title('Wiki-Ai Web Search')

def search():
	if (len(entry.get()) != 0):			
		try:		
			type = entry.get()
			result = wikipedia.summary(type, sentences = 2) 
			con.insert(INSERT, result)
			print(result)
			engine = pyttsx3.init()
			voices = engine.getProperty("voices")
			engine.setProperty('voice', voices[0].id)
			rate = engine.getProperty('rate')
			print (rate)                   
			engine.setProperty('rate', 120)
			engine.say(result)
			engine.runAndWait()

		except Exception as e:
			raise messagebox.showinfo(title='Warning message',message='This query not found, Try another query !')
	else:
		messagebox.showinfo(title='Warning message',message='Search bar is empty !')

def clear():
	entry.delete(0 ,END)
	con.delete("1.0",END)

def repeat():
	if (len(con.get("1.0",END)) != 0):
		data = con.get("1.0",END)
		engine = pyttsx3.init()
		voices = engine.getProperty("voices")
		engine.setProperty('voice', voices[0].id)
		engine.say(data)
		engine.runAndWait()

imgicon = PhotoImage(file="wiki.png")
imglabel = Label(app,image=imgicon)
imglabel.place(x=60,y=5)

titlelabel = Label(app,text='Wiki-Ai Web Search',fg='black',font='Consolas 17 bold')
titlelabel.place(x=140,y=7)

label = Label(app,text='Search your query',fg='black',font='Consolas 10 bold')
label.place(x=10,y=100)

entry = Entry(app,fg='red',font='Consolas 10')
entry.place(x=200,y=102)

button = Button(app,text='Search',bg='grey',fg='black',font='Consolas 10 bold',command=search)
button.place(x=410,y=95)

con = Text(app,height=11,width=57,bd=1,fg='black',font='Consolas 9 bold',wrap=WORD)
con.place(x=16,y=170)

button3 = Button(app,text='Clear',bg='grey',fg='black',font='Consolas 10 bold',command=clear)
button3.place(x=16,y=380)

button2 = Button(app,text='Repeat',bg='grey',fg='black',font='Consolas 10 bold',command=repeat)
button2.place(x=410,y=380)


app.mainloop()