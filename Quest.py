from Countdown import countdown
from OpenCV2 import *
from Scratch import *

QUEST_3_PATH = "img/Quest_3.jpg"
QUEST_3_2_PATH = "img/Quest_3-2.jpg"
QUEST_ASTRO_PATH = "img/quest_asutora.jpg"
GO_PATH = "img/go.jpg"
QUEST2_PATH = "img/quest2.jpg"
RETORY_PATH = "img/retry.jpg"
RETORY_YES_PATH = "img/retry_yes.jpg"
QUEST_END_PATH = "img/quest_end.jpg"
SHINMITUDO_PATH = "img/shinmitudo_result_ok.jpg"
QUEST_PATH = "img/quest_bouken3.jpg"

DURATION = 1500
THRESHOLD = 0.8
START_X = 500
START_Y = 1000
END_X = 500
END_Y = 1700

QUEST_3_X_PATH = 320
QUEST_3_Y_PATH = 800

QUEST_3_2_X_PATH = 544
QUEST_3_2_Y_PATH = 1461

def process_quest():
    while True:
        # 最初に QUEST_3_PATH を探す
        position1 = find_template_position(QUEST_3_PATH)
        position2 = find_template_position(QUEST_3_2_PATH)
        position3 = find_template_position(QUEST_PATH)
        if position1:
            tap_on_device(QUEST_3_X_PATH, QUEST_3_Y_PATH)  # QUEST_3_PATH 用の座標でタップ
            print("quest_3.jpg をタップしました")
            time.sleep(1)
            break  # 次の処理に進む
        elif position2:
            tap_on_device(QUEST_3_2_X_PATH, QUEST_3_2_Y_PATH)  # QUEST_3_2_PATH 用の座標でタップ
            print("quest_3-2.jpg をタップしました")
            time.sleep(1)
            break  # 次の処理に進む
        elif position3:
            break
        else:
            print("quest_3.jpg または quest_3-2.jpg が見つかりませんでした。再試行します...")
            time.sleep(2)

    while True:
        position = find_template_position(QUEST_ASTRO_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("quest_asutora.jpgをタップしました")
            time.sleep(0.5)
            break  # 次の処理へ進む
        else:
            print("quest_asutora.jpgが見つかりませんでした。再試行します...")
            time.sleep(2)

    while True:
        position = find_template_position(GO_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("go.jpgをタップしました")
            countdown(10)
            break  # 次の処理へ進む
        else:
            print("go.jpgが見つかりませんでした。再試行します...")

    while True:
        position = find_template_position(QUEST2_PATH)
        if position:
            print("QUEST2_PATH が見つかりました。スクロールを実行します...")
            scroll_on_device(START_X, START_Y, END_X, END_Y, DURATION)
            countdown(13)  # スクロール後に少し待機
            break
        else:
            print("QUEST2_PATH が見つかりませんでした。再試行します...")
            time.sleep(1)  # 見つからない場合に少し待機

    scratch()

    while True:
        position = find_template_position(SHINMITUDO_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("キャラの親密度が深まりました")
            time.sleep(1)
            break
        else:
            break

    while True:
        position = find_template_position(RETORY_PATH)
        if position:
            tap_on_device(position[0], position[1])
            time.sleep(1)
            break
        else:
            print("RETORY_PATHが見つかりませんでした。再試行します...")

    while True:
        position = find_template_position(RETORY_YES_PATH)
        if position:
            tap_on_device(position[0], position[1])
            countdown(10)
            break
        else:
            print("RETORY_YES_PATHが見つかりませんでした。再試行します...")

    for i in range(9):

        countdown(10)
        while True:
            position = find_template_position(QUEST2_PATH)
            if position:
                print("QUEST2_PATH が見つかりました。スクロールを実行します...")
                scroll_on_device(START_X, START_Y, END_X, END_Y, DURATION)
                countdown(10)  # スクロール後に少し待機
                break
            else:
                print("QUEST2_PATH が見つかりませんでした。再試行します...")

        while True:
            position = find_template_position(SHINMITUDO_PATH)
            if position:
                tap_on_device(position[0], position[1])
                print("キャラの親密度が深まりました")
                time.sleep(1)
                break
            else:
                break

        scratch()

        if i < 8:
            while not tap_button_with_retry(RETORY_PATH):
                print("再挑戦ボタンが見つかりません。再試行します...")

            while not tap_button_with_retry(RETORY_YES_PATH):
                print("はいボタンが見つかりません。再試行します...")
            print(f"{i + 1}回目の処理が終わりました{i + 1}回目の処理を始めます")
        else:
            while not tap_button_with_retry(QUEST_END_PATH):
                print("OKボタンが見つかりません。再試行します...")

    print("クエストを10回クリアしました")