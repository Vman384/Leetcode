from typing import List


def finalPrices(n: int, price: List[int], q: int, queries: List[List[int]]) -> List[int]:
    for query in queries:
        if query[0] == 1:
            price[query[1]-1] = query[2]
        elif query[0] == 2:
            for index, item in enumerate(price):
                if item < query[1]:
                    price[index] = query[2]
    print(price)
    return price

finalPrices(n = 3, price = [7, 5, 4], q = 3, queries = [[2, 6, 6], [1, 2, 9], [2, 8, 8]])