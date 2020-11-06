from collections import OrderedDict

strings = ["ABC", "ABDDDD", "XYZ"]
numbers = [1, 1, 1, 1, 1, 2, 2, 3, 3]

# 리스트의 원소를 한 줄로 이어 붙인다.
string = ''.join(strings)           # ABCABDDDDXYZ
num = ''.join(map(str, numbers))    # 111112233

# set을 이용하여 중복을 제거 후 리스트로 바꾼다.
print(list(set(''.join(strings))))
print(list(set(''.join(map(str, numbers)))))

# 문자열을 순서대로 정렬하고 싶다면 OrderedDict를 이용한다.
print(''.join(OrderedDict.fromkeys(string)))
print(''.join(OrderedDict.fromkeys(num)))