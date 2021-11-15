page_frames = int(input('Enter number of page frames: '))
process_page = int(input('Enter number of process pages: '))
pf = []
pp = []
fault = 0

for i in range(process_page):
    print('Enter',i+1,'process page: ',end=' ')
    p = int(input())
    pp.append(p)

for j in range(process_page):
    if len(pf) < page_frames:
        pf.append(pp[j])
        fault = fault + 1

    elif pp[j] in pf:
        for a in range(len(pf)):
            if pp[j] == pf[a]:
                pf.remove(pf[a])
                pf.append(pp[j])
            break
    else:
        pf.remove(pf[0])
        pf.append(pp[j])
        fault = fault + 1

miss_ratio = fault/process_page
hit_ratio = (process_page-fault)/process_page

print('Total page fault:',fault)
print('Hit ratio is: %.2f'%hit_ratio,'%')
print('Miss ratio is: %.2f'%miss_ratio,'%')


