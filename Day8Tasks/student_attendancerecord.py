name = input("Enter name: ")
open("attendance.txt", "a").write(name + "\n")
print(open("attendance.txt").read())


#f = open("attendance.txt", "a");
#f.write(input("Name: ") + "\n");
#f.close()
#f = open("attendance.txt");
#print(f.read());
#f.close()
