def solution(s):
    return " ".join([word.capitalize() for word in s.lower().split(" ")])