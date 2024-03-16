import re

string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
# 'I AM NOT YELLING', she said. Though we knew it to not be true.
print(string)

new = re.sub('[A-Z]', '', string)
# '   ', she said. hough we knew it to not be true.
print(new)

new = re.sub('[a-z]', '', string)
# 'I AM NOT YELLING',  . T       .
print(new)

new = re.sub('[.,\'a-z]', '', string)
# I AM NOT YELLING   T
print(new)

new = re.sub('[.,\'a-zA-Z]', '', string)
#
# there is only empty spaces remaining
print(new)

new = re.sub('[.,\'a-zA-Z+" "]', '', string)
#
# thers is nothing
print(new)

new = re.sub('[.,\'a-z+" "]', '', string)
# IAMNOTYELLINGT
print(new)

string = string + "2 1 3 - 6"
new = re.sub('[^0-9]', '', string)
# 2136
print(new)