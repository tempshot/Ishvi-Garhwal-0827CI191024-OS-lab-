# Priority non-preemptive with 0 arrival time.

process_no = int(input("Enter number of process: "))
pri_bt_p = []
tat = []
waiting = []

for i in range(process_no):
    p, bt, pri = map(int, input("\nEnter process number and it's bust time and priority (greater number represents hightest priority): ").split())
    pri_bt_p.append([pri, p, bt])

pri_bt_p.sort()
pri_bt_p.reverse()

sum = 0
for j in range(process_no):
    sum = sum + pri_bt_p[j][2]
    tat.append(sum)

for x in range(process_no):
    wt = tat[x] - pri_bt_p[x][2]
    waiting.append(wt)

avg_tat = 0
avg_wt = 0
for a in range(len(tat)):
    avg_tat = avg_tat + tat[a]
    avg_wt = avg_wt + waiting[a]


print('\nProcess |   Bust time   |  Priority   | Waiting time | Turn around time ')
print('--------------------------------------------------------------------------')

for y in range(process_no):
    print(pri_bt_p[y][1],'\t|  ',  pri_bt_p[y][1],'\t\t|',pri_bt_p[y][0],'\t\t|',waiting[y],'  \t\t|',tat[y])

print('\nAverage turn around time is:', avg_tat/len(tat))
print('\nAverage waiting time is', avg_wt/len(waiting))


