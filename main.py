input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
if a==0:
    nod=b
elif b==0:
    nod=a
nok=int((int(data[0]) * int(data[1]))/nod)

output_data = open('output.txt', 'w')
output_data.write(str(nok))
input_data.close()
output_data.close()