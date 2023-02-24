def solution(phone_number):
    last_four = phone_number[-4::]
    answer = "*" * (len(phone_number)-4) + last_four
    return answer