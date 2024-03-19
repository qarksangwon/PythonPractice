# 출력 정렬
# < 좌측 정렬
# > 우측 정렬 (default, 생략 시 우측 정렬)
# ^ 중앙 정렬
number = 125
print(f"[{number:<5}]")
print(f"[{number:5}]")
print(f"[{number:^5}]")
print(f"[{number:^6}]") # 규격 틀리면 오른쪽 한칸
print(f"{20.333333:.2f}") # .2f는 반올림 됨
print(f"{20.3355:.3f}") # 더 많은 소수점 이하 자리 표현은 반올림 없이 그냥 자름