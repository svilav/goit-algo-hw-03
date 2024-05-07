import os


def create_test_files(base_dir):
    os.makedirs(base_dir, exist_ok=True)
    # Створення декількох файлів з різними розширеннями
    extensions = ['txt', 'jpg', 'png', 'pdf', '']
    subdirs = ['folder1', 'folder2', 'folder1/subfolder']

    # Створення піддиректорій
    for subdir in subdirs:
        os.makedirs(os.path.join(base_dir, subdir), exist_ok=True)

    # Створення файлів у кожній директорії
    for ext in extensions:
        for subdir in subdirs:
            file_path = os.path.join(base_dir, subdir, f"testfile_{ext}.{ext}" if ext else "testfile_no_ext")
            with open(file_path, 'w') as f:
                f.write(f"This is a test file with extension {ext}\n")


def main():
    base_dir = "test_source"
    create_test_files(base_dir)
    print(f"Тестові файли створено в директорії '{base_dir}'.")


if __name__ == "__main__":
    main()
