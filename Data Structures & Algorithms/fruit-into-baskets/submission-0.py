class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)
        types = 2
        left = max_fruits = 0
        basket = defaultdict(int)

        for right in range(n):
            basket[fruits[right]] += 1

            if len(basket) > types:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            else:
                max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
