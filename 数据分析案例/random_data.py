import random
import uuid
from datetime import datetime, timedelta
import json

# 定义省份列表
provinces = ["河南省", "广东省", "江苏省", "山东省", "浙江省", "安徽省", "湖南省", "四川省", "陕西省", "河北省"]

# 生成随机日期
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds 
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

# 生成随机数据行（CSV格式）
def generate_random_line():
    date = random_date(datetime(2024, 1, 1), datetime(2024, 1, 31)).strftime("%Y-%m-%d")
    unique_id = str(uuid.uuid4())
    random_number = random.randint(900, 3000)
    province = random.choice(provinces)
    return f"{date},{unique_id},{random_number},{province}"

# 生成并写入txt文件
with open("数据分析案例/data_output.txt", "w", encoding='utf-8') as file:
    for _ in range(30):  # 生成100行数据
        file.write(generate_random_line() + "\n")

# 生成并写入json文件
with open("数据分析案例/data_output.json", "w", encoding='utf-8') as file:
    for i in range(30):  # 生成100行数据
        data = generate_random_line().split(",")
        json_data = json.dumps({
            "date": data[0],
            "order_id": data[1],
            "money": int(data[2]),
            "province": data[3]
        }, ensure_ascii=False)
        file.write(json_data + "\n")  # 确保每个json对象占一行，并在最后一个对象前不加逗号
