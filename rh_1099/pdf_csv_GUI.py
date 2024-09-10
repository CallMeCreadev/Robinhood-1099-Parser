import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog, messagebox, ttk
import os
import csv
from rh_1099.pdf_parser.parser_2020 import Parser2020  # Ensure this import matches your project structure

def update_progress_bar(value, progress_bar):
    progress_bar['value'] = value
    root.update_idletasks()  # Ensures the GUI updates in real-time

def remove_empty_rows(input_csv, output_csv):
    with open(input_csv, 'r', newline='') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if any(cell.strip() for cell in row):  # Check if any cell in the row is not empty
                writer.writerow(row)

def process_pdf(pdf_path, progress_bar, show_progress=True):
    parser = Parser2020(pdf_path)
    contents = parser.process(show_progress, progress_callback=lambda x: update_progress_bar(x, progress_bar))

    # Generate the temporary and final CSV file paths
    csv_dir = os.path.dirname(pdf_path)
    temp_csv_name = f"TempCSV_{os.path.splitext(os.path.basename(pdf_path))[0]}.csv"
    temp_csv_path = os.path.join(csv_dir, temp_csv_name)

    final_csv_name = f"CSV_{os.path.splitext(os.path.basename(pdf_path))[0]}.csv"
    final_csv_path = os.path.join(csv_dir, final_csv_name)

    if not contents.empty():
        # Save to the temporary CSV file first
        contents.to_csv(temp_csv_path)

        # Clean the temporary CSV file and save to the final CSV file
        remove_empty_rows(temp_csv_path, final_csv_path)

        # Optionally, remove the temporary CSV file after processing
        os.remove(temp_csv_path)

        messagebox.showinfo("Success", f"CSV file saved as {final_csv_path}")
    else:
        messagebox.showwarning("No Data", "No data to save to a file")

def open_file_dialog():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="Choose a PDF file"
    )

    if file_path:
        process_pdf(file_path, progress_bar, show_progress=True)

# Create the main application window
root = TkinterDnD.Tk()  # Use TkinterDnD's Tk class
root.title("PDF to CSV Converter")

label = tk.Label(root, text="Drag and drop a PDF file here, or click 'Browse'.", padx=20, pady=20)
label.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=open_file_dialog)
browse_button.pack(pady=20)

# Add drag and drop functionality
def drop(event):
    pdf_path = event.data.strip('{}')
    process_pdf(pdf_path, progress_bar, show_progress=True)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()
