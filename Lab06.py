import datetime as dt
import csv

records = [
    { "name": "Joji", "Sports": "Football", "DOB": dt.datetime(2005, 9, 18), "Department": "CS", "gender": "male" },
    {"name": "Leki", "Sports": "Football", "DOB": dt.datetime(2006, 6, 12), "Department": "Business", "gender": "male" },
    {"name": "Kaustubh", "Sports": "Basketball", "DOB": dt.datetime(2006, 3, 15), "Department": "CS", "gender": "male" },
    {"name": "Mohit", "Sports": "Basketball", "DOB": dt.datetime(2005, 12, 1), "Department": "Maths", "gender": "male" },
    {"name": "Kaganya", "Sports": "Basketball", "DOB": dt.datetime(2006, 8, 25), "Department": "CS", "gender": "female" },
    {"name": "Keshav", "Sports": "Football", "DOB": dt.datetime(2005, 11, 30), "Department": "CS", "gender": "male" },
    {"name": "Akansha", "Sports": "Football", "DOB": dt.datetime(2006, 2, 20), "Department": "Business", "gender": "female"},
    {"name": "uddhav", "Sports": "Football", "DOB": dt.datetime(2004, 7, 10), "Department": "Commerce", "gender": "male"},
    {"name": "Tharik", "Sports": "Kabbadi", "DOB": dt.datetime(2002, 5, 5), "Department": "CS", "gender": "male"},
    {"name": "Chiranjeevi", "Sports": "Badminton", "DOB": dt.datetime(2003, 4, 15), "Department": "CS", "gender": "male"},
    {"name": "Jince", "Sports": "fooseball", "DOB": dt.datetime(2004, 9, 10), "Department": "Business", "gender": "male"},
    {"name": "Neha", "Sports": "Volleyball", "DOB": dt.datetime(2005, 1, 14), "Department": "Engineering", "gender": "female"},
    {"name": "Ravi", "Sports": "Cricket", "DOB": dt.datetime(2004, 4, 22), "Department": "Maths", "gender": "male"},
    {"name": "Sana", "Sports": "Badminton", "DOB": dt.datetime(2006, 5, 7), "Department": "Commerce", "gender": "female"},
    {"name": "Aarav", "Sports": "Volleyball", "DOB": dt.datetime(2003, 8, 12), "Department": "Business", "gender": "male"},
    {"name": "Priya", "Sports": "Cricket", "DOB": dt.datetime(2005, 10, 9), "Department": "Engineering", "gender": "female"},
    {"name": "Nikhil", "Sports": "Basketball", "DOB": dt.datetime(2004, 2, 16), "Department": "Commerce", "gender": "male"},
    {"name": "Mina", "Sports": "Football", "DOB": dt.datetime(2006, 7, 18), "Department": "Maths", "gender": "female"},
    {"name": "Harsh", "Sports": "Badminton", "DOB": dt.datetime(2004, 11, 28), "Department": "CS", "gender": "male"},
    {"name": "Anjali", "Sports": "Volleyball", "DOB": dt.datetime(2005, 6, 3), "Department": "Business", "gender": "female"},
    {"name": "Dev", "Sports": "Cricket", "DOB": dt.datetime(2003, 9, 20), "Department": "Engineering", "gender": "male"},
    {"name": "Riya", "Sports": "Basketball", "DOB": dt.datetime(2006, 12, 5), "Department": "Commerce", "gender": "female"},
    {"name": "Kunal", "Sports": "Football", "DOB": dt.datetime(2004, 3, 11), "Department": "CS", "gender": "male"},
    {"name": "Tara", "Sports": "Badminton", "DOB": dt.datetime(2005, 8, 17), "Department": "Maths", "gender": "female"},
    {"name": "Siddharth", "Sports": "Cricket", "DOB": dt.datetime(2003, 7, 2), "Department": "Engineering", "gender": "male"},
    {"name": "Meera", "Sports": "Basketball", "DOB": dt.datetime(2006, 1, 27), "Department": "Business", "gender": "female"},
    {"name": "Arjun", "Sports": "Volleyball", "DOB": dt.datetime(2004, 6, 15), "Department": "CS", "gender": "male"},
    {"name": "Pooja", "Sports": "Football", "DOB": dt.datetime(2005, 2, 24), "Department": "Commerce", "gender": "female"},
    {"name": "Vikram", "Sports": "Badminton", "DOB": dt.datetime(2003, 10, 13), "Department": "Maths", "gender": "male"},
    {"name": "Isha", "Sports": "Cricket", "DOB": dt.datetime(2006, 4, 8), "Department": "Business", "gender": "female"},
    {"name": "Rohan", "Sports": "Basketball", "DOB": dt.datetime(2004, 9, 30), "Department": "Engineering", "gender": "male"},
    {"name": "Shreya", "Sports": "Volleyball", "DOB": dt.datetime(2005, 11, 19), "Department": "CS", "gender": "female"},
    {"name": "Aditya", "Sports": "Football", "DOB": dt.datetime(2003, 12, 1), "Department": "Maths", "gender": "male"},
    {"name": "Divya", "Sports": "Badminton", "DOB": dt.datetime(2006, 3, 21), "Department": "Commerce", "gender": "female"},
    {"name": "Naman", "Sports": "Cricket", "DOB": dt.datetime(2004, 8, 6), "Department": "Business", "gender": "male"},
    {"name": "Kavya", "Sports": "Basketball", "DOB": dt.datetime(2005, 5, 16), "Department": "Engineering", "gender": "female"},
    {"name": "Yash", "Sports": "Volleyball", "DOB": dt.datetime(2003, 1, 25), "Department": "CS", "gender": "male"},
    {"name": "Asha", "Sports": "Football", "DOB": dt.datetime(2006, 6, 14), "Department": "Maths", "gender": "female"},
    {"name": "Rajat", "Sports": "Badminton", "DOB": dt.datetime(2004, 7, 9), "Department": "Business", "gender": "male"},
    {"name": "Nidhi", "Sports": "Cricket", "DOB": dt.datetime(2005, 4, 4), "Department": "Commerce", "gender": "female"},
    {"name": "Sourav", "Sports": "Basketball", "DOB": dt.datetime(2003, 2, 20), "Department": "Engineering", "gender": "male"},
    {"name": "Tanvi", "Sports": "Volleyball", "DOB": dt.datetime(2006, 9, 11), "Department": "CS", "gender": "female"},
    {"name": "Aman", "Sports": "Football", "DOB": dt.datetime(2004, 10, 2), "Department": "Business", "gender": "male"},
    {"name": "Kritika", "Sports": "Badminton", "DOB": dt.datetime(2005, 12, 14), "Department": "Maths", "gender": "female"},
    {"name": "Bhavya", "Sports": "Cricket", "DOB": dt.datetime(2003, 5, 18), "Department": "Commerce", "gender": "female"},
    {"name": "Manav", "Sports": "Basketball", "DOB": dt.datetime(2004, 1, 7), "Department": "Engineering", "gender": "male"},
    {"name": "Sneha", "Sports": "Volleyball", "DOB": dt.datetime(2006, 8, 23), "Department": "CS", "gender": "female"},
    {"name": "Abhi", "Sports": "Football", "DOB": dt.datetime(2003, 3, 9), "Department": "Maths", "gender": "male"},
    {"name": "Mansi", "Sports": "Badminton", "DOB": dt.datetime(2005, 7, 11), "Department": "Business", "gender": "female"},
]

fieldnames = ["name", "Sports", "DOB", "Department", "gender"]

with open("records.csv", "w", newline="") as csvfile:
    write= csv.DictWriter(csvfile, fieldnames=fieldnames)
    write.writeheader()
    write.writerows(records)

print("CSV file 'records.csv' has been created successfully.")