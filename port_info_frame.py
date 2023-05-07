import customtkinter as ctk

import pins_grid
from external_devices import *
from settings import *
from pins_grid import *

class PortInformationFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color='#f7f7f7')

        deviceNameLabel = ctk.StringVar()
        deviceSrNumLabel = ctk.StringVar()

        def port_select_callback(choice):
            print("combobox dropdown clicked:", choice)
            deviceData = get_ports()[choice]
            deviceName = ' '.join(deviceData['description'].split(' ')[:-1])
            ser_index = deviceData['hwid'].find('SER=') + len('SER=')
            serailNumber = deviceData['hwid'][ser_index:ser_index + 20]
            deviceNameLabel.set(deviceName)
            deviceSrNumLabel.set(serailNumber)
            port = deviceData['port']
            pins_grid.port = port


        self.optionFrame = ctk.CTkFrame(self, fg_color='white')
        self.nameFrame = ctk.CTkFrame(self, fg_color='white')
        self.srNumFrame = ctk.CTkFrame(self, fg_color='white')

        self.optionFrame.pack(side='left', padx=10)
        self.nameFrame.pack(side="left", padx=(5, 10), pady=10, expand=True, fill="both", anchor="center")
        self.srNumFrame.pack(side="left", padx=(5, 10), pady=10, expand=True, fill="both", anchor="center")

        self.port_selector = ctk.CTkComboBox(self.optionFrame,
                                             values=list(get_ports().keys()),
                                             command=port_select_callback,
                                             fg_color='white',
                                             text_color=FONT_COLOR,
                                             border_width=0,
                                             button_color=MAIN_COLOR,
                                             hover=TEXT_COLOR
                                             )
        self.port_selector.pack()

        self.nameText = ctk.CTkLabel(self.nameFrame, text="Device Name : ", text_color=TEXT_COLOR)
        self.nameText.pack(padx=10, side='left')
        self.deviceNameLabel = ctk.CTkLabel(self.nameFrame, textvariable=deviceNameLabel, text_color=FONT_COLOR)
        self.deviceNameLabel.pack(padx=10, side='left')

        self.nameText = ctk.CTkLabel(self.srNumFrame, text="Serial Number : ", text_color=TEXT_COLOR)
        self.nameText.pack(padx=10, side='left')
        self.deviceNameLabel = ctk.CTkLabel(self.srNumFrame, textvariable=deviceSrNumLabel, text_color=FONT_COLOR)
        self.deviceNameLabel.pack(padx=10, side='left')