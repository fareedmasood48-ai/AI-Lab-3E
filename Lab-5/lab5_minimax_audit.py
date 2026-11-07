"""Lab 5: Minimax and Alpha-Beta pruning with leaf-count audit."""
import math

SCORES = [3, 5, 2, 9, 3, 5, 2, 9]
TARGET_DEPTH = int(math.log2(len(SCORES)))

def minimax(depth, index, max_turn, scores, target_depth, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]
    left = minimax(depth + 1, index * 2, not max_turn, scores, target_depth, counter)
    right = minimax(depth + 1, index * 2 + 1, not max_turn, scores, target_depth, counter)
    return max(left, right) if max_turn else min(left, right)

def alphabeta(depth, index, max_turn, scores, target_depth, alpha, beta, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]
    if max_turn:
        value = float("-inf")
        for child in range(2):
            value = max(value, alphabeta(depth+1, index*2+child, False,
                                         scores, target_depth, alpha, beta, counter))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    value = float("inf")
    for child in range(2):
        value = min(value, alphabeta(depth+1, index*2+child, True,
                                     scores, target_depth, alpha, beta, counter))
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value

def run(scores):
    depth = int(math.log2(len(scores)))
    m_count, ab_count = [0], [0]
    m_value = minimax(0, 0, True, scores, depth, m_count)
    ab_value = alphabeta(0, 0, True, scores, depth, float("-inf"), float("inf"), ab_count)
    return m_value, m_count[0], ab_value, ab_count[0]

def main():
    print("Lab 5 — Minimax and Alpha-Beta")
    print("Scores:", SCORES)
    print("Minimax value / leaves:", run(SCORES)[:2])
    print("Alpha-Beta value / leaves:", run(SCORES)[2:])
    print("\nBranch-order comparison (Minimax value, leaves; Alpha-Beta value, leaves):")
    orders = [
        [3,5,2,9,3,5,2,9],
        [5,3,9,2,5,3,9,2],
        [9,2,5,3,9,2,5,3],
    ]
    for scores in orders:
        print(scores, "=>", run(scores))

if __name__ == "__main__":
    main()
