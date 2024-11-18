from OpenCV2 import *

UPDATE_YES_PATH = "img/update_yes.jpg"
UPDATE_PLAYSTORE_PATH = "img/update_playstore.jpg"
UPDATE_PLAYSTORE_OPEN_PATH = "img/update_playstore_open.jpg"
UPDATE_START_PATH = "img/update_start.jpg"


def process_update():
    # 更新する
    update_cfm()
    # Playストアの更新ボタンをタップする
    update_playstore()
    # 更新完了後開くボタンを押す
    update_playstore_open()

def update_cfm():
    while True:
        position = find_template_position(UPDATE_YES_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("新しいバージョンが公開されているためアプリを更新をします")
            time.sleep(1)
            break
        else:
            break

def update_playstore():
    while True:
        position = find_template_position(UPDATE_PLAYSTORE_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("更新ボタンをタップしました（念のため30秒間待機）")
            time.sleep(25)
            break
        else:
            print("更新ボタンが見つかりませんでした")

def update_playstore_open():
    while True:
        position = find_template_position(UPDATE_PLAYSTORE_OPEN_PATH)
        if position:
            print("更新が完了しました")
            time.sleep(1)
            print("白猫プロジェクトを起動します")
            tap_on_device(position[0], position[1])
            time.sleep(1)
            break
        else:
            print("プレイボタンが見つかりませんでした")

def update_start():
    while True:
        position = find_template_position(UPDATE_START_PATH)
        if position:
            tap_on_device(position[0], position[1])
            break
        else:
            print("白猫プロジェクトが起動出来ませんでした")
