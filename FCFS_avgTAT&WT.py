# Average turn around and waiting time with 0 arrival time.

from operator import add as a

process_no = int(input("Enter number of process: "))
process = []
bust = []
waiting = [0] 

print()

for _ in range(process_no):
    p, bt = map(int, input('Enter process number and its bust time: ').split())
    process.append(p)
    bust.append(bt)

for i in range(len(bust)-1):
    wt = waiting[i] + bust[i]
    waiting.append(wt)

tat = list(map(a, bust,waiting))

print()

print('Process |   Bust time   | Waiting time | Turn around time ')
print('----------------------------------------------------------')

for j in range(process_no):
    print(process[j],'\t|  ',  bust[j],'\t\t|',waiting[j],'\t\t|',tat[j])

print()

sum_wt = sum(waiting)
print("Average waiting time is:",sum_wt/len(waiting))

sum_tat = sum(tat)
print("Average turn around time is:",sum_tat/len(tat))



