f = open("marks.txt");
data = f.readlines();
f.close()
marks = [int(i.split()[1])
         for i in data
         if len(i.split())==2 and i.split()[1].isdigit()]
print("Avg:", sum(marks)/len(marks) if marks else "No valid data")
