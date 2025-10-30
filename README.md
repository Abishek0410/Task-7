Task 7: Image Resizer Tool

Objective

To resize and convert images in batch automatically using Python and Pillow.
This project automates repetitive image processing tasks such as resizing, format conversion, and saving in a new directory.

Tools & Technologies

Python 3
Pillow (PIL)
os module
(Optional for Colab): `google.colab` and `zipfile`

 Description

This script reads all images from a specified folder, resizes them to a given dimension, and converts them into a chosen image format (like PNG or JPEG).
It helps in automating image tasks — saving time for designers, developers, and data scientists working on image datasets.
Features

✅ Resize multiple images in a batch
✅ Convert between formats (JPG → PNG, PNG → JPEG, etc.)
✅ Works locally **or** in **Google Colab**
✅ Automatically saves output images to a new folder
✅ Simple and beginner-friendly

 Folder Structure

📁 image_resizer_tool/
│
├── 📄 image_resizer.py        # Main Python script
├── 📄 README.md               # Project documentation
├── 📁 images_input/           # Folder containing original images
├── 📁 images_output/          # Folder where resized images are saved
└── 📦 resized_images.zip      # Output ZIP (in Colab)


 Key Concepts

* File Handling
* Image Processing
* Automation
* Exception Handling
* Directory Operations

How to Run (Locally)

1. Install Pillow:

   bash
   pip install pillow
   
2. Place your images inside the `images_input` folder.
3. Run the script:

  bash
  python image_resizer.py

4. Resized images will appear in the `images_output` folder.

How to Run (in Google Colab)

1. Open [Google Colab](https://colab.research.google.com/).
2. Copy and paste the **Colab-compatible version** of the script.
3. Upload your images or a ZIP file when prompted.
4. Download the resized images as a `.zip` file.

Output Example

✅ cat.jpg resized and saved as images_output/cat.png
✅ dog.png resized and saved as images_output/dog.png

 All images processed successfully!
 Outcome

✔ Automates repetitive image processing tasks
✔ Demonstrates file handling and image manipulation in Python
✔ Builds understanding of PIL and directory management

