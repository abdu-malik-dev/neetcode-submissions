class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict: key=alpha value=list of words
        resultdict = {}

        letterindex = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3,
    'e': 4, 'f': 5, 'g': 6, 'h': 7,
    'i': 8, 'j': 9, 'k': 10, 'l': 11,
    'm': 12, 'n': 13, 'o': 14, 'p': 15,
    'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23,
    'y': 24, 'z': 25
}
        
        alpha = 26 * [0] # increment index for the charecter count

        for word in strs:
            for character in word:
                alpha[letterindex[character]] += 1 
            alphatuple = tuple(alpha)
            if alphatuple not in resultdict:
                resultdict[alphatuple] = []
            resultdict[alphatuple].append(word)
            alpha = 26 * [0]
        res = []
        for i in resultdict:
            res.append(resultdict[i])

        return res 

                
