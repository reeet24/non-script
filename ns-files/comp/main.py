import os
import sys
import syntax as syn

file=sys.argv[1]
try:
    Flag=sys.argv[2]
except:
    Flag='n'
endFile=file[:-3]
endFile+=".py"
filecont=[]
pyString=()

try:
    if file.endswith('.ns')==False:
        print(f'File {file} invalid filetype')
        exit

    with open(file,'r')as f:
        for line in f:
            for word in line.split():
                filecont.append(word)
            filecont.append('\n')
    try:
        for a in filecont:
            pyString+=f'{syn.assignTk(a)}'

        with open((f'temp/{endFile}'),'w') as o:
            o.write(pyString)
    except:
        print(f'Unknown error')
except:
    print(f'File: {file} Not Found')

try:
    if Flag=='d':
        os.system(f'python temp/{endFile}')
    if Flag=='c':
        os.remove(f'temp/{endFile}')
    if Flag=='n':
        os.system(f'python temp/{endFile}')
        os.remove(f'temp/{endFile}')
except:
    print('Invalid Syntax')
