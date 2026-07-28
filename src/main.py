from copy_static_to_public import clear_public_directory, copy_static_to_public
from config import public, static



def main():
    clear_public_directory(public)
    copy_static_to_public(static, public)



if __name__ == "__main__":
    main()
