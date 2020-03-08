def _hash(pattern, seed=None):
    # Use the FNV algorithm from http://isthe.com/chongo/tech/comp/fnv/
    if seed is None:
        seed = 0x01000193
    for c in pattern:
        seed = ((seed * 0x01000193) ^ ord(c)) & 0xFFFFFFFF
    return seed


data = {}
line = 1
for key in open("/usr/share/dict/words", "rt").readlines():
    data[key.strip()] = line
    line += 1

size = len(data)

# Place all of the keys into buckets
buckets = [[]] * size
G = [0] * size
values = [None] * size

for k in data.keys():
    buckets[_hash(k) % size].append(k)

# Sort the buckets and process the ones with the most items first.
buckets.sort(key=len, reverse=True)
for b in range(size):
    bucket = buckets[b]
    if len(bucket) <= 1:
        break
    d = 1
    item = 0
    slots = []
    while item < len(bucket):
        slot = _hash(bucket[item], seed=d) % size
        if values[slot] is not None or slot in slots:
            d += 1
            item = 0
            slots = []
        else:
            slots.append(slot)
            item += 1

    G[_hash(bucket[0]) % size] = d
    for i in range(len(bucket)):
        values[slots[i]] = data[bucket[i]]

freelist = [i for i, v in enumerate(values) if v is None]

for b in range(b, size):
    bucket = buckets[b]
    if len(bucket) == 0:
        break
    slot = freelist.pop()
    G[_hash(bucket[0]) % size] = -slot-1
    values[slot] = data[bucket[0]]


for word in ["hello", "goodbye", "dog", "cat"]:
    d = G[_hash(0, word) % len(G)]
    line = values[-d-1] if d < 0 else values[_hash(d, word) % len(values)]
    print("Word %s occurs on line %d" % (word, line))
