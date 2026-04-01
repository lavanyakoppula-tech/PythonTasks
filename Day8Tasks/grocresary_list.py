items = input("Enter grocery items (comma separated): ").split(",")
f = open("grocery.txt", "w")
f.write("\n".join(items)); f.close()
