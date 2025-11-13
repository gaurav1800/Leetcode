class Solution:
    def hIndex(self, citations: List[int]) -> int:

      # bucket sort
        total = 0
        n = len(citations)
        counter = [0] * (n + 1)

        for cit in citations:
            counter[min(cit, n)] += 1

        for i, count in reversed(list(enumerate(counter))):
            total += count
            if total >= i:
                return i
        return 0

        # slower: O(nlogn) = O(sort())
        # citations.sort()
        # n = len(citations)
        # for i, number in enumerate(citations):
        #     if number >= n - i:
        #         return n - i
        # return 0  