def solution(word, ch):
    index = -1
    for x in range(len(word)):
        if word[x] == ch:
            index = x
            break
    if index == -1: 
        return word
    else:
        first_segment = word[:index + 1]
        reversed_word = first_segment[::-1]
        second_segment = word[index + 1:]
        result = reversed_word + second_segment
        return result
print(solution("abcdefgh", "d"))

    