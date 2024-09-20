course={
    'php':{'duration':'3months','fees':20000},
    'python':{'duration':'6months','fees':20000},
    'java':{'duration':'12months','fees':20000},
    'c++':{'duration':'18months','fees':20000},
    'c#':{'duration':'24months','fees':20000},
}
print(course['php'])
course['php']['fees']   = 40000  
for k,v in course.items():
    print(k,v['duration'],v['fees']) 