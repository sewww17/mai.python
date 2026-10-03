a = input()
ans = {}
for i in set(a):
    ans[f'{i}'] = a.count(i)
print(ans)