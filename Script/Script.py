
'''
This tool allows users to open and inspect genome assembly sequence files (FASTA) 
and genome annotation files (GTF/GFF) through a graphical user interface. 
It provides a platform for basic genome assembly analysis and file management.
'''

##########################
# 1. Importing Libraries #
##########################

import tkinter as tk 
from tkinter import filedialog, messagebox, ttk
from collections import defaultdict

######################################
# 2. Defining Main Application Class #
######################################