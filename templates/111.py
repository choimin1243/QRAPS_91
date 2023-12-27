import re

# 검출할 문자열
문자열 = "이것은 J 값과 F 값입니다. Falling과 같은 단어와 함께 A, B, G,M, Z도 검출되어야 합니다."

# 검출할 값 리스트
tolerance_values = ["J", "F", "A", "B", "G", "M", "Z"]

# 정규표현식 패턴 생성
패턴 = r'(?<!\w)(?:' + '|'.join(tolerance_values) + r')(?!\w)'

# 정규표현식을 사용하여 검출
검출된_값 = re.findall(패턴, 문자열)

# 결과 출력
print(검출된_값)
