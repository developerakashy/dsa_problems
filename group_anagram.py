from collections import defaultdict
def group_anagram1(strs): #naive solution not good
    strs_dict = {key:1 for key in strs}

    grouped = []
    for key in strs:
        if key not in strs_dict:
            continue

        temp_arr = []
        temp_dict = {}


        temp_arr.append(key)
        strs_dict[key] -= 1

        if strs_dict[key] == 0:
            del strs_dict[key]

        for s in strs:
            if s not in strs_dict:
                continue

            for char in key:
                if char in temp_dict:
                    temp_dict[char] += 1
                else:
                    temp_dict[char] = 1

            for char in s:
                if char not in temp_dict:
                    break
                temp_dict[char] -= 1

                if temp_dict[char] == 0:
                    del temp_dict[char]

            if not temp_dict:
                temp_arr.append(s)
                del strs_dict[s]

            temp_dict = {}

        grouped.append(temp_arr)

        print(strs_dict)

    return grouped


def optimal(strs):
    grouped = {}

    for s in strs:
        key = "".join(sorted(s))
        if key not in grouped:
            grouped[key] = []

        grouped[key].append(s)

    return list(grouped.values())

strs = ["eat", "ate", "tea", "bat", "nat", "tan"]
print(group_anagram1(strs))
print(optimal(strs))
