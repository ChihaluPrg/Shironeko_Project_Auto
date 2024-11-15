import cv2
import subprocess
import time
import os
from Launch import launch_game
from ADB import set_tcpip_mode_without_device_check, connect_device

if __name__ == "__main__":

    # 白猫プロジェクトを起動
    launch_game()
    time.sleep(2)
