# import sounddevice
# from scipy.io.wavfile import write
#
# def savefile(sec):
#     print("start")
#     rece = sounddevice.rec((sec*44100),samplerate = 44100,channels=2)
#     sounddevice.wait()
#     write("demo.wav",44100,rece)
#     print("end")
# #
#
# savefile(10)


# import sounddevice
# from scipy.io.wavfile import write
# from tkinter import *
# from tkinter.messagebox import showinfo
# from tkinter.filedialog import askdirectory
#
# add = ""
#
# def file_path():
#     global add
#     add = askdirectory()
#
# def save_file():
#     try:
#         time = int(sec.get())
#         addr = add + "/" + "demo.wav"
#         showinfo(title="Start", message="Rec Start")
#         rece = sounddevice.rec(int(time * 44100), samplerate=44100, channels=2)
#         sounddevice.wait()
#         write(addr, 44100, rece)
#         showinfo(title="End", message="Rec End")
#     except:
#         showinfo(title="Time", message="Wrong Format Time")
#
# def main_window():
#     win = Tk()
#     win.geometry("500x600")
#     win.resizable(False,False)
#     win.title("Wscube Tech")
#     win.configure(bg="pink")
#
#     img1 = PhotoImage(file="my1.png")
#     l1 = Label(win, image=img1)
#     l1.place(x=50, y=20, height=200, width=400)
#
#     global sec
#     sec = Entry(win, font=("Times New Roman", 20))
#     sec.place(x=150, y=230, width=200)
#
#     l2 = Label(win, text="Time in sec", font=("Times New Roman", 20), bg="pink")
#     l2.place(x=100, y=290, height=50, width=300)
#
#     b = Button(win, text="path", font=("Times New Roman", 20), command=file_path)
#     b.place(x=150, y=350, height=50, width=200)
#
#     img2 = PhotoImage(file="my.png")
#     start = Button(win, image=img2, command=save_file)
#     start.place(x=200, y=420, height=100, width=100)
#
#     win.mainloop()
#
# if __name__ == "__main__":
#     main_window()


from tkinter import *
from tkinter import messagebox
import sounddevice                    #pip install sounddevice
from scipy.io.wavfile import write      #pip install scipy
import time
import wavio as wv                        #pip install wavio

def Record():
    freq = 44100
    dur = int(duration.get())
    recording=sounddevice.rec(dur*freq, samplerate=freq, channels=2)
    sounddevice.wait()

    #timer
    try:
        temp = int(duration.get())
    except:
        print("please enter the right value")

    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1
        if (temp==0):
            messagebox.showinfo("Time Countdown","Time's up")
        Label(text=f"{str(temp)}",font="arial 40",width=4,background="#4a4a4a").place(x=240,y=590)

    write("recording.wav",freq,recording)


root = Tk()
root.geometry("600x700+400+80")
root.resizable(False,False)
root.title("Voice Recording")
root.configure(background="pink")

#icon
image_icon=PhotoImage(file="Record.png")
root.iconphoto(False, image_icon)

#logo
photo=PhotoImage(file="Record.png")
myimage=Label(image=photo,background="#4a4a4a")
myimage.pack(padx=5,pady=5)

#name
Label(text="Voice Recorder", font="arial 30 bold", background="#4a4a4a", fg='white').pack()

#entry box
duration = StringVar()
entry = Entry(root,textvariable=duration,font="arial 30",background="#4a4a4a", fg="white")
entry.pack(pady=10)
Label(text="Enter time in seconds",font="arial 15",background="#4a4a4a",fg="white").pack()

#button
record = Button(root,font="Arial 20", text="Record",bg="#111111",fg="white",border=0,command=Record)
record.pack(pady=30)

root.mainloop()
