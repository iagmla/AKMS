from Crypto.Util import number

# Generates the AKMS S-boxes

for x in range(256):
    if number.isPrime(x):
        print(x)
a = ((139 * 42) + 241)
s0 = []
s1 = [0] * 256
for x in range(256):
    b = (((139 * 42) + x) * 29)  % 256
    s0.append(b)
    s1[b] = x
print(s0)
print(s1)
