n = int(input('Enter number of processes: '))
l = []
ct = []
tat = []
wt = []

for _ in range(n):
    p, at, bt = map(int, input('\nEnter process number and its arrival time and bust time: ').split())
    l.append([at,p,bt])

l.sort()

a = 0
avg_tat = 0
avg_wt = 0

for i in range(n):

    # finding completion time 
    if l[i][0] == 0:
        ct.append(l[i][2])
        a = a + l[i][2]
    elif l[i][0] <= a:
        c = ct[-1] + l[i][2]
        ct.append(c)
    else:
        b = l[i][0] - a
        a =  a + b + l[i][2] 
        ct.append(a)

    # finding turn around time    
    t = ct[i] - l[i][0]
    tat.append(t)
    
    # finding waiting time
    w = tat[i] - l[i][2]
    wt.append(w)

    # finding average trun around time and average waiting time
    avg_tat = avg_tat + tat[i]
    avg_wt = avg_wt + wt[i]


print("\nProcess \t Arrival Time \t Burst time \t Waiting time \t Turn Around Time")
for j in range(n):
    print(l[j][1],'\t','\t','\t',l[j][0],'\t','\t',l[j][2],'\t','\t',wt[j],'\t','\t',tat[j])

print('\nAverage turn around time is',avg_tat/len(tat))
print('\nAverage waiting time is',avg_wt/len(wt))


