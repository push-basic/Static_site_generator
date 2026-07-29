import os
import shutil

from config import dir_path_content, dir_path_public, dir_path_static, template_path
from copy_static_to_public import copy_files_recursive
from generate_content import generate_pages_recursive


def main() -> None:
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()
