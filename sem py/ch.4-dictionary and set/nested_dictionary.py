student={
    "name": "rahul",
    "surname":"kumar",
    "sub":{
        "phy":100,
        "chem":78,
        "gk":10,
        "cs":78,
    },
    
    "age":19,
}


print(student["name"])

print(student["sub"]["chem"])



print(list(student.keys()))
print(student.values())


print(len(student))

print(student.items())

print(student.get("surname"))


print(student.get("sub").get("phy"))




# for update
student.update({"city":"delhi"})
print(student)