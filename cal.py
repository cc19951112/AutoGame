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
    
#     def calculate_fitness_score(self, gender, age, height, weight, lung_capacity=None, grip_strength=None, pushups=None, step_test=None, vertical_jump=None, sit_and_reach=None, reaction_time=None, one_leg_stand=None):
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
        
#         return scores

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
#         gender, age, height, weight, lung_capacity, grip_strength, pushups, step_test, vertical_jump, sit_and_reach, reaction_time, one_leg_stand
#     )
#     for metric, score in scores.items():
#         print(f"{metric}: {score}")
# fitness_score_calculator.py
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
                    #print(f"Checking weight range: {weight_min} - {weight_max} for weight: {weight}")
                    if weight_min < weight <= weight_max:
                        return score_dict['score']
        return 0

    def get_other_score(self, metric, gender, age, value):
        age_group_other = self.get_age_group_other(age)
        if metric not in self.other_score_table[gender][age_group_other]:
            print(f"Metric {metric} not found for age group {age_group_other} and gender {gender}")
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

if __name__ == "__main__":
    calculator = FitnessScoreCalculator()
    gender = 'female'
    age = 25
    height = 175
    weight = 70
    lung_capacity = 3500 # 肺活量
    grip_strength = 45 # 握力
    pushups = 20 # 俯卧撑
    step_test = 55 # 台阶试验
    vertical_jump = 30 # 纵跳
    sit_and_reach = 8 # 坐位体前屈
    reaction_time = 0.50 # 选择反应时
    one_leg_stand = 40 # 闭眼单脚站立
    situps_1min = 10 # 1分钟仰卧起坐

    scores = calculator.calculate_fitness_score(
        gender, age, height, weight, lung_capacity, grip_strength, pushups, step_test, vertical_jump, sit_and_reach, reaction_time, one_leg_stand, situps_1min
    )
    for metric, score in scores.items():
        print(f"{metric}: {score}")
