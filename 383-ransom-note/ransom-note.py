class Solution:
    def str_to_Dict(self, string: str) -> dict:
        dict_ret = {}
        for ch in string:
            if ch in dict_ret:
                dict_ret[ch] += 1
            else:
                dict_ret[ch] = 1

        return dict_ret 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_dict = self.str_to_Dict(ransomNote)
        mag_dict = self.str_to_Dict(magazine)

        for ch in note_dict:
            if ch not in mag_dict:
                return False
            else:
                if note_dict[ch] > mag_dict[ch]:
                    return False

        return True