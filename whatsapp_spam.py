from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess

'''def command_root():

    stime=3000
    root = Tk()
    root.title("Follow the instruction")
    root.geometry('320x85')
    text = Text(root)
    text.insert(INSERT,"Scan the QR code")
    text.config(font=("Calibri",12,"bold"),state=DISABLED)
    text.pack()
    root.after(stime , lambda:root.destroy())  #show tkinter window for 3 seconds
    root.mainloop()'''

def notifyme():
    subprocess.Popen(['notify-send',"Scan the QR Code"])
    return


def send():
    chromedriver_loc = '/path/to/chromedriver' # enter path of chromedriver
    driver = webdriver.Chrome(executable_path=chromedriver_loc)
    
    notifyme()
    driver.get('http://web.whatsapp.com')
    driver.quit()

    input() # If done scanning write done on command terminal

    path = '//span[contains(text(),"' + entry1.get() + '")]'
    elem = driver.find_element_by_xpath(path)
    elem.click()
    elem1=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    
    for i in range(int(entry2.get())):
        elem1.send_keys(entry3.get())
        elem1.send_keys(Keys.RETURN)



######### GUI ############

root = Tk()
root.title("Whatsapp Spammer")
root.geometry("320x130")
root.resizable(width=False, height=False)

#### create label1 ########         
label1 = Label(root, text="Enter Victim's Name ")
entry1 = Entry(root)
 
#### label1 configuration ########  
label1.grid(row=1, column=0 ,padx=10, pady=(5,5))
entry1.grid(row=1,column=2 ,padx=10, pady=(5,5))


#### create label2 ########  
label2 = Label(root, text="No. of times")
entry2 = Entry(root)

#### label2 configuration ######## 
label2.grid(row=2, column=0 ,padx=10, pady=(5,5))
entry2.grid(row=2, column=2 ,padx=10, pady=(5,5))

#### create label3 ######## 
label3 = Label(root, text="Message")
entry3= Entry(root)

#### label3 configuration ######## 
label3.grid(row=3,column=0 ,padx=10, pady=(5,5))
entry3.grid(row=3,column=2 ,padx=10, pady=(5,5))

button = Button(root, text="SEND", command=send)
button.place(x=150,y=90)
root.mainloop()

