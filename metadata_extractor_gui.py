import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image
import exifread

def extract_metadata(image_path):
    """Extract metadata from an image file."""
    try:
        # Open the image using PIL (Pillow)
        image = Image.open(image_path)

        # Open the image file in binary mode to read EXIF metadata
        with open(image_path, "rb") as f:
            tags = exifread.process_file(f)

        # Prepare metadata output
        metadata_info = f"Image Format: {image.format}\n"
        metadata_info += f"Image Size: {image.size}\n"
        metadata_info += f"Image Mode: {image.mode}\n\n"
        metadata_info += "Extracted Metadata:\n"

        for tag, value in tags.items():
            metadata_info += f"{tag}: {value}\n"

        return metadata_info

    except Exception as e:
        return f"Error: {e}"

def browse_image():
    """Open file dialog to select an image."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        metadata_text.delete(1.0, tk.END)  # Clear previous output
        metadata = extract_metadata(file_path)
        metadata_text.insert(tk.END, metadata)  # Display metadata

# Create GUI Window
root = tk.Tk()
root.title("Image Metadata Extractor")
root.geometry("600x500")
root.resizable(False, False)

# Heading Label
title_label = tk.Label(root, text="Image Metadata Extractor", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Browse Button
browse_button = tk.Button(root, text="Select Image", command=browse_image, font=("Arial", 12))
browse_button.pack(pady=10)

# Scrolled Text Box for Output
metadata_text = scrolledtext.ScrolledText(root, width=70, height=20, wrap=tk.WORD, font=("Arial", 10))
metadata_text.pack(pady=10)

# Run the GUI Application
root.mainloop()
