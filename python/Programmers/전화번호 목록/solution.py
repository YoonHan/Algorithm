def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book) - 1):
        selected = phone_book[i]
        if selected == phone_book[i + 1][:len(selected)]:
            answer = False
            break

    return answer
