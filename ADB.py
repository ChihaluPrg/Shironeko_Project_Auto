import cv2
import subprocess
import time
import os

adb_path = r"C:\Program Files\BlueStacks_nxt\adb.exe"
device_id = "192.168.0.103:5555"  # Wi-Fi接続のIPアドレスとポート番号を指定
adb_command = "adb"
port = 5555  # 使用するポート番号

def set_tcpip_mode_without_device_check(port=5555):
    """直接TCP/IPモードに設定する関数"""
    try:
        # ADBサーバーを起動
        print("ADBサーバーを起動します\n")
        subprocess.run([adb_command, "start-server"], check=True)
        time.sleep(0.5)

        # TCP/IPモードをポートで設定
        print(f"直接TCP/IPモードをポート {port} で設定します...\n")
        subprocess.run([adb_command, "tcpip", str(port)], check=True)
        time.sleep(0.5)

        print(f"\nポート {port} でTCP/IPモードに設定しました。\n")
        time.sleep(0.5)
    except subprocess.CalledProcessError:
        print("TCP/IP設定中にエラーが発生しました。adbのパスを確認してください。\n")
        time.sleep(0.5)

def connect_device(ip_address, port=5555):
    """指定したIPアドレスとポートにADB接続を試みる関数"""
    try:
        # 指定したIPアドレスに接続
        print(f"{ip_address}:{port} に接続を試みます...\n")
        result = subprocess.run([adb_command, "connect", f"{ip_address}:{port}"], capture_output=True, text=True)
        time.sleep(0.5)
        # 接続結果をチェック
        if "connected" in result.stdout:
            print(f"{ip_address} に接続されました。\n")
            time.sleep(0.5)
            return True
        else:
            print(f"{ip_address} に接続できませんでした。エラー: {result.stderr}\n")
            time.sleep(0.5)
            return False
    except subprocess.CalledProcessError:
        print("接続中にエラーが発生しました。\n")
        time.sleep(0.5)
        return False

# ADB経由でデバイスの接続を確認する関数
def check_device_connected():
    result = subprocess.run([adb_path, "devices"], capture_output=True, text=True)
    if device_id not in result.stdout:
        print(f"デバイス {device_id} が見つかりません。adb devicesでIDを確認してください。\n")
        time.sleep(0.5)
        return False
    return True


# ADB経由で画面キャプチャ取得
def capture_screen():
    if not check_device_connected():
        return False

    # 画面キャプチャの保存先を指定
    subprocess.run([adb_path, "-s", device_id, "shell", "screencap", "-p", "/sdcard/screen.png"])

    # -q オプションで進捗メッセージを非表示にする
    subprocess.run([adb_path, "-s", device_id, "pull", "-q", "/sdcard/screen.png", "screen.png"])

    return os.path.exists("screen.png")

# スクロール操作を実行する関数
def scroll_on_device(start_x, start_y, end_x, end_y, duration=300):
    """
    start_x, start_y: スクロール開始の座標
    end_x, end_y: スクロール終了の座標
    duration: スクロールにかける時間（ミリ秒単位）
    """
    if not check_device_connected():
        return False
    # adbコマンドでドラッグ操作（スクロール）を実行
    subprocess.run(
        [adb_path, "-s", device_id, "shell", "input", "swipe", str(start_x), str(start_y), str(end_x), str(end_y),
         str(duration)])
    return True