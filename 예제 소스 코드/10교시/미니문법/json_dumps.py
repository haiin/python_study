﻿import json

# 리스트 데이터를 JSON 데이터로 변환
my_list = ["cat", "dog", "pig"]
to_json = json.dumps(my_list)

# 변수 타입과 내용 출력
print(type(to_json))
print(to_json)
