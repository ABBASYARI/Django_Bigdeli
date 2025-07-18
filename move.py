import os
import shutil

# مسیر فولدر اصلی (جایی که همه پوشه‌ها هستن)
source_root = r"C:\Users\AbbasYari\Downloads\Telegram Desktop\Html&Css_PyPackage"

# مسیر پوشه مقصد که قراره همه فایل‌ها اونجا جمع بشن
destination_folder = os.path.join(
    source_root,
    r"C:\Users\AbbasYari\Downloads\Telegram Desktop\Html&Css_PyPackage\lfiles",
)

# اگر پوشه مقصد وجود نداشت، ایجادش کن
os.makedirs(destination_folder, exist_ok=True)

# پیمایش تمام فایل‌ها در پوشه‌ها و زیرپوشه‌ها
for root, dirs, files in os.walk(source_root):
    # رد کردن پوشه مقصد خودش
    if root.startswith(destination_folder):
        continue

    for file in files:
        source_file_path = os.path.join(root, file)
        destination_file_path = os.path.join(destination_folder, file)

        # اگر فایل همنام وجود داشت، یک شمارنده اضافه کن
        base, ext = os.path.splitext(file)
        count = 1
        while os.path.exists(destination_file_path):
            destination_file_path = os.path.join(
                destination_folder, f"{base}_{count}{ext}"
            )
            count += 1

        shutil.copy2(source_file_path, destination_file_path)
        print(f"Copied: {source_file_path} → {destination_file_path}")
