
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

    ##############################
    # Function to Create Widgets #
    ##############################

    def create_widgets(self):
        
        # Assembly Details Panel
        self.details_frame = tk.LabelFrame(self, text="Assembly Details", padx=10, pady=10)
        self.details_frame.pack(fill="x", padx=10, pady=5)

        self.file_label = tk.Label(self.details_frame, text="File Name: ")
        self.file_label.pack(anchor="w")

        self.assembly_length_label = tk.Label(self.details_frame, text="Total Assembly Length: ")
        self.assembly_length_label.pack(anchor="w")

        self.num_scaffolds_label = tk.Label(self.details_frame, text="Total Number of Scaffolds: ")
        self.num_scaffolds_label.pack(anchor="w")

        self.largest_scaffold_label = tk.Label(self.details_frame, text="Largest Scaffold: ")
        self.largest_scaffold_label.pack(anchor="w")

        self.shortest_scaffold_label = tk.Label(self.details_frame, text="Shortest Scaffold: ")
        self.shortest_scaffold_label.pack(anchor="w")

        self.n50_label = tk.Label(self.details_frame, text="N50: ")
        self.n50_label.pack(anchor="w")

        self.gc_content_label = tk.Label(self.details_frame, text="GC Content: ")
        self.gc_content_label.pack(anchor="w")

        # Scaffold List and Sequence Viewer
        self.scaffold_frame = tk.Frame(self)
        self.scaffold_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.scaffold_listbox = tk.Listbox(self.scaffold_frame, width=40)
        self.scaffold_listbox.pack(side="left", fill="y")
        self.scaffold_listbox.bind("<<ListboxSelect>>", self.display_sequence)

        self.sequence_text = tk.Text(self.scaffold_frame, wrap="word")
        self.sequence_text.pack(side="right", fill="both", expand=True)

        # GTF/GFF Table
        self.table_frame = tk.LabelFrame(self, text="GTF/GFF Data", padx=10, pady=10)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.table = ttk.Treeview(self.table_frame, columns=("Sequence", "Source", "Feature"), show="headings")
        self.table.heading("Sequence", text="Sequence")
        self.table.heading("Source", text="Source")
        self.table.heading("Feature", text="Feature")
        self.table.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = GenomeAssemblyApp()
    app.mainloop()