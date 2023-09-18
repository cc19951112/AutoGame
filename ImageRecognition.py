import os
import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
from sklearn.cluster import DBSCAN

# --- Global Settings and Constants ---
WINDOW_TITLE = '寻道大千'

path_start = os.path.abspath('start.png')
path_inform = os.path.abspath('inform.png')
path_activity = os.path.abspath('activity.png')
path_main = os.path.abspath('main.png')
path_chooseFudi = os.path.abspath('chooseFudi.png')
path_myFudi = os.path.abspath('myFudi.png')
reference_images = {
    "开始游戏场景": {"image": cv2.imread(path_start), "keypoints": None, "descriptors": None},
    "通告栏场景": {"image": cv2.imread(path_inform), "keypoints": None, "descriptors": None},
    "活动提示场景": {"image": cv2.imread(path_activity), "keypoints": None, "descriptors": None},
    "游戏主场景": {"image": cv2.imread(path_main), "keypoints": None, "descriptors": None},
    "选择福地场景": {"image": cv2.imread(path_chooseFudi), "keypoints": None, "descriptors": None},
    "我的福地场景": {"image": cv2.imread(path_myFudi), "keypoints": None, "descriptors": None},
}

sift = cv2.SIFT_create()

# --- Initialization: Precompute keypoints and descriptors for reference images ---
for scene_name, data in reference_images.items():
    data["keypoints"], data["descriptors"] = sift.detectAndCompute(data["image"], None)

# --- Utility Functions ---
def move_window_to_origin(window_title):
    """将指定标题的窗口移动到屏幕的原点（0,0）位置。"""
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        window.moveTo(0, 0)
    except IndexError:
        print(f"未找到标题为 '{window_title}' 的窗口。")
        raise

def get_game_window_dimensions(window_title):
    """获取指定标题的窗口的宽度和高度。"""
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        return window.width, window.height
    except IndexError:
        print(f"未找到标题为 '{window_title}' 的窗口。")
        raise

move_window_to_origin(WINDOW_TITLE)
width, height = get_game_window_dimensions(WINDOW_TITLE)

def capture_screenshot(region=None):
    """捕获屏幕截图，并返回NumPy数组格式的截图。"""
    screenshot = pyautogui.screenshot(region=region)
    screenshot_np = np.array(screenshot)
    return cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

def process_image(image_np):
    """处理图像来识别游戏的状态。目前，它只是将图像转换为灰度图像。"""
    return cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# --- Action Decider Function ---
