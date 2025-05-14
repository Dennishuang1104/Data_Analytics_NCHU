import os
import shutil
from pathlib import Path

# source_dir = "usps_images/train"
# output_image_dir = "datasets/images"
# output_label_dir = "datasets/labels"
#
# os.makedirs(output_image_dir, exist_ok=True)
# os.makedirs(output_label_dir, exist_ok=True)
#
# img_counter = 0
#
# for label in sorted(os.listdir(source_dir)):
#     class_dir = os.path.join(source_dir, label)
#     if not os.path.isdir(class_dir):
#         continue
#
#     for img_name in os.listdir(class_dir):
#         if img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
#             img_counter += 1
#             new_img_name = f"{label}_{str(img_counter).zfill(5)}.jpg"
#
#             src_path = os.path.join(class_dir, img_name)
#             dst_path = os.path.join(output_image_dir, new_img_name)
#
#             shutil.copy2(src_path, dst_path)
#
#             # YOLO 標籤 (預設中心點在圖片中心、寬高為整張圖的 100%)
#             label_path = os.path.join(output_label_dir, new_img_name.replace('.jpg', '.txt'))
#             with open(label_path, 'w') as f:
#                 f.write(f"{label} 0.5 0.5 1.0 1.0\n")


# from PIL import Image
# import os
#
# image_dir = "datasets/images"
#
# for filename in os.listdir(image_dir):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#         img_path = os.path.join(image_dir, filename)
#         with Image.open(img_path) as img:
#             width, height = img.size
#             print(f"{filename}: width={width}, height={height}")


from PIL import Image
import os

input_dir = "datasets/images"
output_dir = "datasets/images_resized"
os.makedirs(output_dir, exist_ok=True)

target_size = (64, 64)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_dir, filename)
        with Image.open(img_path) as img:
            img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
            img_resized.save(os.path.join(output_dir, filename))
