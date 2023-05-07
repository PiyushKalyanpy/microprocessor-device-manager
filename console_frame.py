import customtkinter as ctk
import sys
from io import StringIO


# Redirect stdout to a variable
stdout_backup = sys.stdout
sys.stdout = StringIO()

console_output = sys.stdout.getvalue()
sys.stdout = stdout_backup



class ConsoleFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color='white')

        # console textbox
        self.console = ctk.CTkTextbox(self,bg_color='white', fg_color='#1f2226', border_width=0, height=250)
        self.console.pack(fill=ctk.BOTH, expand=True)


    def add_item(self, text):
        # add message to the end of the list
        self.console.insert("end", text + "\n")

        # scroll messages at last when new message added
        self.console.see("end")


