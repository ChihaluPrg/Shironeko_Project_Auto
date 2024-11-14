from ADB import check_device_connected, adb_path, device_id
import subprocess

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