# 회문 판별하기
# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 말합니다.
# 예를 들면 "level", "SOS", "rotator", "nurses run"과 같은 단어와 문장이 있지요.
import string
word = input('단어를 입력하세요: ')
word = word.lower()
word = word.strip(string.punctuation + ' ')
is_palindrome = True  # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):  # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:  # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        is_palindrome = False  # 회문이 아님
        break
print(is_palindrome)  # 회문 판별값 출력

# 시퀀스 뒤집기로 문자 검사하기
word = input('단어를 입력하세요: ')

print(word == word[::-1])  # 원래 문자열과 반대로 뒤집은 문자열을 비교

# 이하 영상 참조 #

text = 'Hello'

# 28.2.1  반복문으로 N-gram 출력하기
for i in range(len(text) - 1):  # 2-gram이므로 문자열의 끝에서 한 글자 앞까지만 반복함
    print(text[i], text[i + 1], sep='')  # 현재 문자와 그다음 문자 출력

text = 'this is python script'
words = text.split()  # 공백을 기준으로 문자열을 분리하여 리스트로 만듦

for i in range(len(words) - 1):  # 2-gram이므로 리스트의 마지막에서 요소 한 개 앞까지만 반복함
    print(words[i], words[i + 1])  # 현재 문자열과 그다음 문자열 출력

# zip으로 2-gram 만들기
text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')

text = 'hello'
list(zip(text, text[1:]))

# 이하 영상 참조 #
