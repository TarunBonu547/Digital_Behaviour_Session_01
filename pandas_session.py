import pandas as pd

df = pd.read_csv('digital_behaviour_session_01/digital_behaviour.csv')

print(f"The description :\n{df["Instagram_Minutes"].describe()}")

print(f"The first five rows are :\n {df.head(5)}\n") #First five rows

print(f"The last five rows are :\n {df.tail(5)}\n")#Last five rows

print(f"The shape of the DataFrame is : {df.shape}\n") #No fo rows and columns

print(f"The column names are \n: {df.columns}\n") #All column names

print(f"The instagram minutes are :\n{df["Instagram_Minutes"]}")

val = ["Instagram_Minutes","Date"]

print(f"The Instagram minutes and its corresponding dates are :\n{df[val]}")

# jhg = ["Instagram_Minutes","Study_Minutes","Date"]

# print(df[jhg])

print(f"The Sum of Instagram minutes: {df["Instagram_Minutes"].sum()}\n") #Sum

avg = df["Instagram_Minutes"].mean()

print(f"The avg of the Instagram minutes are : {df["Instagram_Minutes"].mean()}\n") #Mean

print(f"Rounding Mean of Instagram minutes to three decimals : {round(df["Instagram_Minutes"].mean(),3)}\n") #Rounding to three decimals

print(f"Maximum of Instagram minutes : {df["Instagram_Minutes"].max()}\n") #Maximum

print(f"Minimum of Instagram Minutes : {df["Instagram_Minutes"].min()}\n") #Minimum

val = df[df["Instagram_Minutes"] > 100] #Filtering

print(f"Rows where Instagram minutes are greater than 100 :\n {val}\n")

val2 = df[df["Study_Minutes"] > 180]

print(f"Rows where Study minutes are greater than 180 :\n {val2}\n")

print(f"Days where Instagram Minutes are greater than study minutes :\n{df[df["Instagram_Minutes"] > df["Study_Minutes"]]}\n")

print(f"Heavy Instagram Days are :\n{df[df["Instagram_Minutes"] > avg]}\n")

#Sorting

df2 = df.sort_values(by="Instagram_Minutes",ascending=False)

print(f"Sorting the Instagram Values by Highest to Lowest according to Instagram Minutes :\n {df2}\n")

# print(df2.head(5))

# print(df.sort_values("Study_Minutes",ascending=False).head(5))

#Creating new knowledge (calculated columns)

df["Total_Minutes"] = df["Instagram_Minutes"] + df["YouTube_Minutes"] + df["WhatsApp_Minutes"] + df["LinkedIn_Minutes"]

print(f"The total minutes column :\n {df["Total_Minutes"]}\n")

df["Screen_Hours"] = df["Total_Minutes"]/60

print(f"The Screen Hours column :\n {df["Screen_Hours"]}\n")

df["Digital_Balance"] = df["Study_Minutes"]/df["Total_Minutes"]

print(f"The digital balance column :\n {df["Digital_Balance"]}\n")

#classification

df["Day_Type"] = "Normal"

df.loc[df["Total_Minutes"] > 300,"Day_Type"] = "Heavy"

print(f"Classified Day Type according to Total Minutes :\n {df}\n")

# # Part - J

total_app = {
    "Instagram" : df["Instagram_Minutes"].sum(),
    "YouTube" : df["YouTube_Minutes"].sum(),
    "WhatsApp" : df["WhatsApp_Minutes"].sum(),
    "LinkedIn" : df["LinkedIn_Minutes"].sum()
}

# list = df[["Instagram_Minutes","YouTube_Minutes","WhatsApp_Minutes","LinkedIn_Minutes"]].sum()

# print(list)

print(f"The app with max screen time : {max(total_app, key= total_app.get)}\n")

print(f"Average of Digital Balance : {df["Digital_Balance"].mean()}\n")

print(f"Maximum of Study  Minutes : {df["Study_Minutes"].max()}\n")


print(f"The number of columns where DayType is Heavy : {(df["Day_Type"] == "Heavy").sum()}\n")

stu = df.loc[df["Total_Minutes"].idxmax(),"Study_Minutes"]

print(f"The study minutes on heaviest screen day : {stu}\n")

print("Converting the edited file to CSV.......!!!")

df.to_csv("New_digital_behaviour.csv")