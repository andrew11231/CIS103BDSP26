#Andrew Espinoza
numberfile = 'C:/temp/p12number.txt'
numopen = open(numberfile,'r')
dataline = numopen.readline()
datalist = []
print(dataline)
while dataline != "":
     (month,data)= dataline.split(':')
     data = float(data)
     datalist.append(data)
     dataline = numopen.readline()

print(datalist)
print('Highest:',max(datalist))
print('Lowest:',min(datalist))
print('Total:',f'{sum(datalist):.3}'   )
print('Average:',f'{(sum(datalist)/len(datalist)):.3}')

numopen.close()
