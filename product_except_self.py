def product_except_self(nums): #Due to dynamic array it takes more than O(n) can be said amortized
    L = [1]
    R = [1]
    p = []

    l_prod = 1 * nums[0]
    for i in range(1, len(nums)):
        L.append(l_prod)
        l_prod *= nums[i]

    r_prod = 1 * nums[-1]
    for i in range(len(nums) - 2, -1 , -1):
        R.insert(0, r_prod)
        r_prod *= nums[i]

    for i in range(len(nums)):
        p.append(L[i]*R[i])

    return p

def optimal(nums):
    n = len(nums)
    product = [1] * n

    prefix = 1
    for i in range(n):
        product[i] *= prefix
        prefix *= nums[i]

    suffix = 1
    for j in range(n - 1, -1, -1):
        product[j] *= suffix
        suffix *= nums[j]

    return product

nums = [1, 2, 3, 4]
print(product_except_self(nums))
print(optimal(nums))
