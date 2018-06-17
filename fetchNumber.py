text = "aAsmr3idd4bgs7Disf9eAF"

# 1. common solution
nums = list(map(str,range(0,10))) #convert int list to string list

fetchedNums = []
for it in text:
    if it in nums:
        fetchedNums.append(it)
print(''.join(fetchedNums))  #convert string list to string

# 2. regex
import re
print(''.join(re.findall(r'\d+',text)))

# 3. isdigit + for
print(''.join([i for i in text if i.isdigit()]))

# 4. filter + lambda + isdigit
print(''.join(list(filter(lambda x: x.isdigit(), text)))) 
