from copy_static_to_public import clear_public_directory, copy_static_to_public
from config import public, static, src_path, temp_path, dst_path
from block_markdown import markdown_to_html_node, extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    if os.path.isfile(from_path):
        with open(from_path, "r") as fp:
            fp_contents = fp.read()
        html_node = markdown_to_html_node(fp_contents)
        html_string = html_node.to_html()
        new_title = extract_title(fp_contents)

    if os.path.isfile(template_path):
        with open(template_path, "r") as tp:
            tp_contents = tp.read()
        tp_contents = tp_contents.replace("{{ Title }}", new_title)
        tp_contents = tp_contents.replace("{{ Content }}",  html_string)
        
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "w") as dest:
            dest.write(tp_contents)


def main():
    clear_public_directory(public)
    copy_static_to_public(static, public)
    generate_page(src_path, temp_path, dst_path)



if __name__ == "__main__":
    main()
