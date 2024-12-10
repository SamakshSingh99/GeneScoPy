
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
        super().__init__()  # Initializing parent Tk class
        self.title("Genome Sequence and GFF/GTF Analyzer")  # Title
        self.geometry("1500x900")  # Window size
        self.scaffold_map = {}  # Empty dictionary to Stores Scaffold and sequences
        self.create_menu()  # Call method for creating menu bar
        self.create_widgets()  # call method for creating widgets
        self.search_results = [] # Initializing search index
        self.current_search_index = -1 # Initializing search index

    #####################
    # Creating Menu Bar #
    #####################

    def create_menu(self):
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open FASTA", command=self.open_fasta)
        file_menu.add_command(label="Open GTF/GFF", command=self.open_gtf)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

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

        # GTF/GFF Table with additional columns
        self.table_frame = tk.LabelFrame(self, text="GTF/GFF Data", padx=10, pady=10)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Search Bar
        self.search_frame = tk.Frame(self.table_frame)
        self.search_frame.pack(fill="x", padx=5, pady=5)

        self.search_entry = tk.Entry(self.search_frame, width=50)
        self.search_entry.pack(side="left", padx=5)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_table)
        self.search_button.pack(side="left", padx=5)

        self.previous_button = tk.Button(self.search_frame, text="Previous", command=self.previous_search)
        self.previous_button.pack(side="left", padx=5)

        self.next_button = tk.Button(self.search_frame, text="Next", command=self.next_search)
        self.next_button.pack(side="left", padx=5)

        self.reset_button = tk.Button(self.search_frame, text="Reset", command=self.reset_table)
        self.reset_button.pack(side="left", padx=5)

        self.table = ttk.Treeview(self.table_frame, columns=(
            "Sequence", "Source", "Feature", "Start", "End", "Strand", "Frame", "Product","Gene Name"), show="headings")
        
        self.table.heading("Sequence", text="Sequence")
        self.table.heading("Source", text="Source")
        self.table.heading("Feature", text="Feature")
        self.table.heading("Start", text="Start Position")
        self.table.heading("End", text="End Position")
        self.table.heading("Strand", text="Strand")
        self.table.heading("Frame", text="Frame")
        self.table.heading("Product", text="Product")
        self.table.heading("Gene Name", text="Gene Name")
        
        self.table.pack(fill="both", expand=True)

    def open_fasta(self):
        file_path = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta"), ("All files", "*.*")])
        if file_path:
            self.process_fasta(file_path)

    def open_gtf(self):
        file_path = filedialog.askopenfilename(filetypes=[("GTF files", "*.gtf"), ("GFF files", "*.gff"), ("All files", "*.*")])
        if file_path:
            self.process_gtf(file_path)

    def process_fasta(self, file_path):
        try:
            self.scaffold_map.clear()
            self.scaffold_listbox.delete(0, tk.END)
            with open(file_path, "r") as file:
                scaffold = None
                sequence = []
                for line in file:
                    line = line.strip()
                    if line.startswith(">"):
                        if scaffold:
                            self.scaffold_map[scaffold] = "".join(sequence)
                        scaffold = line[1:]
                        sequence = []
                    else:
                        sequence.append(line)
                if scaffold:
                    self.scaffold_map[scaffold] = "".join(sequence)

            # Populate details
            self.file_label.config(text=f"File Name: {file_path.split('/')[-1]}")
            self.update_assembly_details()
            self.scaffold_listbox.insert(tk.END, *self.scaffold_map.keys())

        except Exception as e:
            messagebox.showerror("Error", f"Could not process file: {e}")
    
    def process_gtf(self, file_path):
        try:
            with open(file_path, "r") as file:
                for line in file:
                    if not line.startswith("#"):
                        parts = line.strip().split("\t")
                        if len(parts) >= 9:  # Ensure there's enough columns
                            sequence = parts[0]   # seqname
                            source = parts[1]      # source
                            feature = parts[2]     # feature type (gene, exon, etc.)
                            start = parts[3]       # start position
                            end = parts[4]         # end position
                            strand = parts[6]      # strand (+ or -)
                            frame = parts[7]       # frame
                            product = parts[8]
                            attributes = parts[8]  # gene ID or gene name

                            # Extract the gene name from the attributes (assuming it's in 'gene_name' or 'gene_id')
                            gene_name = "Unknown"
                            if 'gene "' in attributes:  # GTF format
                                gene_name = attributes.split('gene "')[1].split('"')[0]
                            elif "gene=" in attributes:  # GFF format
                                gene_name = attributes.split("gene=")[1].split(";")[0]
                            elif "Name=" in attributes:  # GFF format alternative
                                gene_name = attributes.split("Name=")[1].split(";")[0]
                            
                            product_out = "Unknown"
                            if 'product "' in product: # GTF format
                                product_out = product.split('product "')[1].split('"')[0]
                            elif "product=" in product: #GFF format
                                product_out = product.split("product=")[1].split(";")[0]


                            # Insert data into table
                            self.table.insert("", "end", values=(sequence, source, feature, start, end, strand, frame, product_out, gene_name))

        except Exception as e:
            messagebox.showerror("Error", f"Could not process file: {e}")

    def update_assembly_details(self):
        total_length = sum(len(seq) for seq in self.scaffold_map.values())
        num_scaffolds = len(self.scaffold_map)

        largest_scaffold = max(self.scaffold_map, key=lambda x: len(self.scaffold_map[x]))
        largest_length = len(self.scaffold_map[largest_scaffold])

        smallest_scaffold = min(self.scaffold_map, key=lambda x: len(self.scaffold_map[x]))
        smallest_length = len(self.scaffold_map[smallest_scaffold])

        sorted_lengths = sorted(len(seq) for seq in self.scaffold_map.values())
        cumulative_length = 0
        n50 = 0
        for length in sorted_lengths:
            cumulative_length += length
            if cumulative_length >= total_length / 2:
                n50 = length
                break

        self.assembly_length_label.config(text=f"Total Assembly Length: {total_length}")
        self.num_scaffolds_label.config(text=f"Total Number of Scaffolds: {num_scaffolds}")
        self.largest_scaffold_label.config(text=f"Largest Scaffold: {largest_scaffold} ({largest_length})")
        self.shortest_scaffold_label.config(text=f"Shortest Scaffold: {smallest_scaffold} ({smallest_length})")
        self.n50_label.config(text=f"N50: {n50}")

    def display_sequence(self, event):
        selected = self.scaffold_listbox.curselection()
        if selected:
            scaffold = self.scaffold_listbox.get(selected)
            sequence = self.scaffold_map.get(scaffold, "")
            self.sequence_text.delete(1.0, tk.END)
            self.sequence_text.insert(tk.END, sequence)
            # Calculate GC content
            gc_count = sum(1 for char in sequence if char in "GC")
            gc_content = (gc_count / len(sequence)) * 100 if sequence else 0
            self.gc_content_label.config(text=f"GC Content: {gc_content:.2f}%")

    def search_table(self):
        query = self.search_entry.get().lower()
        self.search_results.clear()  # Clear previous search results
        self.current_search_index = -1  # Reset the search index

        for idx, row in enumerate(self.table.get_children()):
            values = self.table.item(row, "values")
            if any(query in str(value).lower() for value in values):
                self.search_results.append(row)

        if self.search_results:
            self.current_search_index = 0
            self.highlight_search()

    def next_search(self):
        if self.search_results and self.current_search_index < len(self.search_results) - 1:
            self.current_search_index += 1
            self.highlight_search()

    def previous_search(self):
        if self.search_results and self.current_search_index > 0:
            self.current_search_index -= 1
            self.highlight_search()

    def highlight_search(self):
        for row in self.table.selection():
            self.table.selection_remove(row)
        if self.search_results:
            row = self.search_results[self.current_search_index]
            self.table.selection_set(row)
            self.table.see(row)

    def reset_table(self):
        self.search_results.clear()
        self.current_search_index = -1
        self.table.selection_remove(*self.table.selection())
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = GenomeAssemblyApp()
    app.mainloop()
