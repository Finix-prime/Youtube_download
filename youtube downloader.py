from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from pytube import YouTube
from pytube import Playlist
#from pydub import AudioSegment
import ffmpeg
import os

path = "youtube_downloader"

def progressfuction(stream, chunk, bytes_remaining):
    size = stream.filesize
    live = 100-(int((bytes_remaining/size)*100))
    print("downloading",live,"%")
    if live == 0:
        progress['value'] = 5
        frame.update_idletasks()
    if live == 20:
        progress['value'] = 15
        frame.update_idletasks()
    if live == 40:
        progress['value'] = 35
        frame.update_idletasks()
    if live == 60:
        progress['value'] = 55
        frame.update_idletasks()
    if live == 80:
        progress['value'] = 75
        frame.update_idletasks()
    if live == 100:
        progress['value'] = 99
        frame.update_idletasks()


def getmp3(e):
    global recently
    global url
    but2["state"] = DISABLED
    ent1.set = ""
    e = url
    if len(url) > 0:
        yt = YouTube(e)
        video = yt.streams.filter(only_audio=True).first()
        destination = path
        yt.register_on_progress_callback(progressfuction)
        track = video.download(output_path=destination,filename=yt.title)
        newfile = os.path.splitext(track)[0] +".mp3"
        os.rename(track,newfile)
        # sound = AudioSegment.from_file(newfile,format="mp4")
        # sound.export(newfile, format="mp3")
        print(newfile)
        recently = newfile.title()
        lab4["text"] = str(recently)
        print("Complete",recently)
        messagebox.showinfo("Alert", "Download Complete")
        progress['value'] = 0
        frame.update_idletasks()
    else:
        messagebox.showinfo("Alert", "Please save link before download")

def getvideo(e):
    global recently
    global url
    but1["state"] = DISABLED
    ent1.set = ""
    e = url
    if len(url) > 0:
        yt = YouTube(e)
        video = yt.streams.filter().first()
        destination = path
        yt.register_on_progress_callback(progressfuction)
        track = video.download(output_path=destination)
        recently = track.title()
        lab4["text"] = str(recently)
        print("Complete",recently)
        messagebox.showinfo("Alert", "Download Complete")
    else:
        messagebox.showinfo("Alert", "Please save link before download")


def geturl(e):
    global url
    url = e.widget.get()
    ent1["state"] = NORMAL
    but1["state"] = NORMAL
    but2["state"] = NORMAL
    print(url)

recently = ""
url = ""

root = Tk()
root.title("Youtube Downloader by fenix")
root.geometry("750x300")
root.option_add("*Font","tahoma 18")
root.maxsize(width=750,height=300)
root.minsize(width=750,height=300)
frame =Frame(root)
frame.pack()
space1 = Label(frame,text= "press Enter to save URL before download",foreground="red")
space1.grid(column=0,row=0,columnspan=2)
lab1 = Label(frame,text="URL",foreground="green")
lab1.grid(column=0,row=1)
ent1 = Entry(frame,width=30)
ent1.grid(column=1,row=1)
ent1.bind("<Return>", geturl)
space2 = Label(frame)
space2.grid(column=0,row=2,columnspan=2)
but1 = Button(frame,text="Download Video",width=20,state=DISABLED)
but1.grid(column=0,row=3)
but1.bind("<Button-1>", getvideo)
but2 = Button(frame,width=20,text='Download MP3',state=DISABLED)
but2.grid(column=1,row=3)
but2.bind("<Button-1>", getmp3)
space3 = Label(frame)
space3.grid(column=0,row=4,columnspan=2)
lab3 = Label(frame,text="Recently Download")
lab3.grid(column=0,row=5)
lab4 = Label(frame,background="white",foreground="black",text="",width=100,font="tahoma 10")
lab4.grid(column=0,row=6,padx=5,columnspan=2)
lab5 = Label(frame,text="progressing download ")
lab5.grid(column=0,row=7)
progress = Progressbar(frame,length=300, orient=HORIZONTAL, mode='determinate')
progress.grid(column=1,row=7)

ent1.focus_set()
root.mainloop()
