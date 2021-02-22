def solution(board, moves):
    result = []
    answer = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] > 0:
                result.append(board[i][move - 1])
                board[i][move - 1] = 0
                if result[-1:] == result[-2:-1]:
                    answer += result[-1:]
                    result = result[:-2]
                break
    return len(answer) * 2


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
