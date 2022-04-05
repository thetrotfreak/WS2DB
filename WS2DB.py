from pathlib import WindowsPath, PureWindowsPath
from shutil import copy2
from sys import argv

from PIL import Image

path_src = WindowsPath(
    r'~\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets').expanduser()
app_dir = PureWindowsPath(argv[0]).parent
path_dst = WindowsPath(app_dir).joinpath(r'Assets')


def setup():
    if path_dst.exists():
        pass
    else:
        path_dst.mkdir()


def main():
    for child in path_src.iterdir():
        new_child = path_dst.joinpath(child.name)
        if new_child.exists() or new_child.with_suffix('.jpg').exists():
            pass
        else:
            copy2(child, path_dst)
            image_path = new_child.rename(new_child.with_suffix('.jpg'))
            with Image.open(image_path) as image:
                if image.width != 1920:
                    image.close()
                    image_path.unlink()


if __name__ == '__main__':
    setup()
    main()
