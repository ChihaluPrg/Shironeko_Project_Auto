from OpenCV2 import find_template_position, tap_on_device
import time

AD_CLOSE_IMG_PATH = "img/ad_close23.jpg"

def close_ad():
    ad_closed = False
    attempts = 0  # 最大試行回数を追跡
    threshold = 0.9  # 認識度の閾値を設定
    while attempts < 4 and not ad_closed:
        attempts += 1
        ad_found = False  # 1回の試行内で広告が見つかったかどうか

        # 広告閉じボタンを1回目または再試行で確認
        time.sleep(50)
        for i in range(1, 27):
            ad_close_template_path = f"img/ad_close{i}.jpg"
            position = find_template_position(ad_close_template_path, threshold=threshold)
            if position:
                tap_on_device(position[0], position[1])
                ad_found = True
                ad_closed = True
                break  # ボタンが見つかればループを抜けて次の処理に進む

        if ad_found:
            # 見つかった場合、10秒後に再確認
            print(f"{attempts}個目の広告を閉じました。10秒後に再度広告の閉じるボタンを確認します...")
            time.sleep(10)
        elif attempts < 4:
            # 見つからなければ再試行
            print(f"{attempts}個目で広告の閉じるボタンが見つかりませんでした。再試行します...")
            time.sleep(5)  # 再試行の前に少し待機
        else:
            # 最後の試行でも見つからなければ終了
            print(f"{attempts}個目で広告の閉じるボタンが見つかりませんでした。再試行はしません...")
            break  # 4回試行しても見つからなかった場合は終了

"""
ポインタ待ち

def close_ad_img():
    position = find_template_position(AD_CLOSE_IMG_PATH, threshold=0.9)
    if position:
        tap_on_device(position[0], position[1])
    else:
        print()

"""