from tkinter import *
from tkinter import messagebox
import time
import threading
from pygame import mixer
import datetime
root = Tk()
root.title("Alarm")
root.geometry("600x350")
root.configure(bg="#F0F0F0")  # Set background color

mixer.init()

def th():
    t1 = threading.Thread(target=a, args=())
    t1.start()

def a():
    alarm_time_str = hr.get()

    try:
        # Parse the user input to create a datetime object
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
    except ValueError:
        messagebox.showerror('Invalid data', 'Please enter a valid time in HH:MM format')
        return

    while datetime.datetime.now().strftime("%H:%M") != alarm_time.strftime("%H:%M"):
        # Wait until the current time matches the alarm time
        time.sleep(1)

    mixer.music.load('alarm.mp3')
    mixer.music.play()
    msg = messagebox.showinfo('It is time', f'{amsg.get()}')
    if msg == 'ok':
        mixer.music.stop()


header = Frame(root, bg="#2E3B4E")  
header.place(x=5, y=5)

head = Label(header, text="ALARM CLOCK", font=('comic sans', 24, 'bold'), fg="white", bg="#2E3B4E") 
head.pack(fill=X)

panel = Frame(root, bg="#F0F0F0") 
panel.place(x=5, y=70)

alpp = PhotoImage(file='clk3.png')

alp = Label(panel, image=alpp, bg="#F0F0F0")
alp.grid(rowspan=4, column=0)

atime = Label(panel, text="Alarm Time (Hr:Min)", font=('comic sans', 18), bg="#F0F0F0")
atime.grid(row=0, column=1, padx=10, pady=5)

hr = Entry(panel, font=('comic sans', 20), width=5, bd=2, relief=SOLID)
hr.grid(row=0, column=2, padx=10, pady=5)

amessage = Label(panel, text="Message", font=('comic sans', 20), bg="#F0F0F0")
amessage.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

amsg = Entry(panel, font=('comic sans', 15), width=25, bd=2, relief=SOLID)
amsg.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

start = Button(panel, text="Start Alarm", font=('comic sans', 18), command=th, bg="#4CAF50", fg="white")  # Set button color
start.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

root.mainloop()

