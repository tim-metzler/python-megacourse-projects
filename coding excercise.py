with open("members.txt", "r") as f:
    members = f.readlines()
name = input("Enter a name to add to the members list")
members.append(name)

with open("members.txt", "w") as f:
    f.writelines(members)