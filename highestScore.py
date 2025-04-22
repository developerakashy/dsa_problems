def highestScore(A):
        d = {}
        c = {}

        for arr in A:
            d[arr[0]] = d.get(arr[0], 0) + int(arr[1])
            c[arr[0]] = c.get(arr[0], 0) + 1

        for key, val in d.items():
              d[key] = d[key] // c[key]

        return d

l=[
  ['fqyh', 79],
  ['fqyh', 12],
  ['fqyh', 46],
  ['fqyh', 45],
  ['fqyh', 20],
  ['fqyh', 10],
  ['fqyh', 92],
  ['fqyh', 93],
  ['fqyh', 72],
  ['fqyh', 53],
  ['fqyh', 39],
  ['fqyh', 99],
  ['fqyh', 52],
  ['fqyh', 59]
]

print(highestScore(l))
