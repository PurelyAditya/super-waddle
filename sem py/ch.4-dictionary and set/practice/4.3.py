marks={} #null dictionary

x=int(input("enter the marks of maths:\n"))

marks.update({"maths":x})

y=int(input("enter the marks of chem:\n"))

marks.update({"chem":y})


z=int(input("enter the marks of phy:\n"))

marks.update({"phy":z})


print(marks)