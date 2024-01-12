import pathlib
import shutil

import PyInstaller.__main__

if __name__ == "__main__":
    APP_NAME = r"WS2DB"
    APP_DIR = pathlib.PureWindowsPath(__file__).parents[1]
    APP_PATH = APP_DIR.joinpath(f"{APP_NAME}", f"{APP_NAME}.py".lower())
    ICON_PATH = APP_DIR.joinpath(r"icons", "spotlight.ico")
    DIST_DIR = pathlib.WindowsPath(APP_DIR.joinpath(r"release"))
    try:
        DIST_DIR.mkdir(exist_ok=True)
        PyInstaller.__main__.run(
            [
                rf"{APP_PATH}",
                "-i",
                rf"{ICON_PATH}",
                "-n",
                rf"{APP_NAME}",
                "--distpath",
                rf"{DIST_DIR}",
                "--clean",
                "--noconsole",
                "--noconfirm",
            ]
        )
        shutil.make_archive(rf"{APP_NAME}", "zip", root_dir=rf"{DIST_DIR}")
    except FileExistsError as e:
        print("FAILED", e)
