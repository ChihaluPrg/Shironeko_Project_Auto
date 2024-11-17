import time
from Advertisement import close_ad
from OpenCV2 import find_template_position, tap_on_device, tap_button_with_retry, scroll_on_device

#ガチャボタン
GACHA_BUTTON_PATH = "img/gacha.jpg"

# スクロールに必要なパラメータをここで定義
SCR_TEMPLATE_PATH = "img/Gacha_Banner.jpg"  # gacha_scr画像のテンプレートパス
START_X = 810  # スクロール開始のX座標
START_Y = 500  # スクロール開始のY座標
END_X = 10  # スクロール終了のX座標
END_Y = 500  # スクロール終了のY座標
DURATION = 430  # スクロールの時間
THRESHOLD = 0.8  # 画像認識の閾値

#無料ガチャ
gacha_ok_template_path = "img/gacha_ok.jpg"
plus10_template_path = "img/plus_10.jpg"
gacha_result_template_path = "img/gacha_result.jpg"
free_gacha_template_path = "img/free_gacha.jpg"
gacha_25_template_path = "img/gacha_25.jpg"

#広告視聴の無料キャラガチャ
AD_FREE_GACHA_CHARA_PATH = "img/ad_free_gacha_chara.jpg"
AD_FREE_GACHA_CHARA2_PATH = "img/ad_free_gacha_chara2.jpg"
PLUS_10_PATH = "img/plus_10.jpg"
GACHA_RESULT_PATH = "img/gacha_result.jpg"

#広告視聴の無料武器ガチャ
BUKI_PATH = "img/buki.jpg"
FREE_BUKI_PATH = "img/free_buki.jpg"
AD_FREE_GACHA_BUKI_PATH = "img/ad_free_gacha_buki.jpg"
AD_FREE_GACHA_BUKI2_PATH = "img/ad_free_gacha_buki2.jpg"
RESULT_BUKI_PATH = "img/result_buki.jpg"
RESULT_BUKI_OK_PATH = "img/buki_result_ok.jpg"
BUKI_RESULT_RETURN_PATH = "img/buki_result_return.jpg"

# スクロールしてガチャ切り替え
def scroll_until_gacha_found():
    while True:
        if scroll_right_to_left():
            # スクロールして画像を探し続ける
            time.sleep(0.2)  # スクロール後に少し待機
        else:
            # 画像が見つかった場合、処理を進める
            break

def scroll_right_to_left():
    position = find_template_position(SCR_TEMPLATE_PATH, THRESHOLD)
    if position:
        # スクロール操作を実行
        scroll_on_device(START_X, START_Y, END_X, END_Y, DURATION)
        return True  # スクロール成功
    return False  # スクロール不要（目標画像が見つかっている）

def process_gacha():
    while True:
        # キャラクターの画像（ad_free_gacha_chara.jpg または ad_free_gacha_chara2.jpg）を見つけてタップ
        chara_position = find_template_position(AD_FREE_GACHA_CHARA_PATH)

        # AD_FREE_GACHA_CHARA_PATH が見つかった場合のみ処理を実行
        if chara_position:
            tap_on_device(chara_position[0], chara_position[1])  # 画像が見つかった場合はタップ
            print("広告視聴ガチャ(キャラ)を回します")
            time.sleep(50)  # 広告の視聴時間（待機）

            # 広告を閉じる
            close_ad()
            time.sleep(15)  # 広告閉じ後に少し待機

            # +10をタップ
            if tap_button_with_retry(PLUS_10_PATH):
                # ガチャ結果をタップ
                tap_button_with_retry(GACHA_RESULT_PATH)
                break
        else:
            # AD_FREE_GACHA_CHARA_PATH が見つからない場合、AD_FREE_GACHA_CHARA2_PATH を確認
            chara_position2 = find_template_position(AD_FREE_GACHA_CHARA2_PATH)
            if chara_position2:
                print("広告視聴ガチャ(キャラ)は既に回されています")
            else:
                print("キャラクターガチャ画像が見つかりませんでした。再試行します...")

    time.sleep(1)
    print("ガチャの種類を切り替えます")
    time.sleep(1)

def find_and_tap(paths, wait_time=0):
    while True:
        for path in paths:
            position = find_template_position(path)
            if position:
                tap_on_device(position[0], position[1])
                if wait_time:
                    time.sleep(wait_time)
                return position
        print("画像が見つかりません。再試行します...")
        time.sleep(2)  # 再試行までの待機

