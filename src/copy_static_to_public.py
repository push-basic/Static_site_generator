import os
import shutil


def clear_public_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return
    for content in os.listdir(path):
        full_path = os.path.join(path, content)
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
        else:
            os.remove(full_path)


def copy_static_to_public(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for content in os.listdir(src):
        src_path = os.path.join(src, content)
        dst_path = os.path.join(dst, content)
        if os.path.isdir(src_path):
            copy_static_to_public(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)