from OpenCV2 import *

SCRATCH_PATH = "img/scratch.jpg"
SCRATCH_OK_PATH = "img/scratch_ok.jpg"

def scratch():
    while True:
        position = find_template_position(SCRATCH_PATH)
        if position:
            print("スクラッチチャンスを獲得しました")
            break
        else:
            time.sleep(1)
            break

    while True:
        position = find_template_position(SCRATCH_PATH)
        if position:
            tap_on_device(position[0], position[1])
            return True
        else:
            time.sleep(1)
            break