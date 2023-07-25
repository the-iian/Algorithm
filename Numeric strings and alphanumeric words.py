def solution(s):
    
    # answer를 문자열로 저장
    answer = s
    
    # 문자열 - 숫자만 딕셔너리를 생성
    units = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    # 딕셔너리에서 key, value를 꺼내는 반복문 실행
    for key, value in units.items():

        # answer에서 key를 value로 변환
        answer = answer.replace(key, value)
        
    return int(answer) 