from QuestMovement import *
from Gacha import *
from Quest import *
from Mission import *
from Launch import *
from ADB import *
from Update_apk import *

if __name__ == "__main__":

    process_adb()
    time.sleep(1)

    #===================================================================================

    process_launch()
    time.sleep(2)

    print("起動処理が終了しました。\n")
    time.sleep(1)

    # ===================================================================================

    print("デイリーミッションのクエスト周回の処理を開始します\n")

    process_bouken()
    time.sleep(2)

    process_quest()
    time.sleep(2)

    process_mission()
    time.sleep(2)

    print("デイリーミッションのクエスト周回の処理をが終了しました\n")

    # ===================================================================================

    print("デイリーミッションを開始します。\n")
    time.sleep(1)

    print("ミッション報酬受け取り、広告ジュエル回収を行います\n")
    time.sleep(1)

    # missionボタンをタップ
    process_mission()
    time.sleep(1)

    print("デイリーミッションが終了しました。\n")

    # ===================================================================================

    print("ガチャを回す処理を開始します\n")


    #ガチャの画面に移動
    tap_gacha_button()

    # 広告視聴の無料キャラガチャを回す
    process_gacha()

    # ガチャの種類を変えるためにスクロールを実行
    scroll_until_gacha_found()

    # 広告なしの無料ガチャを回す
    tap_free_gacha_no_ad()
    time.sleep(1)

    # 広告視聴の無料武器ガチャを実行
    process_buki_gacha()
    time.sleep(1)

    print("ガチャを回す処理が終了しました\n")
    time.sleep(2)




















