S = [];
K = [1, 2, 3];


for i in range(256):
    S.append(i)
   


j = 0


for i in range(256): 
    j = (j + S[i] + K[i % len(K) ]) % 256
    c = 0
    c = S[i]
    S[i] = S[j]
    S[j] = c


i = 0
j = 0


A = []
while (len(A) < 20):
    i = (i + 1) % 256
    j = (j + S[i]) % 256


    c=0 
    c = S[i]
    S[i] = S[j]
    S[j] = c


    output = S[(S[i] + S[j]) % 256]
    A.append(output)
print(A)
