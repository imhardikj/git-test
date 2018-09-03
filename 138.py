filename = '132_pi_digits.txt'

with open(filename) as asd:
    lines = asd.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
