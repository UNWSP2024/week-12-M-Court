#1: MPG Calculator
# Write a GUI program that calculates a car's gas mileage.
# The program's window should have Entry widgets that let the user enter
    # the number of gallons of gas the car holds
    # and the number of miles it can be driven on a full tank.
# When a Calculate MPG button is clicked
     # the program should display the number of miles that the car may be driven per gallon of gas.
     # Use the following formula to calculate miles per gallon:  MPG = miles / gallons.

#import tkinter
import tkinter
import tkinter.messagebox

#create MyGUI class
class GasMileageGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()

        #create top and bottom frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

#---------------ENTRY widget-----------------------

        #set variables as strings
        self.miles = tkinter.StringVar()
        self.gallons = tkinter.StringVar()

        #create a blank label in the top frame (so user can give us a value)
        #recieving as strings
        self.miles_label = tkinter.Label(self.top_frame, text='Enter distance in miles:')
        self.miles_entry = tkinter.Entry(self.top_frame, textvariable=self.miles, width=10)
        self.gallons_label = tkinter.Label(self.top_frame, text='Enter gas in gallons:')
        self.gallons_entry = tkinter.Entry(self.top_frame, textvariable=self.gallons, width=10)

        #pack the entry labels into top frame
        self.miles_label.pack(padx=10, pady=10)
        self.miles_entry.pack()
        self.gallons_label.pack(padx=10, pady=10)
        self.gallons_entry.pack()

#-------------create the buttons-----------
        # create the buttons into the frame

        # create a button widget
        # the text "Calculate MPG"
        # the calculate method should be executed when the user clicks the button
        self.calc_button = tkinter.Button(self.main_window, text='Calculate MPG', command=self.calc_method)
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        # pack the buttons into the frame (horizontal orientation)
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

#-------------pack frames------------------
        # pack the frames into window
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

#----------------------BUTTON callback-----------------

    # the callback function for the widget
    def calc_method(self):
        #convert the strings to floats
        gallons = float(self.gallons.get())
        miles = float(self.miles.get())

        #calculat miles per gallon
        mpg = miles / gallons
        tkinter.messagebox.showinfo('Gas Mileage', f"{gallons} gallons in {miles} miles is {mpg:.2f} miles per gallons")

#create an instance of the GasMileageGUI class
if __name__ == '__main__':
    gas_mileage_gui = GasMileageGUI()
