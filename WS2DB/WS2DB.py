from pathlib import WindowsPath, PureWindowsPath
from shutil import copy2
from sys import argv

from PIL import Image

path_src = WindowsPath(
    r'~\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets').expanduser()
path_dst = WindowsPath(r'~\OneDrive\Pictures').expanduser()


def setup_dst():
    if not path_dst.exists():
        path_dst_alternate = WindowsPath().cwd().parent.joinpath(r'Spotlight')
        path_dst_alternate.mkdir()


def main():
    for child_src in path_src.iterdir():
        child_dst = path_dst.joinpath(child_src.name)
        if not child_dst.exists() or not child_dst.with_suffix('.jpg').exists():
            copy2(child_src, path_dst)
            image_path = child_dst.rename(child_dst.with_suffix('.jpg'))
            with Image.open(image_path) as image:
                if image.width < image.height:
                    image.close()
                    image_path.unlink()


if __name__ == '__main__':
    setup_dst()
    main()
