text = "devi"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1
print(frequency)
#output:
{'d': 1, 'e': 1, 'v': 1, 'i': 1}
