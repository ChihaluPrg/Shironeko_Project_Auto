import time
from Advertisement import close_ad
from OpenCV2 import tap_on_device, find_template_position, tap_button_with_retry, tap_button_with_retry_restricted

mission_template_path = "img/mission.jpg"  # missionボタンのテンプレート画像
no_mission_template_path = "img/no_mission.jpg"  # no_missionボタンのテンプレート画像

# ボタンを探してタップする関数
def tap_mission(mission_template_path):
    position = find_template_position(mission_template_path)
    if position:
        tap_on_device(position[0], position[1])
        return True
    print("ボタンが見つかりませんでした。")
    return False

# no_mission.jpgがある場合は処理をスキップ
def check_no_mission(no_mission_template_path):
    position_no_mission = find_template_position(no_mission_template_path)
    return position_no_mission is not None

# missionボタンをタップする処理（no_missionが見つかるとスキップ）
def tap_mission_button(mission_template_path, no_mission_template_path):
    # no_mission.jpg が見つかると、処理をスキップする
    if check_no_mission(no_mission_template_path):
        return False

    # no_mission.jpg が見つからなければ、通常通りボタンをタップ
    position = find_template_position(mission_template_path)
    if position:
        tap_on_device(position[0], position[1])
        time.sleep(2)  # 少し待機
        return True
    else:
        return False

# mission_get～mission_daily_rouletteの繰り返し処理
def collect_mission_rewards():
    while True:
        # mission_get.jpg をタップ
        mission_get_template_path = "img/mission_get.jpg"
        if not tap_button_with_retry_restricted(mission_get_template_path):
            break  # 見つからなければループを終了

        # mission_ok.jpg をタップ
        mission_ok_template_path = "img/mission_ok.jpg"
        tap_button_with_retry_restricted(mission_ok_template_path)

        # mission_daily_roulette.jpg をタップ
        mission_daily_roulette_template_path = "img/mission_daily_roulette.jpg"
        tap_button_with_retry_restricted(mission_daily_roulette_template_path)

# mission_watch～mission_ok の繰り返し処理
def watch_and_close_ads():
    while True:
        # mission_watch.jpg をタップ
        mission_watch_template_path = "img/mission_watch.jpg"
        position = find_template_position(mission_watch_template_path)
        if not position:
            break  # mission_watch が見つからなければ終了

        tap_on_device(position[0], position[1])
        time.sleep(45)  # 45秒待機（広告の視聴待機時間）

        # 広告の閉じる処理
        close_ad()  # close_ad関数で広告を閉じる処理を実行
        time.sleep(3)

        # mission_ok.jpg をタップ
        mission_ok_template_path = "img/mission_ok.jpg"
        position = find_template_position(mission_ok_template_path)
        if position:
            tap_on_device(position[0], position[1])
            time.sleep(2)

# close_missionボタンをタップして終了する処理
def close_mission():
    close_mission_template_path = "img/close_mission.jpg"  # close_missionボタンのテンプレート画像
    position = find_template_position(close_mission_template_path)
    if position:
        tap_on_device(position[0], position[1])
    else:
        print("close_missionボタンが見つかりませんでした。")
    time.sleep(3)