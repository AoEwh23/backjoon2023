b,c,d = map(int,input().split()) #(1 ≤ B, C, D ≤ 1,000)

burger = list(map(int,input().split()))
side = list(map(int,input().split()))
drink= list(map(int,input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

total=sum(burger)+sum(side)+sum(drink)
a=min(len(burger),len(side),len(drink))
discount=(sum(burger[:a])+sum(side[:a])+sum(drink[:a]))*0.9
aa=sum(burger[a:])+sum(side[a:])+sum(drink[a:])
disprice=int(discount+aa)


print(total)
print(disprice)