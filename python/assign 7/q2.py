'''def speed(distance,time):
    speed=[]
    i=j=0
    n1=len(distance)
    n2=len(time)
    while i<n1 and j<n2:
        speed.append(distance[i]/time[j])
        i+=1
        j+=1
    return speed

dist=[10,20,30,40,50]
time=[1,5,3,2,4]
res=[]

res=speed(dist,time)
print(res)'''



def speed(distance,time):
    speed=[distance[i]/time[i] for i in range(len(distance))]
    return speed
dist=[10,20,30,40,50]
time=[1,5,3,2,4]
res=[]

res=speed(dist,time)
print(res)

