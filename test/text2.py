dict ={'wang':98,'li':90,'zhang':99}
with open(r"C:\Users\asus\Desktop\text.txt","w+") as myfile:
     for item in myfile:
         f.write(item+":"+str[dict[item]]+"\n");
newD = {};
with open(r'C:\Users\asus\Desktop\text.txt',"r+") as w:
    str = w.read();
    item = str.split("\n");
    for i in item:
        di = i.split(":");
        if len(di)>1:
            newD[di[0]] = di[1];
name = input("Please enter your name:");
print("The grade of you is"+newD[name]);