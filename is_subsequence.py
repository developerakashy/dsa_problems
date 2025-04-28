def isSubsequence(s, t):

        curr = 0
        for i in range(len(t)):
            if curr == len(s):
                return True
            if t[i] == s[curr]:
                curr += 1

        return curr == len(s)


s = "abc"
t = "ahbbgd"

print(isSubsequence(s, t))
