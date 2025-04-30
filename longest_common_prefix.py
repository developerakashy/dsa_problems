def longest_common_prefix(strs):
    prefix = strs[0]

    for str in strs[1:]:
        prefix_len = len(prefix)

        while not str[:prefix_len+1] == prefix:
            prefix = prefix[:prefix_len]
            if prefix == "":
                return ""

            prefix_len -= 1

    return prefix

strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))
