import re

# Not letters
s = '2423'
r = re.match('[^A-z]*$', s)
print(r)

# Only numbers
s = '1212'
r = re.match('[0-9]*$', s)
print(r)

# Only upper case letters
s = 'ADSDD'
r = re.match('[A-Z]*$', s)
print(r)

# Only upper case letters
s = 'adadsa'
r = re.match('[a-z]*$', s)
print(r)

# Not numbers
s = 'xfgcf'
r = re.match('[^0-9]*$', s)
print(r)
