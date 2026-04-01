f = open("employees.txt");
data = f.readlines();
f.close()
print("".join(data));
print("Highest:", max(data, key=lambda x: int(x.split()[1])))
open("employees.txt","a").write(input("New employee: ")+"\n")