def decide_action(scene_name, screenshot_np):
    """根据当前的场景名称来决定要执行的动作。"""
    action_templates = {
        '开始游戏场景': 'start_button.png',
        '通告栏场景': 'close_inform.png',
        '活动提示场景': 'close_activity.png',
        '游戏主场景': 'dongfu_button.png',
        '选择福地场景': 'chooseFudi_button.png',
    }

    if scene_name in action_templates:
        click_template(screenshot_np, action_templates[scene_name])
    elif scene_name == '我的福地场景':
        resources = [
            {"name": "仙桃",      "level": 1,   "template": cv2.imread('peach_1.png', 0), "threshold":0.8},
            {"name": "仙桃",      "level": 2,   "template": cv2.imread('peach_2.png', 0), "threshold":0.8},
            {"name": "仙桃",      "level": 3,   "template": cv2.imread('peach_3.png', 0), "threshold":0.8},
            {"name": "仙桃",      "level": 4,   "template": cv2.imread('peach_4.png', 0), "threshold":0.8},
            #{"name": "仙桃",      "level": 5,   "template": cv2.imread('peach_5.png', 0), "threshold":0.8},

            # {"name": "灵石",  "level": 1,   "template": cv2.imread('blue_1.png', 0), "threshold":0.82},
            # {"name": "灵石",  "level": 2,   "template": cv2.imread('blue_2.png', 0), "threshold":0.82},
            # {"name": "灵石",  "level": 3,   "template": cv2.imread('blue_3.png', 0), "threshold":0.8},   
            # #{"name": "灵石",  "level": 4,   "template": cv2.imread('blue_4.png', 0), "threshold":0.8},
            # #{"name": "灵石",  "level": 5,   "template": cv2.imread('blue_5.png', 0), "threshold":0.8},

            # {"name": "净瓶水",    "level": 1,   "template": cv2.imread('bottle_1.png', 0), "threshold":0.8},
            # {"name": "净瓶水",    "level": 2,   "template": cv2.imread('bottle_2.png', 0), "threshold":0.8},
            # {"name": "净瓶水",    "level": 3,   "template": cv2.imread('bottle_3.png', 0), "threshold":0.8},
            # {"name": "净瓶水",    "level": 4,   "template": cv2.imread('bottle_4.png', 0), "threshold":0.8},
            # {"name": "净瓶水",    "level": 5,   "template": cv2.imread('bottle_5.png', 0), "threshold":0.8},

            # {"name": "仙玉",    "level": 1,   "template": cv2.imread('green_1.png', 0), "threshold":0.8},
            # {"name": "仙玉",    "level": 2,   "template": cv2.imread('green_2.png', 0), "threshold":0.8},
            # {"name": "仙玉",    "level": 3,   "template": cv2.imread('green_3.png', 0), "threshold":0.8},
            # {"name": "仙玉",    "level": 4,   "template": cv2.imread('green_4.png', 0), "threshold":0.8},
            # {"name": "仙玉",    "level": 5,   "template": cv2.imread('green_5.png', 0), "threshold":0.8},

            # {"name": "琉璃珠",    "level": 1,   "template": cv2.imread('glass_1.png', 0), "threshold":0.85},
            # {"name": "琉璃珠",    "level": 2,   "template": cv2.imread('glass_2.png', 0), "threshold":0.85},
            # {"name": "琉璃珠",    "level": 3,   "template": cv2.imread('glass_3.png', 0), "threshold":0.85},
            # {"name": "琉璃珠",    "level": 4,   "template": cv2.imread('glass_4.png', 0), "threshold":0.85},


            # {"name": "昆仑铁",    "level": 1,   "template": cv2.imread('iron_1.png', 0), "threshold":0.8},
            # {"name": "昆仑铁",    "level": 2,   "template": cv2.imread('iron_2.png', 0), "threshold":0.8},
            # {"name": "昆仑铁",    "level": 3,   "template": cv2.imread('iron_3.png', 0), "threshold":0.8},
            # {"name": "昆仑铁",    "level": 4,   "template": cv2.imread('iron_4.png', 0), "threshold":0.8},
            # {"name": "昆仑铁",    "level": 5,   "template": cv2.imread('iron_5.png', 0), "threshold":0.8},

            # {"name": "天衍符",    "level": 1,   "template": cv2.imread('paper_1.png', 0), "threshold":0.8},
            # {"name": "天衍符",    "level": 2,   "template": cv2.imread('paper_2.png', 0), "threshold":0.8},
            #{"name": "天衍符",    "level": 3,   "template": cv2.imread('paper_2.png', 0)},
            # …(添加其他物资和等级)
        ]
        # 将屏幕截图转换为灰度图像
        screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

        # 对屏幕截图应用Canny边缘检测
        screenshot_edges = cv2.Canny(screenshot_gray, 100, 200)
        found_resources = []
        for resource in resources:
            # 对模板应用Canny边缘检测
            resource_edges = cv2.Canny(resource["template"], 100, 200)

            while True:
                res = cv2.matchTemplate(screenshot_edges, resource_edges, cv2.TM_CCOEFF_NORMED)
                threshold = resource["threshold"]
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                if max_val >= threshold:
                    best_match = resource
                    best_match_val = max_val

                    for other_resource in resources:
                        if other_resource["name"] == resource["name"] and other_resource["level"] != resource["level"]:
                            other_resource_edges = cv2.Canny(other_resource["template"], 100, 200)
                            res_other = cv2.matchTemplate(
                                screenshot_edges[max_loc[1]:max_loc[1]+resource["template"].shape[0], max_loc[0]:max_loc[0]+resource["template"].shape[1]], 
                                other_resource_edges, 
                                cv2.TM_CCOEFF_NORMED
                            )
                            min_val_other, max_val_other, min_loc_other, max_loc_other = cv2.minMaxLoc(res_other)
                            if max_val_other > best_match_val:
                                best_match = other_resource
                                best_match_val = max_val_other

                    match_width, match_height = best_match["template"].shape[::-1]
                    found_resources.append(f"{best_match['name']} 等级：{best_match['level']} 位置: {max_loc}")
                    screenshot_gray[max_loc[1]:max_loc[1]+match_height, max_loc[0]:max_loc[0]+match_width] = 0
                else:
                    break

        for i, resource in enumerate(found_resources):
            print(f"{i+1}、{resource}")
        target_resources = [
            #{"name": "仙桃", "levels": [1]},
            {"name": "仙桃", "levels": [2]},
            #{"name": "仙桃", "levels": [3]},
            #{"name": "仙桃", "levels": [4]},
            #{"name": "仙桃", "levels": [5]},
            #{"name": "净瓶水", "levels": [5]},
        ]
        # 创建一个列表来保存你想要收集的资源的位置
        target_positions = []
        for resource_text in found_resources:
            name, level_info, _, position_info1, position_info2 = resource_text.split(' ')
            level = int(level_info.split('：')[1])
            position_info = position_info1 + position_info2  # 合并位置信息
            position_x, position_y = map(float, position_info[1:-1].split(','))  # 提取x和y坐标
            position = (position_x, position_y)
            for target_resource in target_resources:
                if name == target_resource["name"] and level in target_resource["levels"]:
                    target_positions.append((name, level, position))
        # 现在你有了一个包含所有你想要收集的资源位置的列表
        # 你可以使用这个列表来自动化点击操作
        for name, level, position in target_positions:
            # 获取特定点的 RGB 值
            pyautogui.click(x=position[0]+10, y=position[1]) 
            screenshot = capture_screenshot(region=(0, 0, width, height))
            left_x, left_y = 145,432
            right_x,right_y = 446,433
            pixel_rgb_left = screenshot[left_y, left_x]
            pixel_rgb_right = screenshot[right_y, right_x]
            # 判断采集情况
            isCollectByOthers = False
            isCollectByMe = False
            if rgb_similar(pixel_rgb_left, np.array([65, 90, 104]),8):
                isCollectByOthers = False
            else:
                isCollectByOthers = True
            if rgb_similar(pixel_rgb_right, np.array([62, 88, 102]),8):
                isCollectByMe = False
            else:
                isCollectByMe = True
            #根据采集情况做不同动作
            #1、没人采，点击采集
            if isCollectByOthers == False and isCollectByMe == False:
                pyautogui.click(291, 803) 
            #2、有人在采集,点击右上角叉叉
            else:
                pyautogui.click(544, 123)

        # ... 其他代码

    else:
        # 当场景未知时，不执行任何操作。
        pass

