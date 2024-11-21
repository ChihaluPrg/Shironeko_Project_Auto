import time

from OpenCV2 import *
from Print import ERROR_MESSAGE


PRESENT_PATH = "img/present.jpg"
PRESENT_ALL_PATH = "img/page_all.jpg"
PRESENT_OK_PATH = "img/present_ok.jpg"
PRESENT_YES_PATH = "img/present_yes.jpg"
PRESENT_RETURN_PATH = "img/present_return.jpg"

def process_present():
    while True:
        position = find_template_position(PRESENT_PATH)
        if position :
            tap_on_device(position[0], position[1])
            break
        else:
            print("プレゼントボタンが見つかりませんでした。再試行します...")

    while True:
        position = find_template_position(PRESENT_ALL_PATH)
        if position :
            tap_on_device(position[0], position[1])
            time.sleep(2)
            break
        else:
            print("受け取りボタンが見つかりませんでした。再試行します...")

    while True:
        position = find_template_position(PRESENT_YES_PATH)
        if position :
            tap_on_device(position[0], position[1])
            time.sleep(1)
            break
        else:
            print("はいボタン" + ERROR_MESSAGE)

    while True:
        position = find_template_position(PRESENT_OK_PATH)
        if position :
            tap_on_device(position[0], position[1])
            time.sleep(1)
            break
        else:
            print("OKボタン" + ERROR_MESSAGE)

    while True:
        position = find_template_position(PRESENT_RETURN_PATH)
        if position :
            tap_on_device(position[0], position[1])
            break
        else:
            print("戻るボタン" + ERROR_MESSAGE)

