class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) == len(t)):
            s_dic = {}
            t_dic = {}

            for i in range(0,len(s)):
                if s[i] not in s_dic:
                    s_dic[s[i]] = 1
                else:
                    s_dic[s[i]] += 1

                if t[i] not in t_dic:
                    t_dic[t[i]] = 1
                else:
                    t_dic[t[i]] += 1

            lst = s_dic.items()
        
            for tup in lst:
                if tup[0] not in t_dic:
                    return False
                if t_dic[tup[0]] != tup[1]:
                    return False

            return True

        return False