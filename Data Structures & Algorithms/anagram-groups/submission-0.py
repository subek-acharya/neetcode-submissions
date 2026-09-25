class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list) # Maps char count -> lists of anagrams

        for s in strs:   # loops over each string in list of strings
            count = [0] * 26 # [0,0,0,0,.......]

            for char in s:
                count[ord(char) - ord('a')] += 1 
                # creates a unique counter (1,0,2) for each string
            
            hash_map[tuple(count)].append(s) 
            # Groups strings based on keys

        return list(hash_map.values())



            

