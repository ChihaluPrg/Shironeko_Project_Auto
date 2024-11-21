from QuestMovement import *
from Gacha import *
from Quest import *
from Launch import *
from ADB import *
from Mission_Receive import *
from Present import *
from Town import *
from Scratch import *

if __name__ == "__main__":
    """"""
    # adb起動
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

    print("デイリーミッションのクエスト周回の処理をが終了しました\n")

    # ===================================================================================

    print("ミッション報酬受け取り、広告ジュエル回収を行います\n")

    # missionボタンをタップ
    process_mission_receive()
    time.sleep(1)

    print("ミッション報酬受け取り、広告ジュエル回収が終了しました\n")

    # ===================================================================================
    print("スクラッチを削ります\n")

    process_scratch()

    print("スクラッチを削る処理が終了しました\n")
    # ===================================================================================

    print("ガチャを回す処理を開始します\n")

    # 無料ガチャを回す
    process_gacha_all()
    time.sleep(1)

    print("ガチャを回す処理が終了しました\n")
    time.sleep(2)

    # ===================================================================================

    print("プレゼントを受け取る処理を開始します\n")

    process_town()
    time.sleep(1)

    process_present()

    print("プレゼントを受け取る処理が終了しました\n")


















