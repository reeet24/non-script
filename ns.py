import os
import sys
import syntax as syn

file = sys.argv[1]
try:
    Flag = sys.argv[2]
except:
    Flag = 'n'
endFile = file[:-3]
endFile += ".py"
filecont = []
pyString = ""

try:
    if file.endswith('.ns') == False:
        print(f'File {file} invalid filetype')
        exit

    with open(file,'r') as f:
        for line in f:
            for word in line.split():
                filecont.append(word)
            filecont.append('\n')
    try:
        for a in filecont:
            pyString += f'{syn.assignTk(a)}'

        if Flag == 'c':
            with open((f'comp/{endFile}'),"w") as o:
                o.write(pyString)
            print(f'Compiled {endFile} into /comp !')
        if Flag == "d":
            with open((f'temp/{endFile}'),"w") as o:
                o.write(pyString)
            os.system(f'python temp/{endFile}')
        if Flag == 'n':
            with open((f'temp/{endFile}'),"w") as o:
                o.write(pyString)
            os.system(f'python temp/{endFile}')
            os.remove(f'temp/{endFile}')
        if Flag == '-c':
            with open((f'temp/{endFile}'),"w") as o:
               o.write(pyString)
            os.system(f'pyinstaller --onefile temp/{endFile}')
            os.remove(f'temp/{endFile}')

    except:
        print(f'Unknown error')
except:
    print(f'File: {file} Not found')