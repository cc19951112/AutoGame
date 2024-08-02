# from weight_score_table import weight_score_table
# from other_score_table import other_score_table

# class FitnessScoreCalculator:
#     def __init__(self):
#         self.weight_score_table = weight_score_table
#         self.other_score_table = other_score_table

#     def get_weight_score(self, gender, age, height, weight):
#         age_group_weight = self.get_age_group_weight(age)
#         height_ranges = self.weight_score_table[gender][age_group_weight]['height_ranges']
#         scores = self.weight_score_table[gender][age_group_weight]['scores']
        
#         for (height_min, height_max), score_list in zip(height_ranges, scores):
#             if height_min <= height <= height_max:
#                 for score_dict in score_list:
#                     weight_min, weight_max = score_dict['range']
#                     #print(f"Checking weight range: {weight_min} - {weight_max} for weight: {weight}")
#                     if weight_min < weight <= weight_max:
#                         return score_dict['score']
#         return 0

#     def get_other_score(self, metric, gender, age, value):
#         age_group_other = self.get_age_group_other(age)
#         if metric not in self.other_score_table[gender][age_group_other]:
#             print(f"Metric {metric} not found for age group {age_group_other} and gender {gender}")
#             return 0
#         score_list = self.other_score_table[gender][age_group_other][metric]
        
#         for score_dict in score_list:
#             min_value, max_value = score_dict['range']
#             if min_value <= value <= max_value:
#                 return score_dict['score']
#         return 0
    
#     def get_age_group_weight(self, age):
#         if 20 <= age <= 29:
#             return '20-29'
#         elif 30 <= age <= 39:
#             return '30-39'
#         elif 40 <= age <= 49:
#             return '40-49'
#         elif 50 <= age <= 59:
#             return '50-59'
#         else:
#             return 'unknown'
        
#     def get_age_group_other(self, age):
#         if 20 <= age <= 24:
#             return '20-24'
#         elif 25 <= age <= 29:
#             return '25-29'
#         elif 30 <= age <= 34:
#             return '30-34'
#         elif 35 <= age <= 39:
#             return '35-39'
#         elif 40 <= age <= 44:
#             return '40-44'
#         elif 45 <= age <= 49:
#             return '45-49'
#         elif 50 <= age <= 54:
#             return '50-54'
#         elif 55 <= age <= 59:
#             return '55-59'
#         else:
#             return 'unknown'
    
#     def calculate_fitness_score(self, gender, age, height, weight, lung_capacity=None, grip_strength=None, pushups=None, step_test=None, vertical_jump=None, sit_and_reach=None, reaction_time=None, one_leg_stand=None, situps_1min=None):
#         # 获取各项指标的得分
#         weight_score = self.get_weight_score(gender, age, height, weight)
#         lung_capacity_score = self.get_other_score('lung_capacity', gender, age, lung_capacity)
#         grip_strength_score = self.get_other_score('grip_strength', gender, age, grip_strength)
#         pushups_score = self.get_other_score('pushups', gender, age, pushups)
#         step_test_score = self.get_other_score('step_test', gender, age, step_test)
#         vertical_jump_score = self.get_other_score('vertical_jump', gender, age, vertical_jump)
#         sit_and_reach_score = self.get_other_score('sit_and_reach', gender, age, sit_and_reach)
#         reaction_time_score = self.get_other_score('reaction_time', gender, age, reaction_time)
#         one_leg_stand_score = self.get_other_score('one_leg_stand', gender, age, one_leg_stand)
#         situps_1min_score = self.get_other_score('situps_1min', gender, age, situps_1min)

#         # 计算综合得分，可以根据需要调整权重或计算方式
#         scores = {
#             'weight_score': weight_score,
#             'lung_capacity_score': lung_capacity_score,
#             'grip_strength_score': grip_strength_score,
#             'pushups_score': pushups_score,
#             'step_test_score': step_test_score,
#             'vertical_jump_score': vertical_jump_score,
#             'sit_and_reach_score': sit_and_reach_score,
#             'reaction_time_score': reaction_time_score,
#             'one_leg_stand_score': one_leg_stand_score,
#             'situps_1min_score': situps_1min_score
#         }
        
