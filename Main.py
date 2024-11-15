import time
from Launch import launch_game, daily_roulette, apology, close_news, movie_news, boss_weaknesses, boss_weaknesses_ok
from ADB import set_tcpip_mode_without_device_check, connect_device
from Gacha import (process_gacha, ad_free_gacha_chara_path, ad_free_gacha_chara2_path, plus_10_path,
                   gacha_result_path, scroll_right_to_left, tap_gacha_button)

IP_ADDRESS = "192.168.0.103"

if __name__ == "__main__":
    """
    # ADBサーバーの再起動
    set_tcpip_mode_without_device_check()
    connect_device("192.168.0.103")  # 接続したいIPアドレスを指定

#===================================================================================
    
    # 白猫プロジェクトを起動
    print("起動処理を開始します。")
    launch_game()
    time.sleep(25)

    # デイリールーレットのOKボタンをタップ
    if daily_roulette():
        print("デイリールーレットのOKボタンをタップしました")
        time.sleep(2)
    else:
        print("デイリールーレットのOKボタンが表示されませんでした")
        time.sleep(1)

    # お詫びのOKボタンをタップ
    if apology():
        print("お詫びのOKボタンをタップしました")
        time.sleep(2)
    else:
        print("お詫びのOKボタンのタップが表示されませんでした")
        time.sleep(1)

    #ボスの弱点変更
    if boss_weaknesses():
        print("BOSSの弱点変更画面をタップしました")
        time.sleep(2)
    else:
        print("ボスの弱点変更画面が表示されませんでした")
        time.sleep(1)

    if boss_weaknesses_ok():
        print("BOSSの弱点変更ボタンをタップしました")
        time.sleep(2)
    else:
        print("ボスの弱点変更ボタンが表示されませんでした")
        time.sleep(1)

    # ニュースのOKボタンをタップ
    if close_news():
        print("ニュースのOKボタンをタップしました")
        time.sleep(35)
    else:
        print("ニュースのOKボタンが表示されませんでした")
        time.sleep(2)

    # 動画画面を閉じる
    if movie_news():
        print("ムービーのOKボタンをタップしました")
        time.sleep(2)
    else:
        print("ムービーのOKボタンが表示されませんでした")
        time.sleep(2)

    print("起動処理が終了しました。\n")
    time.sleep(1)

    # ===================================================================================

    print("デイリーミッションを開始します。\n")
    time.sleep(1)

    print("デイリーミッションが終了しました。\n")
    time.sleep(1)
"""
    # ===================================================================================

    print("ガチャを回す処理を開始します。\n")
    time.sleep(1)

    if tap_gacha_button():
        print("ガチャボタンをタップしました")
    else:
        print("ガチャボタンが見つかりませんでした")

    time.sleep(2)  # タップ後に少し待機

    process_gacha(ad_free_gacha_chara_path, ad_free_gacha_chara2_path, plus_10_path, gacha_result_path)

    # スクロールを実行し、成功するまで再試行
    while not scroll_right_to_left():
        print("画像が見つかりませんでした。再試行します...")
        time.sleep(2)  # 画像が見つからなかった場合、2秒待機して再試行

    print("スクロールが完了しました")
    time.sleep(1)  # スクロール後に少し待機

    print("ガチャを回す処理が終了しました。\n")
    time.sleep(1)





















