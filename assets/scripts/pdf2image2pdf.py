import os
from pdf2image import convert_from_path
from PIL import Image

def process_pdf(file_path, dpi=300):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    folder = os.path.dirname(file_path)
    original_path = os.path.join(folder, f"{base_name}_ori.pdf")
    output_path = os.path.join(folder, f"{base_name}.pdf")

    os.rename(file_path, original_path)

    print(f"Processing: {original_path}")
    images = convert_from_path(original_path, dpi=dpi)
    # images = images[:-1]  # Exclude last page

    if not images:
        print(f"Skipping {base_name} (only one page?)")
        return

    rgb_images = [img.convert("RGB") for img in images]
    rgb_images[0].save(output_path, save_all=True, append_images=rgb_images[1:])

    print(f"Saved: {output_path}\n")

def process_all_pdfs_in_folder(folder='.'):
    for filename in os.listdir(folder):
        if filename.endswith(".pdf") and not filename.endswith("_ori.pdf"):
            process_pdf(os.path.join(folder, filename))

if __name__ == "__main__":
    process_all_pdfs_in_folder()
    pass
