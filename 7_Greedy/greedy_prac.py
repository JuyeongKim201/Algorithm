def fractional_knapsack(items, capacity):
    # Step 1: 기준 정의
    # 무게당 가치를 계산하여 물건들을 정렬
    # 무게당 가치가 높은 물건부터 선택하는 것이 기준이 됩니다.
    items.sort(key=lambda item: item[1]/item[0], reverse=True)
    
    total_value = 0  # 배낭의 총 가치
    for item in items:
        weight, value = item
        
        # Step 2: 최적의 선택
        # 무게 제한 내에서 무게당 가치가 가장 높은 물건부터 선택하여 배낭에 넣습니다.
        if capacity >= weight:
            capacity -= weight  # 배낭의 남은 무게 업데이트
            total_value += value  # 배낭의 총 가치 업데이트
        else:
            # 무게 제한이 남아 있지만 물건을 완전히 담을 수 없는 경우,
            # 물건을 분할하여 배낭에 넣습니다.
            fraction = capacity / weight  # 분할 비율 계산
            total_value += value * fraction  # 분할된 물건의 가치를 총 가치에 추가
            break  # 배낭의 무게 제한에 도달했으므로 종료
        
        # Step 3: 결과 확인 및 선택 수정
        # 분할 가능 배낭 문제에서는 이전의 선택을 수정할 필요가 없습니다.
        
        # Step 4: 반복
        # 물건을 선택하여 배낭에 넣는 과정을 반복합니다.
        # 배낭의 무게 제한에 도달할 때까지 무게당 가치가 높은 물건을 선택하여 배낭에 넣습니다.
    
    return total_value  # 배낭의 총 가치 반환

# 예제 물건들과 배낭의 무게 제한
items = [(2, 3), (3, 4), (4, 5)]
capacity = 5
# 분할 가능 배낭 문제 해결
result = fractional_knapsack(items, capacity)
print(result)  # 출력: 7.0
