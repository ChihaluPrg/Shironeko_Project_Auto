import time

from Gacha import (process_gacha, scroll_until_gacha_found, tap_gacha_button, process_buki_gacha,
                   tap_free_gacha_no_ad)

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

    print("ミッション報酬受け取り、広告ジュエル回収を行います\n")
    time.sleep(1)

    # missionボタンをタップ
    if tap_mission_button(mission_template_path, no_mission_template_path):
        # mission_get～mission_daily_roulette の繰り返し処理
        collect_mission_rewards()

        # mission_watch～mission_ok の繰り返し処理
        watch_and_close_ads()

        # close_missionボタンをタップして終了
        close_mission()

    print("デイリーミッションが終了しました。\n")
    time.sleep(1)
"""
    # ===================================================================================

    print("デイリーミッションのクエスト周回の処理を開始します")

    print("デイリーミッションのクエスト周回の処理をが狩猟しました\n")

    print("ガチャを回す処理を開始します")
    time.sleep(1)

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




















