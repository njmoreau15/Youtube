from pytube import YouTube
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter import filedialog

tk = Tk()

tk.title("YouTube Downloader") #sets window title
tk.geometry('500x300')         #sets window size


title = Label(tk,font="Arial 22 bold",text = "YOUTUBE VIDEO DOWNLOADER",background='red',foreground="white").place(x = 20, y = 10)


file_var = StringVar()
save_v_to = ""                                                      #init var as a string var to us in tkinter


def save_file():
    global save_v_to                                                              #func to select directory to save to
    file = file_var.get()
    file = filedialog.askdirectory(title = "Select File to Save To")
    file_var.set(file)  
    save_v_to = file
    print(save_v_to)                                                    #sets file var to the directory selected

#save file
file_path_label = Label(tk,font="Arial 12 bold", text = "Save file to...").place(x = 40, y = 90)  

save_button = Button(tk, text="Browse", command= save_file).place(x = 160, y = 90)

save_to = Label(tk , textvariable = file_var).place(x = 245, y = 90)

#-------------------------------------------------------------------------------------------------------------------------------------------------#
links = []
links2 = StringVar()
links2.set([]) #input list of urls

download_url = Label(tk,font="Arial 10 bold", text = "Input Download URL").place(x = 40, y = 135)  #label for Url download area
download_url_entry = Entry(tk, width = 47)
download_url_entry.place(x = 180, y = 135)                               # entry point of downloadable urls
download_list = Label(tk, textvariable = links2 ).place(x = 40, y = 155) # displays entered urls to download


def get_link(event):
     d_list =  download_url_entry.get()
     links2.set(links2.get() + d_list +"\n")
     links.append(d_list)

tk.bind('<Return>', get_link) # gives access to the enter key




close = Button(tk,text = "Close", command = tk.destroy)
close.place(x = 320,y = 270)
#save path


def download():

    print(save_v_to)
    for i in links: 
        try: 
              
        # object creation using YouTube
        # which was imported in the beginning 
            yt = YouTube(i)
            title = yt.title 
            print("Downloading " + yt.title)
            
        except: 
          
        #to handle exception 
            print("Connection Error") 
   

        try: 
        # downloading the video 
            yt.streams.get_highest_resolution().download(save_v_to) 
            print(title)
            print(save_v_to)
        except: 
            
            print("Cannot Download "+ title) 

    print('Task Completed!')

d_start = Button(tk, text = "Start Download", command = download )
d_start.place(x = 400,y = 270)

#download()
if __name__ == "__main__":
    tk.mainloop()