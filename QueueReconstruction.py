class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        # sort in descending order of heights and ascending number of people
        people.sort(key = lambda x: (-x[0], x[1]))
        o = []
        for p in people:
            o.insert(p[1], p)
        return o
