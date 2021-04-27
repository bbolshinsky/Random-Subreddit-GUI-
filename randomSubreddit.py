import tkinter as tk
from tkinter import filedialog, Text
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

root = tk.Tk()
root.title("Random sub-reddit")
subReddits=[]

# GUI frame
canvas = tk.Canvas(root, height = 500, width = 600, bg="#263D42" )
canvas.pack()
frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.85, relheight = 0.75, relx = 0.075, rely = 0.05)

# Open random subreddit
def website():
    for widget in frame.winfo_children():
        widget.destroy()
    driver = webdriver.Chrome()
    driver.get("https://www.reddit.com/r/random")
    subReddit = "r/"+driver.title 
    subReddits.append(subReddit)
    for i in subReddits:
        label = tk.Label(frame, text=i,bg = "white")
        label.pack()
    
openReddit = tk.Button(root, text = "Open Reddit", padx = 10, pady =5, fg = "teal", bg = "#263D42", command=website)
openReddit.pack()

# Close Tkinter Window 
def closeWindow(): 
    root.quit()
closeWindow = tk.Button(root,text = "Close Window", padx = 10, pady =5, fg = "teal", bg = "#263D42", command = closeWindow)
closeWindow.pack()

root.mainloop()

