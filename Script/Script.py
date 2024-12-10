
'''
This tool allows users to open and inspect genome assembly sequence files (FASTA) 
and genome annotation files (GTF/GFF) through a graphical user interface. 
It provides a platform for basic genome assembly analysis and file management.
'''

#######################
# Importing Libraries #
#######################

import tkinter as tk 
from tkinter import filedialog, messagebox, ttk
from collections import defaultdict

###################################
# Defining Main Application Class #
###################################

class GenomeAssemblyApp(tk.Tk):
    def __init__(self):
        super().__init__() # Initializing parent Tk class
        self.title("Genome Assembly Analyzer") # Title
        self.geometry("900x900") # Window size
        self.scaffold_map = {} # Empty dictionary to Stores Scaffold and sequences
        self.create_menu() # Call method for creating menu bar
        self.create_widgets() # call method for creating widgets

    #####################
    # Creating Menu Bar #
    #####################

    def create_menu(self):

        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label ="Open FASTA", command =self.open_fasta)
        file_menu.add_command(label ="Open GTF/GFF", command =self.open_gtf)
        menu_bar.add_cascade(label = "File", menu = file_menu)
        self.config(menu = menu_bar)



if __name__ == "__main__":
    app = GenomeAssemblyApp()
    app.mainloop()