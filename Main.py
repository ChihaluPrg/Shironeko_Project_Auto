import cv2
import subprocess
import time
import os
from Launch import launch_game
from ADB import set_tcpip_mode_without_device_check, connect_device, capture_screen, check_device_connected



if __name__ == "__main__":
    launch_game()