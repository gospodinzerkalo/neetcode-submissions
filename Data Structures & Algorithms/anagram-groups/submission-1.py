class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        alp = 'abcdefghijklmnopqrstuvwxyz'
        alpD = {}
        for i in range(len(alp)):
            alpD[alp[i]] = i

        for w in strs:
            d = [0] * 26
            for i in w:
                d[alpD[i]] += 1
            dStr = ", ".join([str(x) for x in d])
            if dStr in di:
                di[dStr].append(w)
            else:
                di[dStr] = [w]
    
        res = []
    
        for k in di:
            res.append(di[k])
        return res