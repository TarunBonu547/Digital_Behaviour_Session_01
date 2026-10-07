import pandas as pd
import numpy as np
import csv

insta_list = []
study_list = []

#Reading The CSV File
with open("digital_behaviour_session_01/digital_behaviour.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for all_apps in reader:
        insta_list.append(int(all_apps["Instagram_Minutes"]))
        study_list.append(int(all_apps["Study_Minutes"]))

#Slicing The array to fisrt 7 values
insta_list = insta_list[:7]
study_list = study_list[:7]


#Converting the arrays to numpy arrays
insta = np.array(insta_list)
study = np.array(study_list)

#Sum
total_insta = insta.sum()
total_study = study.sum()
print(f"The Sum of Insta Minutes : {total_insta} and Study Minutes : {total_study}")

#Mean
avg_insta = insta.mean()
avg_study = study.mean()
print(f"The Average of Insta Minutes : {avg_insta} and Study Minutes : {avg_study}")

#Max
max_insta = insta.max()
max_study = study.max()
print(f"The Maximum of Insta Minutes : {max_insta} and Study Minutes : {max_study}")

#Min
min_insta = insta.min()
min_study = study.min()
print(f"The Minimum of Insta Minutes : {min_insta} and Study Minutes : {min_study}")

#First and Last value
print(f"First Insta Value : {insta[0]}")

print(f"Last Insta Value : {insta[-1]}")

print(f"Third Insta Value : {insta[2]}")

print(f"Fisrt three days of Insta Values : {insta[0:3]}")

print(f"Last two days of Insta Values : {insta[-2::]}")

print(f"Two , Three , Four days : {insta[1:4]}")

hours = insta / 60
print(f"Instagram minutes to hours : {hours}")

diff = insta - study
print(f"Difference between Insta Min and Study Min : {diff}")

greater = insta > 100

print(greater)

above_avg = insta > avg_insta

only_true = insta[insta > 100]

count = greater.sum()

print(f"No of days above 100 mins : {count}")