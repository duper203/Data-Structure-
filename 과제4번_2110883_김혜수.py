#03장 3번
#문자열이 회문인지 검사는 함수를 재귀 함수로 작성
def palindrome(word):           #회문 판별 함수

    if len(word) < 2:           #문자열 양쪽에서부터 검사하다가 중앙에 하나가 남거나 더 이상 확인할 문자열이 없을 경우
        return True             #더 이상 회문임을 확인 할 필요가 없다.
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1]) #재귀함수 이용


word1 = input("문자열 입력하세요")
palindrome(word1)               #회문 판별 함수

if palindrome(word1) == True:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")