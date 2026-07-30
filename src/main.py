import os
import shutil
import sys

from config import dir_path_docs, dir_path_content, dir_path_static, template_path
from copy_static_to_public import copy_files_recursive
from generate_content import generate_pages_recursive




def main() -> None:
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        raise Exception("No basepath given")

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


main()
