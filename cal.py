import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QMessageBox
from weight_score_table import weight_score_table
from other_score_table import other_score_table
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QComboBox, QDesktopWidget
# 体质评分计算器类
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class FitnessScoreCalculator:
    def __init__(self):
        self.weight_score_table = weight_score_table
        self.other_score_table = other_score_table

    # 获取体重得分
    def get_weight_score(self, gender, age, height, weight):
        age_group_weight = self.get_age_group_weight(age)
        height_ranges = self.weight_score_table[gender][age_group_weight]['height_ranges']
        scores = self.weight_score_table[gender][age_group_weight]['scores']
        
        for (height_min, height_max), score_list in zip(height_ranges, scores):
            if height_min <= height <= height_max:
                for score_dict in score_list:
                    weight_min, weight_max = score_dict['range']
                    if weight_min == float('-inf') or weight_max == float('inf'):
                        if weight_min < weight < weight_max:
                            return score_dict['score']
                    elif weight_min <= weight <= weight_max:
                        return score_dict['score']
        return 0

    # 获取其他指标得分
    def get_other_score(self, metric, gender, age, value):
        age_group_other = self.get_age_group_other(age)
        if metric not in self.other_score_table[gender][age_group_other]:
            return 0
        score_list = self.other_score_table[gender][age_group_other][metric]
        
        for score_dict in score_list:
            min_value, max_value = score_dict['range']
            if min_value == float('-inf') or max_value == float('inf'):
                if min_value < value < max_value:
                    return score_dict['score']
            elif min_value <= value <= max_value:
                return score_dict['score']
        return 0

    # 根据年龄获取对应的体重年龄组
    def get_age_group_weight(self, age):
        if 20 <= age <= 29:
            return '20-29'
        elif 30 <= age <= 39:
            return '30-39'
        elif 40 <= age <= 49:
            return '40-49'
        elif 50 <= age <= 59:
            return '50-59'
        elif 3 <= age <= 6:
            return '3-6'
        elif 60 <= age <= 69:
            return '60-69'
        else:
            return 'unknown'

    # 根据年龄获取对应的其他指标年龄组
    def get_age_group_other(self, age):
        if 20 <= age <= 24:
            return '20-24'
        elif 25 <= age <= 29:
            return '25-29'
        elif 30 <= age <= 34:
            return '30-34'
        elif 35 <= age <= 39:
            return '35-39'
        elif 40 <= age <= 44:
            return '40-44'
        elif 45 <= age <= 49:
            return '45-49'
        elif 50 <= age <= 54:
            return '50-54'
        elif 55 <= age <= 59:
            return '55-59'
        elif 60 <= age <= 64:
            return '60-64'
        elif 65 <= age <= 69:
            return '65-69'
        elif age == 3:
            return '3'
        elif age == 3.5:
            return '3.5'
        elif age == 4:
            return '4'
        elif age == 4.5:
            return '4.5'
        elif age == 5:
            return '5'
        elif age == 5.5:
            return '5.5'
        elif age == 6:
            return '6'
        else:
            return 'unknown'
    
    # 计算综合体质评分
    def calculate_fitness_score(self, gender, age, height, weight, lung_capacity=None, grip_strength=None, pushups=None, step_test=None, vertical_jump=None, sit_and_reach=None, reaction_time=None, one_leg_stand=None, situps_1min=None, run_10m=None, standing_jump=None, tennis_throw=None, continuous_jump=None, balance_beam=None):
        weight_score = self.get_weight_score(gender, age, height, weight)
        lung_capacity_score = self.get_other_score('lung_capacity', gender, age, lung_capacity)
        grip_strength_score = self.get_other_score('grip_strength', gender, age, grip_strength)
        pushups_score = self.get_other_score('pushups', gender, age, pushups)
        step_test_score = self.get_other_score('step_test', gender, age, step_test)
        vertical_jump_score = self.get_other_score('vertical_jump', gender, age, vertical_jump)
        sit_and_reach_score = self.get_other_score('sit_and_reach', gender, age, sit_and_reach)
        reaction_time_score = self.get_other_score('reaction_time', gender, age, reaction_time)
        one_leg_stand_score = self.get_other_score('one_leg_stand', gender, age, one_leg_stand)
        situps_1min_score = self.get_other_score('situps_1min', gender, age, situps_1min)
        run_10m_score = self.get_other_score('run_10m', gender, age, run_10m)
        standing_jump_score = self.get_other_score('standing_jump', gender, age, standing_jump)
        tennis_throw_score = self.get_other_score('tennis_throw', gender, age, tennis_throw)
        continuous_jump_score = self.get_other_score('continuous_jump', gender, age, continuous_jump)
        balance_beam_score = self.get_other_score('balance_beam', gender, age, balance_beam)

        scores = {
            '体重得分': weight_score,
            '肺活量得分': lung_capacity_score,
            '握力得分': grip_strength_score,
            '俯卧撑得分': pushups_score,
            '台阶试验得分': step_test_score,
            '纵跳得分': vertical_jump_score,
            '坐位体前屈得分': sit_and_reach_score,
            '选择反应时得分': reaction_time_score,
            '闭眼单脚站立得分': one_leg_stand_score,
            '1分钟仰卧起坐得分': situps_1min_score,
            '10米折返跑得分': run_10m_score,
            '立定跳远得分': standing_jump_score,
            '网球掷远得分': tennis_throw_score,
            '双脚连续跳得分': continuous_jump_score,
            '走平衡木得分': balance_beam_score
        }
        
        total_score = sum(scores.values())
        scores['综合得分'] = total_score
        
        level = self.get_fitness_level(total_score, age)
        scores['等级'] = level

        return scores

    # 根据综合得分确定等级
    def get_fitness_level(self, total_score, age):
        if 20 <= age <= 39:
            if total_score > 33:
                return '一级（优秀）'
            elif 30 <= total_score <= 33:
                return '二级（良好）'
            elif 23 <= total_score <= 29:
                return '三级（合格）'
            else:
                return '四级（不合格）'
        elif 40 <= age <= 59:
            if total_score > 26:
                return '一级（优秀）'
            elif 24 <= total_score <= 26:
                return '二级（良好）'
            elif 18 <= total_score <= 23:
                return '三级（合格）'
            else:
                return '四级（不合格）'
        elif 3 <= age <= 6:
            if total_score > 31:
                return '一级（优秀）'
            elif 28 <= total_score <= 31:
                return '二级（良好）'
            elif 20 <= total_score <= 27:
                return '三级（合格）'
            else:
                return '四级（不合格）'
        elif 60 <= age <= 69:
            if total_score > 23:
                return '一级（优秀）'
            elif 21 <= total_score <= 23:
                return '二级（良好）'
            elif 15 <= total_score <= 20:
                return '三级（合格）'
            else:
                return '四级（不合格）'
        else:
            return '未知等级'


