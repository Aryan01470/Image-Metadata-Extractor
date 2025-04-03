 🖼️ Image Metadata Extractor

This is a simple Python script that extracts metadata from images using the **Pillow** and **ExifRead** libraries. It allows users to retrieve details like image size, format, EXIF metadata (camera model, timestamp, GPS coordinates, etc.).

 📌 Features
- Extracts metadata such as image format, size, and EXIF data.
- Works with JPEG, PNG, and other image formats.
- Uses **Python’s Pillow and ExifRead libraries for metadata extraction.

 🚀 Installation & Usage
 1️⃣ Clone the Repository
```bash
git clone https://github.com/Aryan01470/Image-Metadata-Extractor.git
cd Image-Metadata-Extractor
pip install pillow exifread
python metadata.py
Enter the full path of the image file: C:\Users\Aryan\Pictures\image.jpg
[INFO] Image Format: JPEG
[INFO] Image Size: 1920x1080
[INFO] EXIF Data:
  - Camera Model: Canon EOS 80D
  - Timestamp: 2023-12-01 14:35:21
  - GPS Location: 28.6139° N, 77.2090° E

