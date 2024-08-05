import os
import sys
from PyQt5.QtWidgets import (QApplication,QDesktopWidget, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QMessageBox, QScrollArea, QFrame, QProgressBar, QSplashScreen)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QTimer, Qt
from typing import Any, Dict
from weight_score_table import weight_score_table
from other_score_table import other_score_table

# 获取资源路径
def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 体质评分计算器类
class FitnessScoreCalculator:
    def __init__(self) -> None:
        self.weight_score_table = weight_score_table
        self.other_score_table = other_score_table

    def get_weight_score(self, gender: str, age: float, height: float, weight: float) -> int:
        age_group_weight = self.get_age_group_weight(age)
        height_ranges = self.weight_score_table[gender][age_group_weight]['height_ranges']
        scores = self.weight_score_table[gender][age_group_weight]['scores']
        
        for (height_min, height_max), score_list in zip(height_ranges, scores):
            if height_min <= height <= height_max:
                for score_dict in score_list:
                    weight_min, weight_max = min(score_dict['range']), max(score_dict['range'])
                    if (weight_min == float('-inf') or weight_max == float('inf')) and (weight_min < weight < weight_max):
                        return score_dict['score']
                    elif weight_min <= weight <= weight_max:
                        return score_dict['score']
        return 0

    def get_other_score(self, metric: str, gender: str, age: float, value: float) -> int:
        age_group_other = self.get_age_group_other(age)
        if metric not in self.other_score_table[gender][age_group_other]:
            return 0
        score_list = self.other_score_table[gender][age_group_other][metric]
        
        for score_dict in score_list:
            min_value, max_value = min(score_dict['range']), max(score_dict['range'])
            if (min_value == float('-inf') or max_value == float('inf')) and (min_value < value < max_value):
                return score_dict['score']
            elif min_value <= value <= max_value:
                return score_dict['score']
        return 0

    def get_age_group_weight(self, age: float) -> str:
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

    def get_age_group_other(self, age: float) -> str:
        age_groups = {
            (20, 24): '20-24',
            (25, 29): '25-29',
            (30, 34): '30-34',
            (35, 39): '35-39',
            (40, 44): '40-44',
            (45, 49): '45-49',
            (50, 54): '50-54',
            (55, 59): '55-59',
            (60, 64): '60-64',
            (65, 69): '65-69'
        }
        for (min_age, max_age), group in age_groups.items():
            if min_age <= age <= max_age:
                return group
        return str(age) if age in [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0] else 'unknown'

    def calculate_fitness_score(self, gender: str, age: float, height: float, weight: float, **kwargs: float) -> Dict[str, Any]:
        scores = {
            '体重得分': self.get_weight_score(gender, age, height, weight),
        }
        kwargs['height'] = height
        for metric, value in kwargs.items():
            scores[f'{metric}得分'] = self.get_other_score(metric, gender, age, value)
        
        total_score = sum(scores.values())
        scores['综合得分'] = total_score
        scores['等级'] = self.get_fitness_level(total_score, age)

        return scores

    def get_fitness_level(self, total_score: int, age: float) -> str:
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

# 启动画面类
class SplashScreen(QSplashScreen):
    def __init__(self, pixmap: QPixmap) -> None:
        super().__init__(pixmap)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFont(QFont('Arial', 16))

    def showMessage(self, message: str, alignment: Qt.Alignment, color: Qt.GlobalColor) -> None:
        super().showMessage(message, alignment, color)

