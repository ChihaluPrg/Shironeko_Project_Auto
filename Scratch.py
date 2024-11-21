from pyautogui import press

from Advertisement import close_ad
from Countdown import countdown
from OpenCV2 import *
from Print import ERROR_MESSAGE

# 周回用
SCRATCH_PATH = "img/scratch.jpg"
SCRATCH_OK_PATH = "img/scratch_ok.jpg"

# 削る用
SCRATCH_GET_PATH = "img/bouken.jpg"
SCRATCH_CHANCE_PATH = "img/scratch_chance.jpg"
SCRATCH_WATCH_PATH = "img/scratch_watch.jpg"
SCRATCH_OK2_PATH = "img/scratch_bonanza_ok.jpg"
SCRATCH_RETURN_PATH = "img/scratch_return.jpg"
SCRATCH_CLOSE_PATH = "img/close_mission.jpg"

def scratch():
    while True:
        position = find_template_position(SCRATCH_PATH)
        if position:
            print("スクラッチチャンスを獲得しました")
            break
        else:
            time.sleep(1)
            return True

    while True:
        position = find_template_position(SCRATCH_OK_PATH)
        if position:
            tap_on_device(position[0], position[1])
            break
        else:
            time.sleep(1)
            print("OKボタンが見つかりません")

def process_scratch():
    # 1. 冒険ボタンを探す
    position = find_template_position(SCRATCH_GET_PATH)
    if position:
        tap_on_device(position[0], position[1])
        time.sleep(2)
    else:
        print("冒険ボタン" + ERROR_MESSAGE)
        return  # 処理を終了

    # 2. チャンスボタンを探す
    position2 = find_template_position(SCRATCH_CHANCE_PATH)
    if position2:
        tap_on_device(position2[0], position2[1])
        time.sleep(2)
    else:
        print("スクラッチはありません")
        return  # 処理を終了

    # 3. 動画を見るボタンを探す
    retry_count = 0
    max_retries = 10
    while retry_count < max_retries:
        position3 = find_template_position(SCRATCH_WATCH_PATH)
        if position3:
            tap_on_device(position3[0], position3[1])
            countdown(50)
            close_ad()
            time.sleep(2)
            break
        else:
            retry_count += 1
            print(f"動画を見るボタン{ERROR_MESSAGE} (試行回数: {retry_count}/{max_retries})")
    else:
        print("動画を見るボタンが見つからないため終了します。")
        return

    # 4. OKボタンを探す
    while True:
        position4 = find_template_position(SCRATCH_OK2_PATH)
        if position4:
            tap_on_device(position4[0], position4[1])
            time.sleep(2)
            break
        else:
            print("OKボタン" + ERROR_MESSAGE)
            break

    # 5. 戻るボタンを探す
    while True:
        position5 = find_template_position(SCRATCH_RETURN_PATH)
        if position5:
            tap_on_device(position5[0], position5[1])
            break
        else:
            print("戻るボタン" + ERROR_MESSAGE)

    # 6. 閉じるボタンを探す
    while True:
        position5 = find_template_position(SCRATCH_CLOSE_PATH)
        if position5:
            tap_on_device(position5[0], position5[1])
            break
        else:
            print("閉じるボタン" + ERROR_MESSAGE)
