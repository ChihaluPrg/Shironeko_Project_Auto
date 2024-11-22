
from Advertisement import close_ad
from OpenCV2 import *
from Countdown import countdown

MISSION_PATH = "img/mission.jpg"
NO_MISSION_PATH = "img/no_mission.jpg"
GET_PATH = "img/mission_get.jpg"
TRE_ROULETEE_PATH = "img/daily_roulette.jpg"
TRE_DAILY_PATH = "img/mission_daily_roulette.jpg"
TRE_COMP_PATH = "img/mission_treasure_comp.jpg"
WATCH_PATH = "img/mission_watch.jpg"
WATCH_MISSION_GET_PATH = "img/mission_watch_get.jpg"
WATCH_WARCH_COMP_PATH = "img/mission_watch_comp.jpg"
CLOSE_MISSION_PATH = "img/close_mission.jpg"


def process_mission_receive():
    # ミッション画面を開く
    if mission_tap():  # True が返ってきた場合、すべての処理を終了
        print("ミッションが達成されていないため、処理を終了します。")
        return
    time.sleep(2)

    # トレジャーソウル報酬の処理
    treasure_soul()
    time.sleep(2)

    # 動画視聴報酬の処理
    watch_movie()
    time.sleep(1)

    # ミッション画面を閉じる
    close_mission()
    print("すべてのミッション処理が完了しました。")

def mission_tap():
    while True:
        position = find_template_position(MISSION_PATH)
        position2 = find_template_position(NO_MISSION_PATH)

        if position:
            tap_on_device(position[0], position[1])
            print("ミッションボタンをタップしました")
            return False  # ミッションがあるので False を返す

        elif position2:
            print("達成されているミッションはありません")
            return True  # ミッションがない場合 True を返す

        else:
            print("ミッションボタンが見つかりませんでした。再試行します...")

def treasure_soul():
    for i in range(3):
        try:
            # ゲットボタンの位置を探す
            position = find_template_position(GET_PATH)

            if position:
                # ゲットボタンが見つかったらタップ
                tap_on_device(position[0], position[1])
                time.sleep(2)  # 少し待機

                # ミッション獲得ボタンを見つけるまでループ
                while True:
                    position2 = find_template_position(TRE_ROULETEE_PATH)
                    if position2:
                        # ミッション獲得ボタンが見つかったらタップ
                        tap_on_device(position2[0], position2[1])
                        break  # ミッション獲得が成功したらループを抜ける
                    else:
                        print("ルーレットボタンが見つかりません。再試行します。")
                        time.sleep(2)  # 少し待機して再試行

                # デイリーミッション獲得ボタンを見つけるまでループ
                while True:
                    position3 = find_template_position(TRE_DAILY_PATH)
                    if position3:
                        # デイリーミッション獲得ボタンが見つかったらタップ
                        tap_on_device(position3[0], position3[1])
                        break  # ミッション獲得が成功したらループを抜ける
                    else:
                        print("デイリーミッションボタンが見つかりません。再試行します。")
                        time.sleep(2)  # 少し待機して再試行
            else:
                # ゲットボタンが見つからなかった場合
                print(f"ゲットボタンが{i + 1}回目の試行で見つかりませんでした。")
                return  # 処理を終了（失敗として返す）

        except Exception as e:
            # 予期しないエラーをキャッチ
            print(f"エラーが発生しました: {e}")
            return False  # エラーが発生した場合も終了

    # 全ての試行が正常に完了した場合
    return True


def watch_movie():
    time.sleep(2)
    for i in range(3):  # 最大6回試行
        print(f"=== {i+1}回目の試行 ===")  # 試行のログを追加
        try:
            # 動画視聴ボタンの位置を探す
            position = find_template_position(WATCH_PATH)

            if position:
                # 動画視聴ボタンが見つかったらタップ
                tap_on_device(position[0], position[1])
                print(f"{i+1}回目: 動画を視聴します")
                countdown(50)  # 50秒カウントダウン（動画視聴をシミュレート）
                close_ad()  # 広告を閉じる
                time.sleep(2)  # 少し待機

                # ミッション獲得ボタンを見つけるまでループ
                while True:
                    position2 = find_template_position(WATCH_MISSION_GET_PATH)

                    if position2:
                        # ミッション獲得ボタンが見つかったらタップ
                        tap_on_device(position2[0], position2[1])
                        print(f"{i+1}回目: ミッション獲得ボタンをタップしました。")
                        break  # ミッション獲得が成功したらループを抜ける
                    else:
                        print("ミッション獲得ボタンが見つかりません。再試行します。")
                        time.sleep(2)  # 少し待機して再試行

            else:
                # 動画視聴ボタンが見つからない場合
                print(f"{i+1}回目: 動画視聴ボタンが見つかりませんでした。終了します。")
                return  # 処理を終了

        except Exception as e:
            # 予期しないエラーをキャッチ
            print(f"エラーが発生しました: {e}")
            return False  # 処理を終了

    # 全ての試行が正常に完了した場合
    print("全ての試行が完了しました。")
    return True




def close_mission():
    while True:
        position = find_template_position(CLOSE_MISSION_PATH)
        if position:
            tap_on_device(position[0], position[1])
            time.sleep(2)
            break
        else:
            print("閉じるボタンが見つかりませんでした。\n再試行します...")




