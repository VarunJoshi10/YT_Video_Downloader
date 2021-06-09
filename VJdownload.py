from tkinter import *
from tkinter import filedialog, ttk
from tkinter import messagebox
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
import time
Folder_Name = ""
fileSizeInBytes = 0
MaxFileSize = 0


def downloadvd():
    global Folder_Name
    vdbtn['state'] = DISABLED
    vdbtn['text'] = "Please wait..."
    Folder_Name = filedialog.askdirectory()
    try:
        if (len(Folder_Name) > 1):
            locationError.config(text=Folder_Name, fg="green")

        else:
            locationError.config(text="Please Choose Folder!!", fg="red")

        choice = ytdchoices.get()
        url = ytdEntry.get()


        if (len(url) > 1):
            ytdError.config(text="")
            yt = YouTube(url,on_progress_callback=on_progress)

            if (choice == choices[0]):
                select = yt.streams.filter(progressive=True).first()

            elif (choice == choices[1]):
                select = yt.streams.filter(progressive=True, file_extension='mp4').last()

            elif (choice == choices[2]):
                select = yt.streams.filter(only_audio=True).first()

            else:
                ytdError.config(text="Paste Link again!!", fg="red")
        fileSizeInBytes = select.filesize
        MaxFileSize = fileSizeInBytes / 1024000
        MB = str(MaxFileSize) + " MB"
        print("File Size = {:00.00f} MB".format(MaxFileSize))
        print("Downloading Started")
        select.download(Folder_Name)
        messagebox.showinfo("download","Download Complete")
        vdbtn['state']=NORMAL
        vdbtn['text']="Download Video"
    except EXCEPTION as e:
        print("Error in download",e)


def downloadplay():
    global Folder_Name
    playbtn['state'] = DISABLED
    playbtn['text'] = "Please wait..."
    Folder_Name = filedialog.askdirectory()
    try:
        if (len(Folder_Name) > 1):
            locationError.config(text=Folder_Name, fg="green")

        else:
            locationError.config(text="Please Choose Folder!!", fg="red")

        url = playEntry.get()
        if (len(url) > 1):
            ytdError.config(text="")
            pl = Playlist(url)
            count=1
            for video in pl.videos:
                print("Downloading video:",count)
                select=video.streams.first()
                select.download(Folder_Name)
                count+=1
        messagebox.showinfo("Success", "Playlist Downloaded")
        playbtn['state']=NORMAL
        playbtn['text']="Download Playlist"
    except EXCEPTION as e:
        print("Error in download",e)


def button_exit():
    MsgBox = messagebox.askquestion(
        'Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo(
            'Return', 'You will now return to the application screen')
    return

#GUI

root =Tk()
root.title("YT Downloader")
root.geometry('350x400')
root.iconbitmap("./img/icon.ico")
im= PhotoImage(file="./img/play.png")
logoImage=Label(root,image=im)
logoImage.place(x=75,y=5)
jai=Label(root,text="YT Downloader",fg="red",font=("Arial",20,"bold"))
jai.place(x=75,y=70)
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.insert(0,"Enter Video URL")
ytdEntry.place(x=25,y=110)
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.insert(0,"Select Video Quality")
ytdchoices.place(x=100,y=140)
vdbtn=Button(root,text="Download Video",command=downloadvd,state=NORMAL)
vdbtn.place(x=125,y=170)
playEntryvar=StringVar()
playEntry=Entry(root,width=50,textvariable=playEntryvar)
playEntry.insert(0,"Enter Playlist URL")
playEntry.place(x=25,y=210)
playbtn=Button(root,text="Download Playlist",command=downloadplay,state=NORMAL)
playbtn.place(x=125,y=240)
locationError = Label(root,text=" ",fg="red",font=("jost",10))
locationError.place(x=125,y=270)
ytdError = Label(root,text=" ",fg="red",font=("jost",10))
ytdError.place(x=125,y=270)

button_exit = Button(
    root, text="EXIT",
    padx=30, pady=10,
    bg='red', fg="white", command=button_exit
)
button_exit.place(x=125,
                  y=300)
develop=Label(root,text="Developed by: Group No 4",bg="black",fg="white",font=("Arial",15,"bold"))
develop.place(x=50,y=360)
root.mainloop()
