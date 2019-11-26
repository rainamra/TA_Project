#6
def histogram (list:[int]):
    for i in  (list):
        print ("*" * i)
histogram([4, 9, 7])

#7
def string_to_int (list:[str]):
    intList : [int] = []
    for i in list:
        intList.append(len(i))
    return intList
print(string_to_int(["aaa", "ccc"]))

#4
def is_member(char:str, list: [str]):
    for i in list:
        if char == i:
            return True
    return False
print(is_member("a", ["c", "b", "d"]))
print(is_member("d", ["c", "b", "d"]))

#5
def overlapping (list1 : [str], list2 : [str]):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False
print(overlapping(["r", "g", "i"], ["p", "j", "r"]))
print(overlapping(["r", "g", "i"], ["p", "j", "d"]))

#2
def translate (stnc:str):
    vowel = "aiueo "
    stnc = list(stnc)
    for i in stnc:
        if i not in vowel:
            stnc[stnc.index(i)] = i + 'o' + i
    return (''.join(stnc))

print(translate("this is fun"))

#1
sample_data = "3, 5, 7, 23"
sample_data = sample_data.replace(",", "")
newdataArr = sample_data.split()
print(newdataArr)
print(tuple(newdataArr))







