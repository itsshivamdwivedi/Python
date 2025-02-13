#write a python program to translate a message into the secret code

# st = input("Enter the message  ")
# words= st.split("  ")
# coding = input("1 for coding 0 for decoding ")
# coding = True if (coding=="1") else False
# if(coding):
#   nwords=[ ]
#   for word in words:
#    if(len(word)>=3):
#       r1="dsf"
#       r2="jkr"
#       stnew =r1 +word[1:]+ word[0]+r2
#       nwords.append(stnew)
#    else:
#      nwords.append(word[::-1])
#      print(" ".join(nwords))
# else:
#     nwords = [ ]
#     for word in words:
#         if (len(word) >= 3):
#             r1 = "dsf"
#             r2 = "jkr"
#             stnew =  word[3:-3]
#             stnew = stnew[-1]+ stnew[:-1]
#             nwords.append(stnew)
#         else:
#          nwords.append(word[::-1])
#     print(" ".join(nwords))
#     pass
#     print(nwords)

#  write a python program to find a duplicate element in a list
lst=[1,2,3,4,3,5,6,7]
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]==list[j]:
#             print(list[i] ,"is a duplicate")
#             break
#O(n²) (slow for large lists)  My program is slow for the larger lists
# Efficient way to do for the larger lists would be 
lst=[1,2,3,4,3,5,6,7]
def find_duplicates(lst):
    seen = set()
    duplicates= set()

    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(find_duplicates(lst))

# Program breakdown:-
# 1.	seen set keeps track of all seen element in a list 
# 2.	then duplicates set stores the element that are encountered more than once i.e duplicate
# 3.	For loop through the list :  for each element in the list check if already seen
# 4.	If yess it’s a duplicate then add it to the duplicate 
# 5.	If no then add it to the seen 
# 6.	Then convert the duplicates set into the list using list(duplicates) and return it
