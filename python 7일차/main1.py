import mymath

# 삼각형 넓이 계산
base = 10
height = 5
print(f"삼각형의 넓이: {mymath.triangle_area(base, height)}")

# 원의 넓이 계산
radius = 7
print(f"원의 넓이: {mymath.circle_area(radius)}")

# 직육면체의 겉넓이 계산
length = 4
width = 5
height = 6
print(f"직육면체의 겉넓이: {mymath.cuboid_area(length, width, height)}")

import os
print("현재 작업 경로:", os.getcwd())