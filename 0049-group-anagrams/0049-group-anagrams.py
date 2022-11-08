class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        res = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in my_dict:
                my_dict[sortedWord].append(word)
            else:
                my_dict[sortedWord] = [word]
        for key in my_dict:
            res.append(my_dict[key])
        return res