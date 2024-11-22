#2:  Joe's Automotive
# Joe's Automotive performs the following routine maintenance service:
    # Oil Change - $30.00
    # Lube Job - $20.00
    # Radiator Flush - $40.00
    # Transmission Fluid - $100.00
    # Inspection - $35.00
    # Muffler replacement - $200.00
    # Tire Rotation - $20.00

# Write a GUI with check buttons that allows the user to select any or all of these services.  When the user clicks a button, the total charges should be displayed.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        #create two frames
        #one frame for Checkbuttons
        self.top_frame = tkinter.Frame(self.main_window)
        #one frame for regular button widgets
        self.bottom_frame = tkinter.Frame(self.main_window)

        #create three BooleanVar objects to use with the Checkbuttons
        self.cb_var1 = tkinter.BooleanVar()
        self.cb_var2 = tkinter.BooleanVar()
        self.cb_var3 = tkinter.BooleanVar()
        self.cb_var4 = tkinter.BooleanVar()
        self.cb_var5 = tkinter.BooleanVar()
        self.cb_var6 = tkinter.BooleanVar()
        self.cb_var7 = tkinter.BooleanVar()

        #create the Checkbutton widgets in the top frame
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Lub Job - $20.00', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100.00', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200.00', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable=self.cb_var7)

        #pack the Checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

#----------------OK and Quit------------------
        #create an OK and Quit button
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.ok_button.pack()
        self.quit_button.pack()

        #pack the Buttons
        self.top_frame.pack()
        self.bottom_frame.pack()

        #start the mainloop
        tkinter.mainloop()

#-------------CALLBACK-------------------
    #the show_choice method
    def show_choice(self):
        #create the message string
        self.message = "Joe's Automotive:\n"

        #determine with Checkbuttons are selected and find the sum
        price = 0
        if self.cb_var1.get():
            price += 30.00
        if self.cb_var2.get():
            price += 20.00
        if self.cb_var3.get():
            price += 40.00
        if self.cb_var4.get():
            price += 100.00
        if self.cb_var5.get():
            price += 35.00
        if self.cb_var6.get():
            price += 200.00
        if self.cb_var7.get():
            price += 20.00

        #display the message in an info dialog box
        tkinter.messagebox.showinfo('Thanks for stopping by!', f"Your total price is ${price:.2f}")

# create instance
if __name__ == '__main__':
    price_list_gui = MyGUI()
