# LJF non-preemptive with 0 arrival time

process_no = int(input('enter number of processes: '))
bt_p = []
tat = []
wt = []

for _ in range(process_no):
    p, bt = map(int, input("\nEnter process number and it's bust time: ").split())
    bt_p.append([bt, p])

bt_p.sort()
bt_p.reverse()

sum = 0
for j in range(process_no):
    sum = sum + bt_p[j][0]
    tat.append(sum)

for i in range(len(tat)):
    w = tat[i] - bt_p[i][0]
    wt.append(w)

avg_tat = 0
avg_wt = 0
for x in range(process_no):
    avg_tat = avg_tat + tat[x]
    avg_wt = avg_wt + wt[x]

print('\nProcess |   Bust time   | Waiting time | Turn around time ')
print('-------------------------------------------------------------------')

for y in range(process_no):
    print(bt_p[y][1],'\t|' , bt_p[y][0], '\t\t|' , wt[y],'\t\t|', tat[y])

print('\nAverage turn around time is',avg_tat/len(tat))
print('\nAverage waiting time is',avg_wt/len(wt))

