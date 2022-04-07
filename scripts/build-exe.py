import pathlib
import shutil

import PyInstaller.__main__

if __name__ == '__main__':
    APP_NAME = r'WS2DB'
    APP_DIR = pathlib.PureWindowsPath(__file__).parents[1]
    APP_PATH = APP_DIR.joinpath(f'{APP_NAME}', f'{APP_NAME}.py')
    ICON_PATH = APP_DIR.joinpath(r'icons', '96x96.ico')
    DIST_DIR = pathlib.WindowsPath(APP_DIR.joinpath(r'release'))
    try:
        DIST_DIR.mkdir(exist_ok=True)
        PyInstaller.__main__.run([
            fr'{APP_PATH}',
            '-i',
            fr'{ICON_PATH}',
            '-n',
            fr'{APP_NAME}',
            '--distpath',
            fr'{DIST_DIR}',
            '--clean',
            '--noconsole',
            '--noconfirm'
        ])
        shutil.make_archive(fr'{APP_NAME}', 'zip', root_dir=fr'{DIST_DIR}')
    except FileExistsError as e:
        print('FAILED', e)
