# birthday cake candles, works
n = input("")
n = int(n)
h = input("")
h = list(h.split())

def birthdayCakeCandles(h):
    for i in range(len(h)):
        h[i]=int(h[i])
    return(h.count(max(h)))

print(birthdayCakeCandles(h))
