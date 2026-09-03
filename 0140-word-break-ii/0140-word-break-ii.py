class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        max_len = max(map(len, wordDict))

        @lru_cache(None)
        def dfs(start):
            if start == len(s):
                return [""]

            result = []

            # Only check lengths that can exist in the dictionary
            for end in range(start + 1, min(len(s), start + max_len) + 1):
                word = s[start:end]

                if word in word_set:
                    for rest in dfs(end):
                        if rest:
                            result.append(word + " " + rest)
                        else:
                            result.append(word)

            return result

        return dfs(0)