# PyQt5应用程序类 
class FitnessApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def set_adaptive_window_size(self):
        screen = QDesktopWidget().screenGeometry()
        width, height = screen.width() * 0.8, screen.height() * 0.8
        self.setGeometry((screen.width() - width) / 2, (screen.height() - height) / 2, width/2, height)
    
    # 初始化界面
    def initUI(self):
        self.setWindowTitle('华投国民体质评分系统')
        self.set_adaptive_window_size()  # 设置窗口的自适应尺寸
        #self.resize(800, 300)  # 设置窗口的初始尺寸为 800x300
        layout = QVBoxLayout()
        
        # 添加图像显示
        self.image_label = QLabel(self)
        image_path = resource_path('icon.jpg')  # 动态获取图片路径
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(200, 200)  # 调整图像大小
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(10, 10, 200, 200)  # 设置图像显示位置和大小
        layout.addWidget(self.image_label)
        
        self.gender_label = QLabel('性别:')
        self.gender_input = QComboBox()
        self.gender_input.addItems(['男', '女'])
        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_input)
        
        self.age_label = QLabel('年龄:')
        self.age_input = QLineEdit()
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        
        self.height_label = QLabel('身高 (cm):')
        self.height_input = QLineEdit()
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        
        self.weight_label = QLabel('体重 (kg):')
        self.weight_input = QLineEdit()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        
        self.lung_capacity_label = QLabel('肺活量 (ml):')
        self.lung_capacity_input = QLineEdit()
        layout.addWidget(self.lung_capacity_label)
        layout.addWidget(self.lung_capacity_input)
        
        self.grip_strength_label = QLabel('握力 (kg):')
        self.grip_strength_input = QLineEdit()
        layout.addWidget(self.grip_strength_label)
        layout.addWidget(self.grip_strength_input)
        
        self.pushups_label = QLabel('俯卧撑 (次):')
        self.pushups_input = QLineEdit()
        layout.addWidget(self.pushups_label)
        layout.addWidget(self.pushups_input)
        
        self.step_test_label = QLabel('台阶试验 (分数):')
        self.step_test_input = QLineEdit()
        layout.addWidget(self.step_test_label)
        layout.addWidget(self.step_test_input)
        
        self.vertical_jump_label = QLabel('纵跳 (cm):')
        self.vertical_jump_input = QLineEdit()
        layout.addWidget(self.vertical_jump_label)
        layout.addWidget(self.vertical_jump_input)
        
        self.sit_and_reach_label = QLabel('坐位体前屈 (cm):')
        self.sit_and_reach_input = QLineEdit()
        layout.addWidget(self.sit_and_reach_label)
        layout.addWidget(self.sit_and_reach_input)
        
        self.reaction_time_label = QLabel('选择反应时 (秒):')
        self.reaction_time_input = QLineEdit()
        layout.addWidget(self.reaction_time_label)
        layout.addWidget(self.reaction_time_input)
        
        self.one_leg_stand_label = QLabel('闭眼单脚站立 (秒):')
        self.one_leg_stand_input = QLineEdit()
        layout.addWidget(self.one_leg_stand_label)
        layout.addWidget(self.one_leg_stand_input)
        
        self.situps_1min_label = QLabel('1分钟仰卧起坐 (次):')
        self.situps_1min_input = QLineEdit()
        layout.addWidget(self.situps_1min_label)
        layout.addWidget(self.situps_1min_input)
        
        self.run_10m_label = QLabel('10米折返跑 (秒):')
        self.run_10m_input = QLineEdit()
        layout.addWidget(self.run_10m_label)
        layout.addWidget(self.run_10m_input)
        
        self.standing_jump_label = QLabel('立定跳远 (cm):')
        self.standing_jump_input = QLineEdit()
        layout.addWidget(self.standing_jump_label)
        layout.addWidget(self.standing_jump_input)
        
        self.tennis_throw_label = QLabel('网球掷远 (米):')
        self.tennis_throw_input = QLineEdit()
        layout.addWidget(self.tennis_throw_label)
        layout.addWidget(self.tennis_throw_input)
        
        self.continuous_jump_label = QLabel('双脚连续跳 (次):')
        self.continuous_jump_input = QLineEdit()
        layout.addWidget(self.continuous_jump_label)
        layout.addWidget(self.continuous_jump_input)
        
        self.balance_beam_label = QLabel('走平衡木 (秒):')
        self.balance_beam_input = QLineEdit()
        layout.addWidget(self.balance_beam_label)
        layout.addWidget(self.balance_beam_input)
        
        self.calculate_button = QPushButton('计算得分')
        self.calculate_button.clicked.connect(self.calculate_score)
        layout.addWidget(self.calculate_button)
        
        self.results_label = QLabel('')
        layout.addWidget(self.results_label)
        
        self.setLayout(layout)
    
    # 计算得分并显示结果
    def calculate_score(self):
        gender = self.gender_input.currentText()
        gender = 'male' if gender == '男' else 'female'
        age = float(self.age_input.text())
        height = float(self.height_input.text())
        weight = float(self.weight_input.text())
        lung_capacity = int(self.lung_capacity_input.text())
        grip_strength = int(self.grip_strength_input.text())
        pushups = int(self.pushups_input.text())
        step_test = int(self.step_test_input.text())
        vertical_jump = int(self.vertical_jump_input.text())
        sit_and_reach = int(self.sit_and_reach_input.text())
        reaction_time = float(self.reaction_time_input.text())
        one_leg_stand = int(self.one_leg_stand_input.text())
        situps_1min = int(self.situps_1min_input.text())
        run_10m = float(self.run_10m_input.text())
        standing_jump = int(self.standing_jump_input.text())
        tennis_throw = float(self.tennis_throw_input.text())
        continuous_jump = int(self.continuous_jump_input.text())
        balance_beam = float(self.balance_beam_input.text())
        
        calculator = FitnessScoreCalculator()
        scores = calculator.calculate_fitness_score(
            gender, age, height, weight, lung_capacity, grip_strength, pushups, step_test, vertical_jump, sit_and_reach, reaction_time, one_leg_stand, situps_1min, run_10m, standing_jump, tennis_throw, continuous_jump, balance_beam
        )
        
        results_text = ''
        for metric, score in scores.items():
            results_text += f"{metric}: {score}\n"
        
        self.results_label.setText(results_text)
        QMessageBox.information(self, '结果', results_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FitnessApp()
    ex.show()
    sys.exit(app.exec_())
