import subprocess
from ADB import check_device_connected, adb_path, device_id
from OpenCV2 import find_template_position, tap_on_device

# 画像テンプレートのパス
DAILY_ROULETTE_TEMPLATE_PATH = "img/daily_roulette.jpg"
APOLOGY_TEMPLATE_PATH = "img/apology.jpg"
CLOSE_NEWS_TEMPLATE_PATH = "img/news_close.jpg"
CLOSE_MOVIE_TEMPLATE_PATH = "img/movie_close.jpg"
BOSS_WEAKNESSES_TEMPLATE_PATH = "img/boss_weaknesses.jpg"
BOSS_WEAKNESSES_OK_TEMPLATE_PATH = "img/boss_weaknesses_ok.jpg"


# 白猫プロジェクトを起動する
def launch_game():
    if check_device_connected():
        result = subprocess.run([adb_path, "-s", device_id, "shell", "monkey", "-p", "jp.colopl.wcat", "-c",
                                 "android.intent.category.LAUNCHER", "1"], capture_output=True, text=True)
        if result.returncode != 0:
            print("アプリの起動に失敗しました。\n")
            return False
        print("白猫プロジェクトを起動しました。\n")
        return True
    return False


# 共通のタップ処理関数
def tap_template(template_path, description):
    position = find_template_position(template_path)
    if position:
        tap_on_device(position[0], position[1])
        print(f"{description}をタップしました。\n")
        return True
    return False  # 見つからなければ何もせず、Falseを返す


# 各タップ関数
def daily_roulette():
    return tap_template(DAILY_ROULETTE_TEMPLATE_PATH, "デイリールーレットのOKボタン")

def apology():
    return tap_template(APOLOGY_TEMPLATE_PATH, "お詫びのOKボタン")

def boss_weaknesses():
    return tap_template(BOSS_WEAKNESSES_TEMPLATE_PATH, "ボスの弱点変更")

def boss_weaknesses_ok():
    return tap_template(BOSS_WEAKNESSES_OK_TEMPLATE_PATH, "ボスの弱点変更のOKボタン")

def close_news():
    return tap_template(CLOSE_NEWS_TEMPLATE_PATH, "ニュースの閉じるボタン")

def movie_news():
    return tap_template(CLOSE_MOVIE_TEMPLATE_PATH, "動画の閉じるボタン")
