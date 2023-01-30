from os import path
import os
from threading import Thread
import shutil

WORK_FOLDER = path.join(r'E:\sort_trash\trash')
OUTPUT_DIR = path.join(r'E:\sort_trash')
def sort_by_ext(file_path: path) -> None:
    _, folder_name = os.path.splitext(file_path)
    ext_folder = os.path.join(OUTPUT_DIR,folder_name)
    os.makedirs(ext_folder, exist_ok = True)
    shutil.copy(file_path, ext_folder)

def sort_files(folder_path: path) -> None:
    threads = []
    for file in os.listdir(folder_path):
        
        if os.path.isdir(os.path.join(folder_path, file)):
            print(file, 'is dir')
            sort_files(os.path.join(folder_path, file))
        else:
            thread = Thread(name=f'{folder_path}', target=sort_by_ext, args=((os.path.join(folder_path,file),)))
            thread.start()
            threads.append(thread)
    [el.join() for el in threads]
            # sort_by_ext(os.path.join(folder_path,file))


if __name__ == '__main__':
    sort_files(WORK_FOLDER)
