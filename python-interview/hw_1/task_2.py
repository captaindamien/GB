"""2. Дополнить следующую функцию недостающим кодом:"""
import os


def print_directory_contents(source_path: str) -> list:
    """Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами."""
    def get_directory_files(source_path: str) -> list:
        root = []
        for file_or_dir in os.listdir(source_path):
            full_name = os.path.join(os.path.abspath(source_path), file_or_dir)
            if os.path.isfile(full_name):
                root.append((os.path.abspath(source_path), file_or_dir))
            else:
                root.extend(get_directory_files(full_name))
        return root
    return [print(i) for i in get_directory_files(source_path)]


print_directory_contents(r'C:\Users\Admin\Desktop')
