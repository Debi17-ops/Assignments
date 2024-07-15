'''x = [1, 2, 3]
y = [1, 2, 3]

result = [(i, j) for i in x for j in y if i != j]

print(result)'''




x=[1,2,3]
y=[1,2,3]

res=[]
for xi in x:
    for yi in y:
        if xi!=yi:
            t=(xi,yi)
            res.append(t)

print(res)
