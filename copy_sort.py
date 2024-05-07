"""
python copy_sort.py test_source dist
"""

import argparse
import os
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description="Копіює файли з однієї директорії в іншу, сортуючи їх за розширенням.")
    parser.add_argument("source", type=str, help="Шлях до вихідної директорії")
    parser.add_argument("destination", type=str, nargs='?', default="dist",
                        help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()


def copy_files_based_on_extension(source, destination):
    try:
        # Створення директорії призначення, якщо вона не існує
        os.makedirs(destination, exist_ok=True)

        # Обхід елементів у директорії
        for entry in os.listdir(source):
            full_path = os.path.join(source, entry)
            if os.path.isdir(full_path):
                # Рекурсивний виклик для піддиректорії
                copy_files_based_on_extension(full_path, destination)
            elif os.path.isfile(full_path):
                # Обробка файлу
                extension = os.path.splitext(entry)[1][1:]  # Вилучення розширення без крапки
                if extension == "":
                    extension = "no_extension"

                # Створення піддиректорії для кожного типу файлів
                ext_dir = os.path.join(destination, extension)
                os.makedirs(ext_dir, exist_ok=True)

                # Копіювання файлу в відповідну піддиректорію
                shutil.copy(full_path, ext_dir)

    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")


def main():
    args = parse_args()
    copy_files_based_on_extension(args.source, args.destination)
    print(f"Файли з директорії '{args.source}' були успішно скопійовані та розсортовані в '{args.destination}'.")


if __name__ == "__main__":
    main()
