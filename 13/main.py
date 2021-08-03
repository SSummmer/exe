"""
    练习13
"""
import os
import random
import shutil

image = {'.jpg', '.png', '.gif'}
doc = {'.txt', '.docx', '.pptx'}
video = {'.mp4', '.mp3'}
sheet = {'.xlsx'}
code = {'.py', '.c', '.cpp', '.exe', '.o', '.px', '.q'}


def proc(path):
    suffx_list = ['.jpg', '.mp4', '.txt',
                  '.docx', '.pptx', '.xlsx',
                  '.png', '.py', '.c', '.cpp',
                  '.exe', '.mp3', '.gif',
                  '.o', '.px', '.q',
                  ]
    os.makedirs(path, exist_ok=True)
    for i in range(1000):
        filepath = os.path.join(path, str(random.randint(0, 99999)) + suffx_list[
            random.randrange(0, len(suffx_list))])
        with open(filepath, 'w') as f:
            pass


def create_dirs(path):
    dir_list = ["images", "docs", "videos", "sheets", "codes"]
    for dir_name in dir_list:
        dir_path = path + "/" + dir_name
        if os.path.exists(dir_path):
            pass
        else:
            os.makedirs(dir_path, exist_ok=True)


def synonym(file_path):
    if os.path.exists(file_path):
        pass


def classify(file, path):
    file_name, t = os.path.splitext(file)
    if t in image:
        if os.path.exists(path + '/images/' + file):
            pass
        else:
            shutil.move(path + '/' + file, path + "/images/")
    elif t in doc:
        if os.path.exists(path + '/docs/' + file):
            pass
        else:
            shutil.move(path + '/' + file, path + "/docs/")
    elif t in video:
        if os.path.exists(path + '/videos/' + file):
            pass
        else:
            shutil.move(path + '/' + file, path + "/videos/")
    elif t in sheet:
        if os.path.exists(path + '/sheets/' + file):
            pass
        else:
            shutil.move(path + '/' + file, path + "/sheets/")
    elif t in code:
        if os.path.exists(path + '/codes/' + file):
            pass
        else:
            shutil.move(path + '/' + file, path + "/codes/")
    else:
        return None


def main():
    path = '/Users/xiayubing/PycharmProjects/code/13/files'
    create_dirs(path)
    proc(path)
    for files in os.walk(path):
        for file in files[2]:
            classify(file, path)


if __name__ == '__main__':
    main()
