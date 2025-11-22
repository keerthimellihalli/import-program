import sys
    #check if correct number of argv
if len(sys.argv) != 3:
print("Usage: python student.py <name><rollno>")
    #sys.argv[0] is always the program name
script_name = sys.argv[0]
rollno = sys.argv[2]

print("script name:",script_name)
print("student name:",name)
print("rollno number:",rollno)