# PyQt5应用程序类 
class FitnessApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def set_adaptive_window_size(self) -> None:
        screen = QDesktopWidget().screenGeometry()
        width, height = screen.width() * 0.8, screen.height() * 0.8
        self.setGeometry((screen.width() - width) / 2, (screen.height() - height) / 2, width / 2, height)

    def initUI(self) -> None:
        self.setWindowTitle('华投国民体质评分系统')
        self.set_adaptive_window_size()
        
        # 创建一个滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        # 创建一个容器小部件并将其设置为滚动区域的内容
        container = QWidget()
        scroll_area.setWidget(container)
        
        layout = QVBoxLayout(container)

        # 添加图像显示
        # self.image_label = QLabel(self)
        # image_path = resource_path('icon.jpg')
        # pixmap = QPixmap(image_path).scaled(200, 200)
        # self.image_label.setPixmap(pixmap)
        # self.image_label.setGeometry(10, 10, 200, 200)
        # layout.addWidget(self.image_label)

        self.add_input_field(layout, '性别:', QComboBox, 'gender_input', ['男', '女'])
        self.add_input_field(layout, '年龄:', QLineEdit, 'age_input')
        self.add_input_field(layout, '身高 (cm):', QLineEdit, 'height_input')
        self.add_input_field(layout, '体重 (kg):', QLineEdit, 'weight_input')
        self.add_input_field(layout, '肺活量 (ml):', QLineEdit, 'lung_capacity_input')
        self.add_input_field(layout, '握力 (kg):', QLineEdit, 'grip_strength_input')
        self.add_input_field(layout, '俯卧撑 (次):', QLineEdit, 'pushups_input')
        self.add_input_field(layout, '台阶试验 (分数):', QLineEdit, 'step_test_input')
        self.add_input_field(layout, '纵跳 (cm):', QLineEdit, 'vertical_jump_input')
        self.add_input_field(layout, '坐位体前屈 (cm):', QLineEdit, 'sit_and_reach_input')
        self.add_input_field(layout, '选择反应时 (秒):', QLineEdit, 'reaction_time_input')
        self.add_input_field(layout, '闭眼单脚站立 (秒):', QLineEdit, 'one_leg_stand_input')
        self.add_input_field(layout, '1分钟仰卧起坐 (次):', QLineEdit, 'situps_1min_input')
        self.add_input_field(layout, '10米折返跑 (秒):', QLineEdit, 'run_10m_input')
        self.add_input_field(layout, '立定跳远 (cm):', QLineEdit, 'standing_jump_input')
        self.add_input_field(layout, '网球掷远 (米):', QLineEdit, 'tennis_throw_input')
        self.add_input_field(layout, '双脚连续跳 (次):', QLineEdit, 'continuous_jump_input')
        self.add_input_field(layout, '走平衡木 (秒):', QLineEdit, 'balance_beam_input')

        self.calculate_button = QPushButton('计算得分')
        self.calculate_button.clicked.connect(self.calculate_score)
        layout.addWidget(self.calculate_button)

        self.results_label = QLabel('')
        layout.addWidget(self.results_label)

        # 设置主布局
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def add_input_field(self, layout: QVBoxLayout, label_text: str, widget_class: Any, attr_name: str, items: list = None) -> None:
        label = QLabel(label_text)
        input_field = widget_class()
        if items and isinstance(input_field, QComboBox):
            input_field.addItems(items)
        layout.addWidget(label)
        layout.addWidget(input_field)
        setattr(self, attr_name, input_field)

    def calculate_score(self) -> None:
        try:
            gender = self.gender_input.currentText()
            gender = 'male' if gender == '男' else 'female'
            age = float(self.age_input.text())
            height = float(self.height_input.text())
            weight = float(self.weight_input.text())
            inputs = {
                'lung_capacity': float(self.lung_capacity_input.text()),
                'grip_strength': float(self.grip_strength_input.text()),
                'pushups': float(self.pushups_input.text()),
                'step_test': float(self.step_test_input.text()),
                'vertical_jump': float(self.vertical_jump_input.text()),
                'sit_and_reach': float(self.sit_and_reach_input.text()),
                'reaction_time': float(self.reaction_time_input.text()),
                'one_leg_stand': float(self.one_leg_stand_input.text()),
                'situps_1min': float(self.situps_1min_input.text()),
                'run_10m': float(self.run_10m_input.text()),
                'standing_jump': float(self.standing_jump_input.text()),
                'tennis_throw': float(self.tennis_throw_input.text()),
                'continuous_jump': float(self.continuous_jump_input.text()),
                'balance_beam': float(self.balance_beam_input.text()),
            }
        except ValueError:
            QMessageBox.warning(self, '输入错误', '请确保所有输入项都是有效的数字。')
            return

        try:
            calculator = FitnessScoreCalculator()
            scores = calculator.calculate_fitness_score(gender, age, height, weight, **inputs)
        except KeyError as e:
            QMessageBox.critical(self, '计算错误', f'无法计算得分，错误：{e}')
            return

        metric_names = {
            'lung_capacity': '肺活量',
            'grip_strength': '握力',
            'pushups': '俯卧撑',
            'step_test': '台阶试验',
            'vertical_jump': '纵跳',
            'sit_and_reach': '坐位体前屈',
            'reaction_time': '选择反应时',
            'one_leg_stand': '闭眼单脚站立',
            'situps_1min': '1分钟仰卧起坐',
            'run_10m': '10米折返跑',
            'standing_jump': '立定跳远',
            'tennis_throw': '网球掷远',
            'continuous_jump': '双脚连续跳',
            'balance_beam': '走平衡木',
            'height': '身高',
        }

        results_text = '\n'.join([f"{metric_names.get(metric.split('得分')[0], metric)}: {score}" for metric, score in scores.items()])
        self.results_label.setText(results_text)
        QMessageBox.information(self, '结果', results_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 创建启动画面
    splash_pix = QPixmap(resource_path('icon.jpg')).scaled(400, 400, Qt.KeepAspectRatio)
    splash = SplashScreen(splash_pix)
    splash.show()
    splash.showMessage("加载中...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)

    # # 创建进度条
    # progress_bar = QProgressBar(splash)
    # progress_bar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)
    # progress_bar.setAlignment(Qt.AlignCenter)
    # progress_bar.setValue(0)

    # # 定时更新进度条
    # for i in range(1, 101):
    #     QTimer.singleShot(i * 20, lambda v=i: progress_bar.setValue(v))

    # 两秒后启动主应用
    QTimer.singleShot(2000, lambda: (splash.close(), app.quit()))

    app.exec_()
    
    # 创建并展示主应用
    ex = FitnessApp()
    ex.show()
    sys.exit(app.exec_())