def tap_gacha_button():
    while True:
        position = find_template_position(GACHA_BUTTON_PATH)
        if position:
            # 画像が見つかればその位置をタップ
            tap_on_device(position[0], position[1])
            print("ガチャ画面に移動します")
            time.sleep(3)  # ガチャ画面に移動した後、少し待機
            return True
        else:
            # 画像が見つからなければ再試行（待機時間を追加してリトライ）
            print("ガチャボタンが見つかりませんでした。再試行します...")
            time.sleep(1)  # 再試行前に待機時間を設ける

"""
========================================== 武器ガチャ ==========================================   
"""

def process_buki_gacha():

    # free_buki.jpg または buki.jpg のどちらかを探してタップ
    target_position = find_and_tap([FREE_BUKI_PATH, BUKI_PATH])
    if not target_position:
        print("武器ガチャ画像が見つかりませんでした。終了します")
        return

    time.sleep(2)  # 少し待機

    # 広告付きガチャの確認 (AD_FREE_GACHA_BUKI_PATHのみを確認)
    ad_position = find_template_position(AD_FREE_GACHA_BUKI_PATH)
    if ad_position:
        tap_on_device(ad_position[0], ad_position[1])  # 広告ガチャをタップ
        print("広告視聴ガチャ(武器)を回します")
        time.sleep(50)  # 広告視聴時間（待機）

        # 広告を閉じる
        close_ad()
        time.sleep(20)  # 広告閉じ後に少し待機

        # 結果画面の操作
        handle_gacha_result(RESULT_BUKI_PATH, RESULT_BUKI_OK_PATH, BUKI_RESULT_RETURN_PATH)
    else:
        # AD_FREE_GACHA_BUKI_PATHが見つからない場合、AD_FREE_GACHA_BUKI2_PATHを確認
        ad_position2 = find_template_position(AD_FREE_GACHA_BUKI2_PATH)
        if ad_position2:
            print("広告視聴ガチャ(武器)は既に回されています")
        else:
            print("広告ガチャの画像が見つかりませんでした。処理をスキップします")

def handle_gacha_result(result_path, ok_path, return_path):
    if tap_button_with_retry(result_path):
        tap_button_with_retry(ok_path)
        tap_button_with_retry(return_path)

"""
========================================== その他ガチャ ==========================================   
"""

def tap_free_gacha_no_ad():

    while True:
        # free_gacha.jpg が見つかればタップ
        position_free_gacha = find_template_position(free_gacha_template_path)
        if position_free_gacha:
            tap_on_device(position_free_gacha[0], position_free_gacha[1])
            print("無料ガチャ(広告なし)を回します")

            # === gacha_ok.jpg をタップ ===
            wait_and_tap_gacha_ok()  # gacha_ok.jpg を見つかるまでタップする関数を呼び出し
            time.sleep(15)

            wait_and_tap_gacha_10()

            wait_and_tap_gacha_result()
            return True  # タップしたら終了

        # free_gacha.jpg が見つからなければ gacha_25.jpg を確認
        position_gacha_25 = find_template_position(gacha_25_template_path)
        if position_gacha_25:
            print("無料ガチャ(広告なし)は既に引いてあります")
            return False  # スキップしたら終了

        # どちらも見つからない場合は少し待って再確認

def wait_and_tap_gacha_ok():
    while True:
        position_gacha_ok = find_template_position(gacha_ok_template_path)
        if position_gacha_ok:
            tap_on_device(position_gacha_ok[0], position_gacha_ok[1])
            break  # ボタンが見つかればループ終了
        else:
            print("はいボタンが見つかりません。再試行します...")
            time.sleep(1)  # 少し待機して再試行

def wait_and_tap_gacha_10():
    while True:
        position_gacha_10 = find_template_position(plus10_template_path)
        if position_gacha_10:
            tap_on_device(position_gacha_10[0], position_gacha_10[1])
            break  # ボタンが見つかればループ終了
        else:
            print("限界突破が見つかりません。再試行します...")
            time.sleep(1)  # 少し待機して再試行

def wait_and_tap_gacha_result():
    while True:
        position_gacha_result = find_template_position(gacha_result_template_path)
        if position_gacha_result:
            tap_on_device(position_gacha_result[0], position_gacha_result[1])
            break  # ボタンが見つかればループ終了
        else:
            print("戻るボタンが見つかりません。再試行します...")
            time.sleep(1)  # 少し待機して再試行

