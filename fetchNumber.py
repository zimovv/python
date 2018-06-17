text = "aAsmr3idd4bgs7Disf9eAF"

nums = list(map(str,range(0,10))) #convert int list to string list

fetchedNums = []
for it in text:
    if it in nums:
        fetchedNums.append(it)
print(''.join(fetchedNums))  #convert string list to string 
