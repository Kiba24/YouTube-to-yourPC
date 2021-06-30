from tkinter import font
import pytube
import os
import tkinter as tk

#Función principal
def download_vid():
    video_url=entry_box.get()
    youtube_vid= pytube.YouTube(video_url)
    video = youtube_vid.streams.filter(only_audio=True).first()
    downloaded_file = video.download()
    base,ext = os.path.splitext(downloaded_file)
    new_file=base + ".mp3"
    os.rename(downloaded_file,new_file)
    print("Done")

def download_mp4():
    video_url=entry_box.get()
    youtube_vid= pytube.YouTube(video_url)
    video = youtube_vid.streams.filter(res="720p").first()
    downloaded_file = video.download()
    print("Done")

#Interfaz

#Definimos la ventana
window= tk.Tk()
window.geometry("600x300")
window.title("Youtube Vids to your PC")

#Label1
tag1= tk.Label(window, text="Conversor de Youtube a MP3/MP4")
tag1.config(fg="black", font=("Arial",20))
tag1.pack(padx=30,pady=30)

#Label2 - Entry
entry_box = tk.Entry(window,width=40)
entry_box.pack(padx=30,pady=10)

#Button y función
button=tk.Button(window, text="Convertir a MP3 - (Audio)", command=download_vid, bd=0 , background="lightblue" , font=("Arial",15))
button2=tk.Button(window, text="Convertir a MP4 - (Video)", command=download_mp4, bd=0 , background="lightblue" , font=("Arial",15))

button.pack(pady=30)
button2.pack()
#Label3
tag2= tk.Label(window, text= "Made by @Kiba24")
tag2.config(fg="black" , font=("Arial",12))
tag2.place(relx=0.75,rely=0.9)


window.mainloop()