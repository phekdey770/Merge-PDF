import os
from PyPDF2 import PdfMerger
from PyQt5.QtWidgets import QApplication, QFileDialog, QInputDialog

# Define the path where PDF files are located
pdf_folder_path = r"C:\Code Workpace\VS Code\Python 3\Z - Other\Data\Convert\Merge"

def merge_pdfs_in_folder(folder_path):
    # Initialize the PDF merger
    merger = PdfMerger()

    # Iterate through all files in the folder
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder_path, filename)
            merger.append(filepath)

    # Prompt the user to input the filename to save the merged PDF
    app = QApplication([])
    text, ok = QInputDialog.getText(None, 'Save Merged PDF', 'Enter filename for merged PDF:')
    if ok and text:
        merged_pdf_path = os.path.join(folder_path, f"{text}.pdf")
        # Write out the merged PDF file
        merger.write(merged_pdf_path)
        merger.close()
        print(f"Merged PDF saved as: {merged_pdf_path}")
    else:
        print("No filename provided. Merge operation canceled.")

if __name__ == "__main__":
    merge_pdfs_in_folder(pdf_folder_path)

