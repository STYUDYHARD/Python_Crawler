# 保持热爱 奔赴山海

import json
import pandas as pd

# JSON文件路径
json_file_path = 'movies_data.json'
# CSV文件路径
csv_file_path = 'test_data.csv'

# 读取JSON文件
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 将JSON数据转换为DataFrame
df = pd.DataFrame(data)


# 将DataFrame写入CSV文件
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')  # 使用utf-8-sig编码确保中文等字符正确显示

print("转换完成, CSV文件已生成。")