# --- Scene Identification Function ---
def identify_scene(screenshot_np):
    """识别当前的游戏场景。"""
    kp_screenshot, des_screenshot = sift.detectAndCompute(screenshot_np, None)
    bf = cv2.BFMatcher()
    
    highest_match_count = 0
    identified_scene = "未知"
    
    for scene_name, data in reference_images.items():
        matches = bf.knnMatch(des_screenshot, data["descriptors"], k=2)
        good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]
        if len(good_matches) > highest_match_count:
            highest_match_count = len(good_matches)
            identified_scene = scene_name
    
    return identified_scene

def click_template(screenshot_np, template_path):
    """找到模板在屏幕截图中的位置并点击它。"""
    template = cv2.imread(template_path, 0)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    h, w = template.shape
    center_x = max_loc[0] + w // 2
    center_y = max_loc[1] + h // 2
    pyautogui.click(center_x, center_y)

def rgb_similar(rgb1, rgb2, threshold):
    return np.linalg.norm(rgb1 - rgb2) <= threshold

# --- Main Loop ---
def main():
    """主循环，持续捕获屏幕截图，处理图像，做出决策并执行动作。"""

    while True:
        screenshot_np = capture_screenshot(region=(0, 0, width, height))
        identified_scene = identify_scene(screenshot_np)
        decide_action(identified_scene, screenshot_np)

if __name__ == "__main__":
    main()
