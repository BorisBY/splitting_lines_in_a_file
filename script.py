import os
import re

def check():
    filename_out = '/home/ubuntu/Old version/win_fixed.json'
    with open(filename_out) as f:

        temp = 0
        stroki = 1
        final_text = ''

        for line in f:
            if line.startswith('{"Timestamp"') == False:
                print('error! stroka %s ne nachinaetsy s timestamp\n' % stroki)

            # flag = re.findall('{"Timestamp"', line)
            stroki += 1
            if line =='':
                print('error - stroka %s pustaya' % stroki)




filename = '/home/ubuntu/Old version/win_part6.json'
filename_out = '/home/ubuntu/Old version/win_fixed.json'
# file_source = open(filename, 'r')
file_out = open(filename_out, 'w')
# source_text = file_source.read()
# file_source.seek(0)


with open(filename) as f:
    temp = 0
    stroki = 1
    final_text = ''


    for line in f:
        flag = re.findall('{"Timestamp"', line)
        stroki +=1
        if len(flag)>1:
            print('string  %s split \n' % stroki)
            temp = [m.start() for m in re.finditer('{"Timestamp"', line)]
            for j in range(len(temp)):
                try:
                    beg = temp[j]
                    if (j+1)>=len(temp):
                        end = -1
                    else:
                        end = temp[j+1]

                    str = line[beg:end] + '\n'
                    file_out.write(str)
                except:
                    print('error!\n')
                    break
            continue
        file_out.write(line)
        # final_text+=line
file_out.close()
f.close()


check()



        # string = line

"""
def change_the_number_of_iterations():
    iter = '\t'+"self.iterations=" + str(iterations)+'\n'
    temp=''
    fileName = os.path.expanduser('~') + '/canvas/udpportscan/udpportscan.py'
    file = open(fileName, 'r')
    text = file.read()
    file.seek(0)
    for line in file:
        if 'self.iterations=' in line:
            temp = line
    file.close()
    if iter in text:
        return
    else:
        ReplaceLineInFile(fileName, text, temp, iter)
"""