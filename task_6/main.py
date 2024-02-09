def greedy_algorithm(items, budget):
    items_with_ratio = []

    for key, value in items.items():
        items_with_ratio.append({
            "item": key,
            "ratio": value["cost"] / value["calories"],
            "cost": value["cost"],
            "calories": value["calories"]
        })

    items_with_ratio.sort(key=lambda x: x["ratio"], reverse=True)
    total_cost = 0
    selected_items = []

    for item in items_with_ratio:
        if total_cost + item["cost"] <= budget:
            total_cost += item["cost"]
            selected_items.append(item["item"])

    return selected_items


def dynamic_programming(items, budget):
    n = len(items)
    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]

    for i, (item, values) in enumerate(items.items(), 1):
        for j in range(1, budget + 1):
            if values["cost"] > j:
                K[i][j] = K[i - 1][j]
            else:
                K[i][j] = max(K[i - 1][j], K[i - 1][j - values["cost"]] + values["calories"])

    result = []
    j = budget
    for i in range(n, 0, -1):
        if K[i][j] != K[i - 1][j]:
            result.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]

    return result


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    res_greedy_algorithm = greedy_algorithm(items, 100)

    print(f"Greedy algorithm: {res_greedy_algorithm}")

    res_dynamic_programming = dynamic_programming(items, 100)
    print(f"Dynamic programming: {res_dynamic_programming}")



