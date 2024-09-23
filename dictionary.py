course={
    'php':{'duration':'3months','fees':20000},
    'python':{'duration':'6months','fees':20000},
    'java':{'duration':'12months','fees':20000},
    'c++':{'duration':'18months','fees':20000},
    'c#':{'duration':'24months','fees':20000},
}
# print(course['php'])
# print(course.items())   # it returns all the items of the dictionary
# print(course.values())   #it returns all the values of the dictionary
# course['php']['fees']   = 40000  
# print(course['php'])
for k,v in course.items():
    print(k,v['duration'],v['fees']) 
# The above loop retuns a key value pairs of the dictionary course
