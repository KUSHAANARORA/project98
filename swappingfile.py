def swappingfile():
    f1 = input("enter the name of the first file:")
    f2 = input("enter the name of the second file:")
    with open(f1,"r") as dataf1:
        data_a = dataf1.read()
    with open(f2,"r") as dataf2:
        data_b = dataf2.read()
    with open(f1,"w") as dataf1:
        dataf1.write(data_b)
    with open(f2,"w") as dataf2:
        dataf2.write(data_a)
swappingfile()