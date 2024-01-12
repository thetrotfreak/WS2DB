from PIL import Image
from pathlib import Path
from platform import system
from shutil import copy2
from subprocess import check_output


class Spotlight:
    def __init__(self):
        self.pathname = ""
        self.savepath = ""
        self.winuser = ""
        self.iswsl = False

        if system() == "Linux":
            try:
                self.winuser = check_output(
                    ["powershell.exe", "$env:USERNAME"], text=True
                ).strip()
            except FileNotFoundError:
                pass
            else:
                self.iswsl = True
                self.pathname = Path(
                    rf"/mnt/c/Users/{self.winuser}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
                )
                self.savepath = Path(rf"/mnt/c/Users/{self.winuser}/spotlight/")

        elif system() == "Windows":
            self.pathname = Path(
                r"~\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
            ).expanduser()
            self.savepath = Path(r"~\spotlight\"").expanduser()

    def saveall(self):
        if not self.savepath.is_dir():
            self.savepath.mkdir()
        if self.pathname:
            for child_src in self.pathname.iterdir():
                child_dst = self.savepath.joinpath(child_src.name)
                if child_dst.exists() or child_dst.with_suffix(".jpg").exists():
                    pass
                else:
                    copy2(child_src, self.savepath)
                    try:
                        image_path = child_dst.rename(child_dst.with_suffix(".jpg"))
                        with Image.open(image_path) as image:
                            if image.width < image.height:
                                image.close()
                                image_path.unlink()
                    except FileExistsError:
                        pass


def main():
    Spotlight().saveall()


if __name__ == "__main__":
    main()
