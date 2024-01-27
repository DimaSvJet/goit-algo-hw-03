import argparse     # Ствює парсери кoманднoгo рядка
from pathlib import Path # зручний інтерфейс для роботи з файловими та каталожними шляхами
import shutil # Містить функції для взаємодії з файловою системою, такі як копіювання файлів

def parce_arvg(): # Визначає парсер аргументів командного рядка
    parser = argparse.ArgumentParser(description="Копіювання файлів в папку")
    parser.add_argument("-s", "--source", type=Path, required=True, help="Папка з файлами")
    parser.add_argument("-o", "--output", type=Path, default=Path("output"), help="Папка для копіювання")
    return parser.parse_args()

def recursive_copy(source: Path, output: Path): # Рекурсивно копіює файли з джерела (вказано в source) в вихідну папку (вказано в output)
    for el in source.iterdir(): # Метод iterdir(), oтримає всі елементи (файли та каталоги) 
        if el.is_dir(): # Перевірка, що це папка
            recursive_copy(el, output)
        else:
            extension = el.suffix.lstrip('.')  # Отримати розширення файла
            folder = output / extension  # Ствюється об'єкт типу Path для представлення шляху до папки
            folder.mkdir(exist_ok=True, parents=True)

            shutil.copy(el, folder) #Куди copy класти

def main(): # Функція, яка викликається при запуску скрипта
    args = parce_arvg()
    print(args)

if __name__ == '__main__':  # конструкція гарантує, що функція main() буде викликана тільки тоді, коли скрипт викликається безпосередньо
    main()
