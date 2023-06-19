import ast

def read_file(pos_file):
    f=open(pos_file,mode='r')
    lines =  f.read()
    f.close()
    return lines
    

pos = []
pos = eval(read_file("pos.txt"))
print(pos)
print(pos[0])
print(pos[0][2])
