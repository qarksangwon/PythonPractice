# 파이썬 피클(Pickle) 은 파이썬 객체를 직렬화(serialize) 하고 역직렬화(deserialize) 하는 모듈
# 피클을 사용하면 파이썬 객체를 파일에 저장하거나 네트워크를 통해 전송할 수 있다.
# 객체를 이진 형식 (binary) 으로 변환 저장해 필요 시 원래 상태로 복원 가능

import pickle

# 객체를 직렬화하여 파일에 저장하기
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
with open('문제풀이/data.pickle', 'wb') as file:
    pickle.dump(data, file)

# 파일에서 객체를 역직렬화하여 복원하기
with open('문제풀이/data.pickle', 'rb') as file:
    restored_data = pickle.load(file)

print(restored_data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

