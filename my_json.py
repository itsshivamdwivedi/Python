# import json

# d='{
#     "name": "John",
#     "age": 30

# }'
# f=json.dumps(d)
# The format of the data   present in an json file is in string format


# print(f)


        #  How to convert Json to python objects
import json
d='{"name": "John","age": 30}'

f=json.loads(d)
print(f)
print(type(f))
for a in f:
    print(a,f[a])
 