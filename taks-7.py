!pip install pillow
import os
from PIL import Image
from google.colab import files
import zipfile

print("📂 Upload images or a ZIP file containing images:")
uploaded = files.upload()

for fn in uploaded.keys():
    if fn.endswith(".zip"):
        with zipfile.ZipFile(fn, 'r') as zip_ref:
            zip_ref.extractall("images_input")
        print(f"✅ Extracted ZIP: {fn}")
    else:
        os.makedirs("images_input", exist_ok=True)
        os.rename(fn, os.path.join("images_input", fn))

input_folder = "images_input"
output_folder = "images_output"
new_size = (300, 300)
new_format = "PNG"

os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        try:
            img_path = os.path.join(input_folder, file_name)
            with Image.open(img_path) as img:
                resized_img = img.resize(new_size)
                base_name = os.path.splitext(file_name)[0]
                output_path = os.path.join(output_folder, f"{base_name}.{new_format.lower()}")
                resized_img.save(output_path, new_format)
                print(f"✅ {file_name} resized and saved as {output_path}")
        except Exception as e:
            print(f"❌ Error processing {file_name}: {e}")

print("\n🎯 All images processed successfully!")

output_zip = "resized_images.zip"
with zipfile.ZipFile(output_zip, 'w') as zipf:
    for file_name in os.listdir(output_folder):
        zipf.write(os.path.join(output_folder, file_name), file_name)

files.download(output_zip)
