#create a csv file of your own and do the write operation of file handling
import csv
f=open("write.csv","a",newline="")
a=csv.writer(f)
a.writerow(["student id","roll no","name","phone no"])
studentid=int(input("Enter student id:"))
rollno=int(input("Enter roll number:"))
name=input("Enter name:")
phoneno=int(input("Enter phone number:"))
a.writerow([studentid,rollno,name,phoneno])
print("student record has save")
f.close()
