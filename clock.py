from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("_SERGEANT_ O'Clock")
app_window.geometry("420x150")
app_window.resizable()

text_font= ("San-serif", 68, 'bold')
background = "#A3B95A"
foreground= "#AB6E32"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()