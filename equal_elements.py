def equal_exist(A, B):
        hashmap = {}
        n = len(A)

        for num in A:
            hashmap[num] = hashmap.get(num, 0) + 1
            hashmap[num+B] = hashmap.get(num+B, 0) + 1
            hashmap[num-B] = hashmap.get(num-B, 0) + 1


        if hashmap[max(hashmap, key=hashmap.get)] == n:
            return 1
        return 0

A=[2,3,1]
X=1

print(equal_exist(A, X))
