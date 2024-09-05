

students_result ={
    "Harry":85,
    "Ron":71,
    "Hermiona":98,
    "Draco":69,
}
stupnice={
    91:"Excelentní",
    81:"Vynikající",
    71:"Splněno",
    0:"Nesplněno"   
}

def klasifikace (students_result, stupnice):
    for i in students_result:
        for a in stupnice:
            if students_result[i]>=a:
                students_result[i]=stupnice[a]
                break
klasifikace(students_result, stupnice)
# for i in students_result:
#     for a in stupnice:
#         if students_result[i]>=a:
#             students_result[i]=stupnice[a]
#             break
print (students_result)

#Stupnice
# 91-100 = "Excelcentní"
# 81-90 = "Vynikající"
# 71-80 = "Splněno71 = "Nesplněno"

# for key in students_result:
#     print(students_result[key])
#     if int(students_result[key])>91 and int(students_result[key])<=100:
#         students_result[key]="Excelentní"
#     elif int(students_result[key])>81 and int(students_result[key])<=90:
#         students_result[key]="Vynikající"
#     elif int(students_result[key])>71 and int(students_result[key])<=80:
#         students_result[key]="Splněno"
#     else:
#         students_result[key]="Nesplněno"
  
        

# print (students_result)


    
# print(stupnice)
