import customtkinter as ctk
from port_info_frame import PortInformationFrame
from pins_grid import PinsGrid
from console_frame import ConsoleFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='white')
        self._set_appearance_mode('light')
        self.geometry("900x500")
        self.title("Control Hub")

        # layout
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=4)

        self.portInfo = PortInformationFrame(parent=self)
        self.portInfo.pack_propagate()
        self.portInfo.pack(fill=ctk.X, padx=20, pady=20, ipadx=30)

        self.pins = PinsGrid(parent=self,  rows=2, columns=10)
        self.pins.pack_propagate()
        self.pins.pack(fill=ctk.X, padx=20, pady=20, ipadx=30)

        self.console = ConsoleFrame(parent=self)
        self.console.pack_propagate()
        self.console.pack(fill=ctk.X, padx=20, pady=20, ipadx=30)



if __name__ == '__main__':
    app = App()
    app.mainloop()