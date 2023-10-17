# Payton Lutterman
# Calculator-Class
# Last Updated 10-17

from scripts.settings import *

class Math(object):
    def __init__(self):
        self.root = Tk()
        self.display=StringVar()
        self.display.set("0")
        self.answer = ""
        self.opr1 = ""
        self.opr2 =""
        self.opp = ""

        self.root_setup()
        self.create_widgets()

    def root_setup(self):
        # Creating The Root and its Properties
        self.root.resizable(0,0)
        self.root.geometry(geoString)
        self.root.title(TITLE)
        self.root.iconbitmap(ICON)

    def play(self):
        self.root.mainloop()

    def create_widgets(self):
        # Creating Widgets
        self.frame_font = font.Font(family='Consolas',size=30,weight='bold')
        self.bttn_font = font.Font(family='Consolas',size=40,weight='bold')
        self.window = Frame(self.root, width=WIDTH, height=HEIGHT, background='gray5')
        self.display_lbl = Label(self.window, textvariable=self.display, font=self.frame_font,anchor="e")


        # Making The Number Keypad For The Calculator
        self.number_frame = Frame(self.window)
        self.numbers = "123456789C0="
        self.num_list = []
        row = 0
        col = 0
        for number in self.numbers:
            x= Button(self.number_frame, text = number, font=self.bttn_font, background='gray5', foreground='white', command=
            lambda id=number: self.button_click(id))
            x.grid(row=row,column=col,padx=5,pady=5,ipadx=5,ipady=5)
            self.num_list.append(x)
            col += 1
            if col > 2:
                row += 1
                col = 0

        # Making The Operator buttons
        self.opperator_frame = Frame(self.window)
        self.operators = "+-x/"
        self.opperator_list = []
        row = 0
        col = 4
        for l in self.operators:
            x = Button(self.opperator_frame, text=l, font=self.bttn_font, background='maroon', foreground='white',command=
            lambda id=l: self.button_click(id))
            x.grid(row=row, column=col, padx=5, pady=5, ipadx=5, ipady=5)
            self.opperator_list.append(x)
            row += 1
            if row > 1:
                row += 1

        # Place Widgets
        self.display_lbl.grid(row = 0, column = 0, columnspan = 4, sticky = NSEW, padx=5, pady=5, ipadx=5, ipady=5)
        self.number_frame.grid(row=4, column=0, columnspan=3, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)
        self.opperator_frame.grid(row=4, column=3, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)
        self.window.pack()

    def button_click(self, id):
        if id == "=":
            self.calculate()
        elif id == "+":
            self.opr1 = int(self.display.get())
            self.display.set("0")
            self.opp = "+"
        elif id == "-":
            self.opr1 = int(self.display.get())
            self.display.set("0")
            self.opp = "-"
        elif id == "x":
            self.opr1 = int(self.display.get())
            self.display.set("0")
            self.opp = "x"
        elif id == "/":
            self.opr1 = int(self.display.get())
            self.display.set("0")
            self.opp = "/"
        elif id == "C":
            self.display.set("0")
            self.answer = ""
            self.opr1 = ""
            self.opr2 = ""
            self.opp = ""
        else:
            temp = self.display.get()
            if temp == "0":
                temp = id
            else:
                temp += id

            self.display.set(temp)
        # Making Sure The User Doesn't Completely Break The Display With Giant Numbers
        if len(str(self.opr2)) or len(str(self.opr1)) > 18:
            self.display.set('ERROR')

    def calculate(self):
        self.opr2 = int(self.display.get())
        self.display.set("000")
        if self.opp == "+":
            self.answer = self.opr1+self.opr2
        elif self.opp == "-":
            self.answer = int(self.opr1)-self.opr2
        elif self.opp == "/":
            # Solving The Divide By 0 Error
            if self.opr1 == 0 or self.opr2 == 0:
                self.answer = 'ERROR'
            else:
                self.answer = self.opr1/self.opr2
        elif self.opp == "x":
            self.answer = self.opr1 * self.opr2
        self.display.set(self.answer)
