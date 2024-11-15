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
free_gacha_path = "img/free_gacha.jpg"
free_gacha_25_path = "img/gacha_25.jpg"
free_gacha_ok_template_path = "img/gacha_ok.jpg"
plus10_template_path = "img/+10.jpg"
free_gacha_result_template_path = "img/gacha_result.jpg"

#広告視聴の無料ガチャ
ad_free_gacha_chara_path = "img/ad_free_gacha_chara.jpg"
ad_free_gacha_chara2_path = "img/ad_free_gacha_chara2.jpg"
plus_10_path = "img/+10.jpg"
gacha_result_path = "img/gacha_result.jpg"

#スクロールしてガチャ切り替え
def scroll_right_to_left():
    position = find_template_position(SCR_TEMPLATE_PATH, THRESHOLD)
    if position:
        # スクロール操作を実行
        scroll_on_device(START_X, START_Y, END_X, END_Y, DURATION)
        return True
    return False

# free_gacha と gacha_25 の存在を確認して判定
def check_gacha_buttons(free_gacha_template_path, gacha25_template_path):
    free_gacha_position = find_template_position(free_gacha_template_path)
    gacha25_position = find_template_position(gacha25_template_path)
    return free_gacha_position if free_gacha_position and not gacha25_position else None

def process_gacha(ad_free_gacha_chara_path, ad_free_gacha_chara2_path, plus_10_path, gacha_result_path):
    # ad_free_gacha_chara.jpgとad_free_gacha_chara2.jpgのどちらがあるか確認
    position_chara = None
    position_chara2 = None

    # どちらかが見つかるまで再試行
    while not position_chara and not position_chara2:
        position_chara = find_template_position(ad_free_gacha_chara_path)
        position_chara2 = find_template_position(ad_free_gacha_chara2_path)

        if not position_chara and not position_chara2:
            print("どちらの画像も見つかりませんでした。再試行します...")

    if position_chara:
        tap_on_device(position_chara[0], position_chara[1])
        time.sleep(50)

        # 広告を閉じる
        close_ad()
        time.sleep(15)

        # +10.jpgをタップ
        if tap_button_with_retry(plus_10_path):
            # gacha_result.jpgをタップ
            tap_button_with_retry(gacha_result_path)

    elif position_chara2:
        time.sleep(0)


def tap_gacha_button():
    position = find_template_position(GACHA_BUTTON_PATH)

    if position:
        # 画像が見つかればその位置をタップ
        tap_on_device(position[0], position[1])
        return True
    else:
        # 画像が見つからなければタップせずにFalseを返す
        return False