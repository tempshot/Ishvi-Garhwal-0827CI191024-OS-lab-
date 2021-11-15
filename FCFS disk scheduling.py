n = int(input('Enter number of sequence: '))
queue = []
moment = []
total = 0
for i in range(n):
    print('Enter',i+1,'sequence:', end=' ')
    x = int(input())
    queue.append(x)

head = int(input('Enter head: '))
moment.append(abs(queue[0]-head))

for j in range(len(queue)-1):
    moment.append(abs(queue[j]-queue[j+1]))

for a in moment:
    total = total + a

print('Total seek count is:',total)
print('Seek sequnce is:', queue)



