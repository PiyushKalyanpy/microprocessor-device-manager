import customtkinter as ctk
from settings import *
from external_devices import *
from PIL import Image, ImageTk
import serial

port = 'COM7'
baud_rate = 9600
ser = serial.Serial(port, baud_rate)

class PinsGrid(ctk.CTkFrame):
    def __init__(self, rows,  columns, parent):
        super().__init__(parent, fg_color='white', border_color="#e7e7e7", border_width=1)
        self.rows = rows
        self.columns = columns
        self.buttons = []

        self.pins = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                     '13', 'GND']
        self._create_buttons()

    def _create_buttons(self):
        i = 0
        for row in range(self.rows):
            for column in range(self.columns):
                self.buttons.append(OnOffButton(self, text=f"{self.pins[i]}"))
                self.buttons[-1].grid(row=row, column=column, padx=5, pady=5)
                i += 1

class OnOffButton(ctk.CTkFrame):
    def __init__(self, parent,  text):
        super().__init__(parent)

        self.isOn = False
        self.text= text



        self.statusImage = Image.open("assets/off.png")
        self.statusImage = self.statusImage.resize((20, 20))
        self.status = ImageTk.PhotoImage(self.statusImage)

        self.button = ctk.CTkButton(self, text=text, command=self.toggle_color, image=self.status,
                                    fg_color='white', text_color=FONT_COLOR, width=70, height=30,
                                    hover_color='#e7e7e7', bg_color='white')
        self.button.pack(side='left')

    def toggle_color(self):
        if self.isOn == False:
            self.statusImage = Image.open("assets/on.png")
            self.statusImage = self.statusImage.resize((20, 20))
            self.status = ImageTk.PhotoImage(self.statusImage)
            self.button.configure(image=self.status, fg_color="#ddf5d5")
            self.isOn = True
            self.read_pin()

        else:
            self.statusImage = Image.open("assets/off.png")
            self.statusImage = self.statusImage.resize((20, 20))
            self.status = ImageTk.PhotoImage(self.statusImage)
            self.button.configure(image=self.status, fg_color='white')
            self.isOn = False
    def read_pin(self):

        if self.isOn:
            # Read input from pin
            ser.write(('r' + self.text + '\n').encode())
            pin_input = ser.readline().strip().decode("utf-8")

            # Do something with the input

            print(f"Input from pin: {pin_input}")

            # console.add_item(f"Input from pin: {pin_input}")

            # Schedule the function to run again after a delay
            self.after(100, self.read_pin)