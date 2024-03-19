# 슬라이싱은 값 변경해도 원본 데이터는 변경되지 않는다.
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
slice1 = list1[2:7]    # 2부터 7미만
slice2 = list1[1:9:2]  # 1부터 9미만 2간격
slice3 = list1[5:] # 5부터 끝까지
slice4 = list1[-7:] # 뒤에서 부터 7개
slice5 = list1[:3] # 처음 부터 3미만
slice6 = list1[:-3] # 처음 부터 뒤에서 3개 빼고 전까지
print(slice1)
print(slice2)
print(slice3)
print(slice4)
print(slice5)
print(slice6)

jumin = "991120-1234567"
print(jumin[7])


str1 = "Hello Python"
print(str1.upper()) #대문자
print(str1.lower()) #소문자

str2 = "Hello Java"
print(str2.replace("Java","Python")) # 변경하기

str3 = "문자 개수 세기 및 문자의 길이"
print(f"문 : {str3.count('문')} 개") #문자 개수 세기
print(len(str3))
print(str3.__len__())
print(str3.find("문")) # 찾은 문자 index 반환, 중복 시 앞에거, 없으면 -1
print(str3.rfind("문")) # 뒤에서 찾음
print(str3.index("문")) # 얘는 없으면 ValueError

str4 = """
      안녕~
     요종도 공백
"""
print(str4.strip()) # 맨 앞과 맨 뒤의 공백 없앰 (중간은 안 없앰)