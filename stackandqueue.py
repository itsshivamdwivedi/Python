# print("HEllo guys")
# stack and queue using the list 
# stack is the linear data structure stores data in linear format
# l=[]
# while True:
#     c=input('''

#     1. push
#     2. pop
#     3. peek
#     4. display
    
#     ''')
#     if c=='1':
#         l.append(int(input("enter the element")))
#         print(l)
#     elif c=='2':
#         if len(l)==0:
#             print("stack is empty")
#         else:
#              p= l.pop()
#              print(p)
#              print(l)
#     elif c=='3':
#         if len(l)==0:
#             print("stack is empty")
#         else:    
#              print("the last stack value is",l[-1])
#     elif c=='4':
#          print("display stack,",l)
#     else:
#         print("invalid input")
    #  Queue using list first in first out

l=[]
while True:
    c=input('''

    1. push
    2. pop first element
    3. front
    4.last
    5. display list
    
    ''')
    if c=='1':
        l.append(int(input("enter the element")))
        print(l)
    elif c=='2':
        if len(l)==0:
            print("stack is empty")
        else:
            #  p= l.pop()
             del l[0]
            #  print(p)
             print(l)
    elif c=='3':
        if len(l)==0:
            print("stack is empty")
        else:    
             print("the first element value is",l[0])
    elif c=='4':
         if len(l)==0:
             print("stack is empty")
         else: 
            print("the last element value is",l[-1])
    elif c=='5':
        print("display stack,",l)
        break;
    else:
        print("invalid input")
