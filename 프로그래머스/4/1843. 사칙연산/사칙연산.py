def solution(arr):
    answer = -1
    # DP: 구하고자 하는 것: 0~n-1의 최댓값 구하기
    # 0~k 의 최댓값 + k+1~n-1의 최댓값 들 중, 최댓값이 구하는 값

    # 초기값
    nums = arr[::2]
    ops = arr[1::2]
    ln = len(nums)
    lo = len(ops)

    # 메인
    max_sum = dict()
    min_sum = dict()
    for i in range(ln):
        max_sum[(i, i)] = int(nums[i])
        min_sum[(i, i)] = int(nums[i])

    for d in range(1, lo + 1):
        for i in range(ln - 1):
            j = i + d

            if j >= ln:  # j가 index 범위 넘어가면 예외 처리
                continue

            max_part = []
            min_part = []
            for k in range(i, j):
                if ops[k] == '+':
                    max_num = max_sum[(i, k)] + max_sum[(k+1, j)]
                    min_num = min_sum[(i, k)] + min_sum[(k+1, j)]
                    max_part.append(max_num)
                    min_part.append(min_num)
                if ops[k] == '-':
                    max_num = max_sum[(i, k)] - min_sum[(k+1, j)]
                    min_num = min_sum[(i, k)] - max_sum[(k+1, j)]
                    max_part.append(max_num)
                    min_part.append(min_num)
            max_sum[(i, j)] = max(max_part)
            min_sum[(i, j)] = min(min_part)
    return max_sum[(0, ln - 1)]
