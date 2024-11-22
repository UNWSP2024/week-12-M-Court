#3 Long-Distance Calls
#A long-distance provider charges the following rates for telephone calls:
    #  Rate Category	Rate per Minute
    #  Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02
    #  Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12
    #  Off-Peak (midnight through 5:59 P.M.) 	$0.05

#Write a GUI application that allows the user to select a rate category (from a set of radio buttons),
# and enter the number of minutes of the call into a Entry widget.
# An info dialog box should display the charge for the call.

import tkinter
import tkinter.messagebox

class CentsPerMinuteGUI:
    def __init__(self):
        #create the main window
        self.main_window = tkinter.Tk()

        #create top frame fir Radiobuttons
        self.top_frame = tkinter.Frame(self.main_window)
        #create bottom frame for regular Button widgets
        self.bottom_frame = tkinter.Frame(self.main_window)


#-----------Radiobuttons-----------

        #create the IntVar object to use with the Radiobuttons.
        self.radio_var = tkinter.DoubleVar()

        #set the doubleVar object to 1 (default)
        self.radio_var.set(1)

        self.minutes = tkinter.StringVar()

        #create label
        self.min_label = tkinter.Label(self.top_frame, text="Enter time in minutes:")
        #create entry
        self.min_entry = tkinter.Entry(self.top_frame, textvariable=self.minutes, width=10)

        #pack label and entry
        self.min_label.pack()
        self.min_entry.pack()

        #create Radiobuttons in the top frame
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Daytime', variable=self.radio_var, value=0.02)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Evening', variable=self.radio_var, value=0.12)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Offpeak', variable=self.radio_var, value=0.05)

        #pack Radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

#---------------- OK and QUIT------------------

        #self.okay_button
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.calc_method)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit',command=self.main_window.destroy)

        #pack ok and quit buttons
        self.ok_button.pack()
        self.quit_button.pack()

#----------------PACK FRAMES------------

        #pack frame into window
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    # ------------CALLBACK-------------------

    #callback function for calculate
    def calc_method(self):
        #convert string to float
        minutes = float(self.minutes.get())
        rate = float(self.radio_var.get())
        #calculate cost
        cost = minutes * rate

        #display total cost
        tkinter.messagebox.showinfo('Cost', f"{minutes:.0f} minutes at ${rate:.2f} per minute is ${cost:.2f}")

#create an instance of the MyGui class
if __name__ == '__main__':
    cents_per_minute_gui = CentsPerMinuteGUI()
