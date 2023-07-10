primeiro = 0
segundo = 1
n = int(input())
for terceiro in range(0,n+1):
  if segundo > n:
    break
  print(segundo)
  terceiro = primeiro + segundo
  primeiro = segundo
  segundo = terceiro
