def test_solution():
    assert solution(["119", "97674223", "1195524421"]) == False
    assert solution(["123", "456", "789"]) == True
    assert solution(["12", "123", "1235", "567", "88"]) == False


def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] in phone_book[j]:
                return False
    return True
