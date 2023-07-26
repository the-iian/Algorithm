def solution(s):
    answer = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    return ''.join(sorted(answer))


# python은 들여쓰기로 문법을 검증하므로 주의하자
print(solution('hello'))
