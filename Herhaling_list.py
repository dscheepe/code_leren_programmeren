studenten = ["Arne","Bert","Chris","Dennis","Erik"]
print(len(studenten))
studenten.append("Freddy")
studenten.insert(2,"Jef")
studenten.extend(["Karel"])
print(studenten)
studenten.remove("Karel")
studenten.pop(0)
print(studenten)
#studenten.sort(reverse=True)
student_z_a = sorted(studenten,reverse=True)
print(student_z_a)

