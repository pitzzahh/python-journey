#  You can experiment here, it won’t be checked
height = 10
width = 35
length = 35

allowed = (height <= 10 < width <= 35 < length <= 40) or (height + width + length <= 80)

print(allowed)
