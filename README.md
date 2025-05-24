# 🧬 GeneScoPy
![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)


Genome assembly sequence and GFF/GTF file analyzer

## Overview
GeneScoPy is a python based standalone graphical user interface (GUI) tool for working with genome assembly sequence files (FASTA) and genome annotation files (GTF/GFF). It provides a platform for:

- Inspecting and managing genome assembly files.
- Viewing genome annotation details.
- Performing basic analyses such as computing assembly statistics (e.g., N50, GC content, scaffold sizes).
- Searching and navigating annotation files efficiently.
- Higlight the region of interest in the FASTA sequence (selection based).
## Key Features
- **File Compatibility**: Supports FASTA and GTF/GFF file formats.
- **Assembly Details**: Displays total assembly length, scaffold counts, largest and smallest scaffolds, N50, and GC content.
- **Annotation Table**: Presents GTF/GFF data in an easy-to-navigate table with fields like scaffold, source, feature, start and end positions, strand, frame, product, and gene name.
- **Sequence Viewer**: Allows users to view scaffold sequences in a text editor.
- **Search Functionality**: Provides tools for searching and navigating annotation records by keywords.
- **Highlight Functionality** Highlights the sequence region of interest based annotation selection.
- **Highlight & Export Functionality**: Highlights sequence regions based on annotation selection and allows export of:
  - Selected annotation rows (`.csv`)
  - Full scaffold sequences (`.fasta`)
  - Highlighted region sequences (`.fasta`)
- **User-Friendly Interface**: Built with a modern and intuitive GUI.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/SamakshSingh99/GeneScoPy/
   cd GeneScoPy
   ```
2. Ensure you have Python installed (version 3.7 or higher).
3. Install required dependencies:
   ```bash
   pip install tk
   ```
4. Run the tool:
   ```bash
   python ./Script/Script.py
   ```

## How to Use
### Opening Files
1. Launch the application.
2. Use the `File` menu to open a FASTA file or GTF/GFF file.
   
<img width="1019" alt="Screenshot 2024-12-11 at 10 03 48 AM" src="https://github.com/user-attachments/assets/d9e8c53f-5536-459a-99cf-a149749adb1d">

### Viewing Assembly Details
- After loading a FASTA file, the "Assembly Details" section will display information about:
  - Total assembly length.
  - Number of scaffolds.
  - Largest and smallest scaffolds.
  - N50 value.
    
<img width="1020" alt="Screenshot 2024-12-11 at 10 04 51 AM" src="https://github.com/user-attachments/assets/50da89a5-23e1-4261-913b-40c7f88d3aa7">

### Viewing Annotation Data
- Load a GTF/GFF file to populate the annotation table.
- Use the table columns to explore scaffold details, gene annotations, and other metadata.

<img width="1019" alt="Screenshot 2024-12-11 at 10 06 47 AM" src="https://github.com/user-attachments/assets/659de93e-af6d-4f47-932f-02317aca6e52">

### Searching Annotations
- Use the search bar to find specific entries in the annotation table.
- Navigate through results using the `Previous` and `Next` buttons.
- Check the sequence box to find the highlighted regions for selection.
- Reset the search to view the entire table again.
  
 <img width="1019" alt="Screenshot 2024-12-11 at 11 32 44 AM" src="https://github.com/user-attachments/assets/adab1790-f11c-4389-bcb5-4edb67c41d90">

### Exporting Features

GeneScoPy allows exporting genome data in multiple formats directly from the GUI:

- ✅ **Export Selected Annotation Row**: Save a selected gene/feature row as a `.csv` file.
- ✅ **Export Full Scaffold**: Save the entire FASTA sequence of any scaffold in `.fasta` format.
- ✅ **Export Highlighted Region**: After selecting a gene/feature in the annotation table, export the matching sequence region as `.fasta`.

To use these:
1. Load both a FASTA and a GTF/GFF file.
2. Navigate to the `Export` menu in the menu bar.
3. Choose the appropriate export function.

<img width="1019" alt="Screenshot 2025-05-24 at 1 27 41 PM" src="https://github.com/user-attachments/assets/ee8458ed-6fcc-4763-90ad-5f4efb67d1b3" />

   
## File Management
- Scaffold sequences can be selected from the list and displayed in the sequence viewer for detailed inspection.

## Contributing
Contributions are welcome! If you'd like to enhance the tool or fix any bugs:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or support, please open an issue on the GitHub repository.