#         # 计算综合得分，忽略0分项目
#         total_score = sum(scores.values())
#         scores['total_score'] = total_score
        
#         # 根据总分确定等级
#         level = self.get_fitness_level(total_score, age)
#         scores['level'] = level

#         return scores

#     def get_fitness_level(self, total_score, age):
#         if 20 <= age <= 39:
#             if total_score > 33:
#                 return '一级（优秀）'
#             elif 30 <= total_score <= 33:
#                 return '二级（良好）'
#             elif 23 <= total_score <= 29:
#                 return '三级（合格）'
#             else:
#                 return '四级（不合格）'
#         elif 40 <= age <= 59:
#             if total_score > 26:
#                 return '一级（优秀）'
#             elif 24 <= total_score <= 26:
#                 return '二级（良好）'
#             elif 18 <= total_score <= 23:
#                 return '三级（合格）'
#             else:
#                 return '四级（不合格）'
#         else:
#             return '未知等级'

# if __name__ == "__main__":
#     calculator = FitnessScoreCalculator()
#     gender = 'female'
#     age = 25
#     height = 175
#     weight = 70
#     lung_capacity = 3500 # 肺活量
#     grip_strength = 45 # 握力
#     pushups = 20 # 俯卧撑
#     step_test = 55 # 台阶试验
#     vertical_jump = 30 # 纵跳
#     sit_and_reach = 8 # 坐位体前屈
#     reaction_time = 0.50 # 选择反应时
#     one_leg_stand = 40 # 闭眼单脚站立
#     situps_1min = 10 # 1分钟仰卧起坐

#     scores = calculator.calculate_fitness_score(
#         gender, age, height, weight, lung_capacity, grip_strength, pushups, step_test, vertical_jump, sit_and_reach, reaction_time, one_leg_stand, situps_1min
#     )
#     for metric, score in scores.items():
#         print(f"{metric}: {score}")
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QMessageBox
from weight_score_table import weight_score_table
from other_score_table import other_score_table

class FitnessScoreCalculator:
    def __init__(self):
        self.weight_score_table = weight_score_table
        self.other_score_table = other_score_table

    def get_weight_score(self, gender, age, height, weight):
        age_group_weight = self.get_age_group_weight(age)
        height_ranges = self.weight_score_table[gender][age_group_weight]['height_ranges']
        scores = self.weight_score_table[gender][age_group_weight]['scores']
        
        for (height_min, height_max), score_list in zip(height_ranges, scores):
            if height_min <= height <= height_max:
                for score_dict in score_list:
                    weight_min, weight_max = score_dict['range']
                    if weight_min < weight <= weight_max:
                        return score_dict['score']
        return 0

    def get_other_score(self, metric, gender, age, value):
        age_group_other = self.get_age_group_other(age)
        if metric not in self.other_score_table[gender][age_group_other]:
            return 0
        score_list = self.other_score_table[gender][age_group_other][metric]
        
        for score_dict in score_list:
            min_value, max_value = score_dict['range']
            if min_value <= value <= max_value:
                return score_dict['score']
        return 0
    
    def get_age_group_weight(self, age):
        if 20 <= age <= 29:
            return '20-29'
        elif 30 <= age <= 39:
            return '30-39'
        elif 40 <= age <= 49:
            return '40-49'
        elif 50 <= age <= 59:
            return '50-59'
        else:
            return 'unknown'
        
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
        else:
            return 'unknown'
    
    def calculate_fitness_score(self, gender, age, height, weight, lung_capacity=None, grip_strength=None, pushups=None, step_test=None, vertical_jump=None, sit_and_reach=None, reaction_time=None, one_leg_stand=None, situps_1min=None):
        # 获取各项指标的得分
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

        # 计算综合得分，可以根据需要调整权重或计算方式
        scores = {
            'weight_score': weight_score,
            'lung_capacity_score': lung_capacity_score,
            'grip_strength_score': grip_strength_score,
            'pushups_score': pushups_score,
            'step_test_score': step_test_score,
            'vertical_jump_score': vertical_jump_score,
            'sit_and_reach_score': sit_and_reach_score,
            'reaction_time_score': reaction_time_score,
            'one_leg_stand_score': one_leg_stand_score,
            'situps_1min_score': situps_1min_score
        }
        
        # 计算综合得分，忽略0分项目
        total_score = sum(scores.values())
        scores['total_score'] = total_score
        
        # 根据总分确定等级
        level = self.get_fitness_level(total_score, age)
        scores['level'] = level

        return scores

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
        else:
            return '未知等级'


class FitnessApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Fitness Score Calculator')
        
        layout = QVBoxLayout()
        
        self.gender_label = QLabel('Gender:')
        self.gender_input = QComboBox()
        self.gender_input.addItems(['male', 'female'])
        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_input)
        
        self.age_label = QLabel('Age:')
        self.age_input = QLineEdit()
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        
        self.height_label = QLabel('Height (cm):')
        self.height_input = QLineEdit()
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        
        self.weight_label = QLabel('Weight (kg):')
        self.weight_input = QLineEdit()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        
        self.lung_capacity_label = QLabel('Lung Capacity (ml):')
        self.lung_capacity_input = QLineEdit()
        layout.addWidget(self.lung_capacity_label)
        layout.addWidget(self.lung_capacity_input)
        
        self.grip_strength_label = QLabel('Grip Strength (kg):')
        self.grip_strength_input = QLineEdit()
        layout.addWidget(self.grip_strength_label)
        layout.addWidget(self.grip_strength_input)
        
        self.pushups_label = QLabel('Push-ups (times):')
        self.pushups_input = QLineEdit()
        layout.addWidget(self.pushups_label)
        layout.addWidget(self.pushups_input)
        
        self.step_test_label = QLabel('Step Test (score):')
        self.step_test_input = QLineEdit()
        layout.addWidget(self.step_test_label)
        layout.addWidget(self.step_test_input)
        
        self.vertical_jump_label = QLabel('Vertical Jump (cm):')
        self.vertical_jump_input = QLineEdit()
        layout.addWidget(self.vertical_jump_label)
        layout.addWidget(self.vertical_jump_input)
        
        self.sit_and_reach_label = QLabel('Sit and Reach (cm):')
        self.sit_and_reach_input = QLineEdit()
        layout.addWidget(self.sit_and_reach_label)
        layout.addWidget(self.sit_and_reach_input)
        
        self.reaction_time_label = QLabel('Reaction Time (s):')
        self.reaction_time_input = QLineEdit()
        layout.addWidget(self.reaction_time_label)
        layout.addWidget(self.reaction_time_input)
        
        self.one_leg_stand_label = QLabel('One-leg Stand (s):')
        self.one_leg_stand_input = QLineEdit()
        layout.addWidget(self.one_leg_stand_label)
        layout.addWidget(self.one_leg_stand_input)
        
        self.situps_1min_label = QLabel('1-Minute Sit-ups (times):')
        self.situps_1min_input = QLineEdit()
        layout.addWidget(self.situps_1min_label)
        layout.addWidget(self.situps_1min_input)
        
        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_score)
        layout.addWidget(self.calculate_button)
        
        self.results_label = QLabel('')
        layout.addWidget(self.results_label)
        
        self.setLayout(layout)

    def calculate_score(self):
        gender = self.gender_input.currentText()
        age = int(self.age_input.text())
        height = int(self.height_input.text())
        weight = int(self.weight_input.text())
        lung_capacity = int(self.lung_capacity_input.text())
        grip_strength = int(self.grip_strength_input.text())
        pushups = int(self.pushups_input.text())
        step_test = int(self.step_test_input.text())
        vertical_jump = int(self.vertical_jump_input.text())
        sit_and_reach = int(self.sit_and_reach_input.text())
        reaction_time = float(self.reaction_time_input.text())
        one_leg_stand = int(self.one_leg_stand_input.text())
        situps_1min = int(self.situps_1min_input.text())
        
        calculator = FitnessScoreCalculator()
        scores = calculator.calculate_fitness_score(
            gender, age, height, weight, lung_capacity, grip_strength, pushups, step_test, vertical_jump, sit_and_reach, reaction_time, one_leg_stand, situps_1min
        )
        
        results_text = ''
        for metric, score in scores.items():
            results_text += f"{metric}: {score}\n"
        
        self.results_label.setText(results_text)
        QMessageBox.information(self, 'Results', results_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FitnessApp()
    ex.show()
    sys.exit(app.exec_())
