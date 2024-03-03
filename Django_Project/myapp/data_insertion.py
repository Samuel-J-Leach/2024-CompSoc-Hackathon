from .models import *

Department.objects.raw("INSERT INTO Department VALUES (010,'Department of Computer Science'),(020,'Department of Electronics and Electrical Engineering');")

Course.objects.raw("INSERT INTO Course VALUES (100,'BSc Computer Science'),(101,'BSc Computer Information Technology'),(200,'MSc Data Science'),(201,'MSc Security'),(210,'MSc Electrical Engineering');")

Student.objects.raw("INSERT INTO Student VALUES (1234567,'Hallam','Saunders',100,'none'),(2345678,'Leon','Queen',100,'none'),(3456789,'Samuel','Leach',100,'none');")

Academic.objects.raw("INSERT INTO Academic VALUES (0987654,'Joe','Appleton',010,'none'),(9876543,'Joey','Lam',010,'none'),(8765432,'Brijesh','Dongol',010,'none'),(7654321,'John','Doe',020,'none'),(6543210,'Skibidi','Rizzler',020,'none');")

Module.objects.raw("INSERT INTO Module VALUES (1026,'software engineering'),(1027,'web and database systems'),(1028,'computer security'),(1030,'foundations of electronics'),(1031,'foundations of computing');")

Convener.objects.raw("INSERT INTO Convener VALUES (1029384,'John','Smith',1026),(2938475,'Jane','Doe',1027),(3847561,'Bob','Gunn',1028),(4756102,'Samantha','Lee',1030),(5610293,'Dave','Bourne',1031);")

ModuleCourse.objects.raw(" INSERT INTO Module_Course VALUES (1026,100),(1027,100),(1027,101),(1028,100),(1028,201),(1030,210),(1031,100),(1031,101),(1031,200),(1031,201)")

Assessment.objects.raw("INSERT INTO Assessment VALUES (10260,100,40,100,1026),(10270,100,40,100,1027),(10280,100,40,100,1028),(10300,100,40,100,1030),(10310,100,40,70,1031),(10311,100,40,30,1031);")