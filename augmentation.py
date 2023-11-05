from PIL import Image, ImageOps, ImageFilter
import os

def flip_image_and_label(image_path, image_folder):

    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)
    label_filename = f"{name}.txt"

    with Image.open(image_path) as img:
        flipped_img = ImageOps.mirror(img)
        new_image_filename = f"{name}_flipped{ext}"
        new_image_path = os.path.join(image_folder, new_image_filename)
        flipped_img.save(new_image_path)

    label_path = os.path.join(os.path.dirname(image_path), label_filename)
    new_label_filename = f"{name}_flipped.txt"
    new_label_path = os.path.join(image_folder, new_label_filename)

    if os.path.exists(label_path):
        with open(label_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            class_id, x_center, y_center, width, height = line.split()
            
            x_center = str(1 - float(x_center))
            new_lines.append(f"{class_id} {x_center} {y_center} {width} {height}\n")

        with open(new_label_path, 'w') as file:
            file.writelines(new_lines)

        print(f"Saved flipped image as {new_image_path} and label as {new_label_path}")
    else:
        print(f"Label file for {image_path} not found.")


def apply_gaussian_blur_and_save_label(image_path, image_folder, blur_radius= 0.3):
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)
    label_filename = f"{name}.txt"

    with Image.open(image_path) as img:
        blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))
        new_image_filename = f"{name}_blurred{ext}"
        new_image_path = os.path.join(image_folder, new_image_filename)
        blurred_img.save(new_image_path)

    label_path = os.path.join(os.path.dirname(image_path), label_filename)
    new_label_filename = f"{name}_blurred.txt"
    new_label_path = os.path.join(image_folder, new_label_filename)

    if os.path.exists(label_path):
        with open(label_path, 'r') as file:
            lines = file.readlines()

        with open(new_label_path, 'w') as file:
            file.writelines(lines)

        print(f"Saved blurred image as {new_image_path} and label as {new_label_path}")
    else:
        print(f"Label file for {image_path} not found.")


def main(image_folder):
    img_list = [path for path in os.listdir(image_folder) if path.endswith((".png",))]
    for img_path in img_list:
        full_img_path = os.path.join(image_folder, img_path)
        apply_gaussian_blur_and_save_label(full_img_path, image_folder)
        flip_image_and_label(full_img_path, image_folder)

if __name__ == "__main__":
    image_folder = r"E:\poongsan\PoongsanData\raw_Data\integral"
    main(image_folder)
