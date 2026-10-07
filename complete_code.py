import csv
APP = "Instagram"
list = []

with open("digital_behaviour_session_01/digital_behaviour.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file) #Gives the data in dictionary format
    for all_apps in reader:
        list.append(int(all_apps["Instagram_Minutes"]))
print(f"The 7 days of Instgram Minutes : {list[0:7]}")

total = sum(list)

print(f"Sum of the minutes : {total}")

avg = total/len(list)

print(f"Average of minutes : {avg}")

print(f"Maximum value : {max(list)}")

print(f"Minimum value : {min(list)}")

count = 0
for row in list:
    if(row > avg):
        count+=1

print(f"Count of above average : {count}")

print(f"App name : {APP} , The 7 days of Instgram Minutes : {list[0:7]} , Sum of the minutes : {total} , Average of minutes : {avg} , Maximum value : {max(list)} , Minimum value : {min(list)} , Count of above average : {count}")