with open ("test.txt", "r") as f:
    print(type(f))
    data = f.read(3)
    f.truncate(5)
  
    print(data)