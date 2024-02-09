import random
from collections import defaultdict

import matplotlib.pyplot as plt



def main():
    nums = 1_000_000

    counts = defaultdict(int)

    for _ in range(nums):
        dice = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        key = str(dice + dice_2)
        counts[key] += 1

    probabilities = {key: count / nums for key, count in counts.items()}

    print("Dice | Probability")
    print("-----|------------")
    for dice, prob in probabilities.items():
        print(f"{dice} | {prob:.2%}")

    plt.bar(probabilities.keys(), probabilities.values())  # noqa
    plt.show()


if __name__ == "__main__":
    main()
