from Tkinter import *
from auth import *
from math import pow
window = Tk()
window.attributes('-fullscreen',True)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.title("Welcome to CANARA BANK ")
window.configure(background = "LightSeaGreen")
hashDir = {'efe9a4c30b262cc66f6be40afb9a97bdfbb7c89e66a313b17d16c86624bd615dddaae1fb6c3975211339057ec6cca0309069e3f22433de34d62993de6e340acd':'CHIRAG JAIN-18BIT0008', #7828
           'ddb09f20b3b0fcab1654fac601b83568f2110f6db007c8633c9f974dc126f2f75c3e76a7841b5fa393ec7879ec39c8548b16e689f09888c1cd45c58eb2ff590f':'MUSKAN SAHNI-18BIT0382', #6774
           '6f826cf5a8359854258e184537b978c39cff97bcde6118bd2df25072e537034fa66360d5e066296660f84b5be8168472b6b81455cb0723fffe7025804002e301':'MAHAK GUPTA-18BIT0041', #8367
           } 
hashDirLen = len(hashDir)
hashList = list(hashDir.keys())

def authenticate():
        newWin = Toplevel(window)
        newWin.attributes('-fullscreen',True)
        newWin.title("Authentication")
        newWin.configure(background = "LightSeaGreen" )
        Label(
                newWin,
                text = "Welcome to CANARA BANK ",
                bg = "LightSeaGreen",
                fg = "DarkCyan",
                font = "Consolas 72"
        ).place(
                x = 90,
                y = 50
        )
        P = PINEntry.get()
        PINEntry.delete(0,END)
        if len(P) == 4 and P.isdigit():
                q = 123456789987654321234567898 #random.randint(pow(10,20),pow(10,50))
                g = 23931164504956447807213117212663825326210289577470
                key = gen_key(q) #Receiver_Private_key
                h = power(g,key,q)
                out = encrypt(P,q,h,g)
                flag = 0
                for i in range(len(hashList)):
                        if out == hashList[i]:
                                flag = 1
                                pos = i
                                break
                if flag == 1:
                        Label(
                                newWin,
                                text = "PIN Matched. Hello, " + hashDir[hashList[pos]] + "!",
                                bg = "LightSeaGreen",
                                fg = "Navy",
                                font = "Consolas 20"
                        ).place(
                                x = 430,
                                y = 300
                        )
                        Button(
                                newWin,
                                text = "Back",
                                width = 20,
                                font = "Calibri 15",
                                bg = "LightSeaGreen",
                                fg = "White",
                                command = newWin.destroy
                        ).place(
                                x = 550,
                                y = 425
                        )
                else:
                        Label(
                                newWin,
                                text = "No match found. Please try again.",
                                bg = "LightSeaGreen",
                                fg = "Maroon",
                                font = "Consolas 20"
                        ).place(
                                x = 430,
                                y = 300
                        )
                        Button(
                                newWin,
                                text = "Back",
                                width = 20,
                                font = "Calibri 15",
                                bg = "LightSeaGreen",
                                fg = "White",
                                command = newWin.destroy
                        ).place(
                                x = 550,
                                y = 425
                        )
        else:
                Label(
                        newWin,
                        text = "Invalid PIN. Please try again.",
                        bg = "LightSeaGreen",
                        fg = "Maroon",
                        font = "Consolas 20"
                ).place(
                        x = 430,
                        y = 300
                )
                Button(
                        newWin,
                        text = "Back",
                        width = 20,
                        font = "Calibri 15",
                        bg = "LightSeaGreen",
                        fg = "White",
                        command = newWin.destroy
                ).place(
                        x = 550,
                        y = 425
                )
Label(
	text = "Welcome to CANARA BANK ",
	bg = "LightSeaGreen",
	fg = "DarkCyan",
	font = "Consolas 72"
).place(
	x = 90,
	y = 50
)
Label(
	text = "Enter your 4-digit PIN:",
	bg = "LightSeaGreen",
	fg = "White",
	font = "SegoeUILight 20",
).place(
	x = 525,
	y = 250
)
PINEntry = Entry(
	window,
	width = 4,
	font = "Consolas 50",
	show = "*"
)
PINEntry.place(
	x = 582,
	y = 300
)
PINEntry.focus_set()
Button(
	window,
	text = "Proceed",
	width = 20,
	font = "Calibri 15",
	bg = "LightSeaGreen",
	fg = "White",
	command = authenticate
).place(
	x = 550,
	y = 425
)
Button(
	window,
	text = "Quit",
	width = 20,
	font = "Calibri 15",
	bg = "LightSeaGreen",
	fg = "White",
	command = window.destroy
).place(
	x = 550,
	y = 475
)
window.mainloop()
