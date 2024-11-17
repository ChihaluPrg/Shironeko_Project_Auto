import time
from OpenCV2 import *

BOUKEN_PATH = "img/bouken.jpg"
MAIN_STORY_PATH = "img/main_story.jpg"
NEW_WORLD_PATH = "img/new_world.jpg"
CHAPTER_ZERO_TITLE_PATH = "img/Chapter Zero_Title.jpg"
CHAPTER_ZERO_TITLE2_PATH = "img/Chapter Zero_Title2.jpg"
GO_QUEST_PATH = "img/go_quest.jpg"
DECISIVE_BATTLE_PATH = "img/Decisive_Battle.jpg"
DECISIVE_BATTLE2_PATH = "img/Decisive_Battle2.jpg"

def process_bouken():
    while True:
        position = find_template_position(BOUKEN_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("bouken.jpgをタップしました")
            time.sleep(1)
            break  # 次の処理へ進む
        else:
            print("bouken.jpgが見つかりませんでした。再試行します...")

    while True:
        position = find_template_position(MAIN_STORY_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("main_story.jpgをタップしました")
            time.sleep(2)
            break  # 次の処理へ進む
        else:
            print("main_story.jpgが見つかりませんでした。再試行します...")
            time.sleep(2)

    while True:
        position = find_template_position(NEW_WORLD_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("new_world.jpgをタップしました")
            time.sleep(1)
            break  # 次の処理へ進む
        else:
            print("new_world.jpgが見つかりませんでした。再試行します...")
            time.sleep(2)

    while True:
        position = find_template_position(CHAPTER_ZERO_TITLE_PATH)
        position2 = find_template_position(CHAPTER_ZERO_TITLE2_PATH)
        if position:
            print("Chapter Zero_Title.jpgが見つかりました")
            break
        elif position2:
            tap_on_device(position2[0], position2[1])
            print("Chapter Zero_Title2.jpgをタップしました")
            break
        else:
            print("Chapter Zero_Title.jpgまたはChapter Zero_Title2.jpgが見つかりませんでした。再試行します...")
            time.sleep(2)

    while True:
        position = find_template_position(GO_QUEST_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("go_quest.jpgをタップしました")
            time.sleep(3)
            break  # 次の処理へ進む
        else:
            print("go_quest.jpgが見つかりませんでした。再試行します...")

    while True:
        position = find_template_position(DECISIVE_BATTLE_PATH)
        position2 = find_template_position(DECISIVE_BATTLE2_PATH)
        if position:
            tap_on_device(position[0], position[1])
            print("decisive_battle.jpgをタップしました")
            time.sleep(2)
            break  # 次の処理へ進む
        elif position2:
            print("decisive_battle2.jpgが見つかりました")
            time.sleep(2)
        else:
            print("decisive_battle.jpgが見つかりませんでした。再試行します...")