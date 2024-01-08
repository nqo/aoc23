#AoC 2023 Day 1 Part 1

#name var that we are looking for slcv - sum line calibration value
slcv=0

#fake first and last
#first=7
#last=3
#combine two digits (first and last) into a single number called lcv (line calibration value)


#open calibration data document and read it line by line
for line in open('calibdata.txt'):
    first=''
    last=''
    lcv=0
    for char in line:
        if first=='' and char.isdecimal():
            first=int(char)
        elif char.isdecimal():
            last=int(char)
            lcv=first*10+last
    if last=='':
        last=first
        lcv=first*10+last
    slcv+=lcv
    print(line,first,last,lcv,slcv)

print(slcv)




