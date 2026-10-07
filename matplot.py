import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('digital_behaviour_session_01/New_digital_behaviour.csv')

total_app = {
    "Instagram" : df["Instagram_Minutes"].sum(),
    "YouTube" : df["YouTube_Minutes"].sum(),
    "WhatsApp" : df["WhatsApp_Minutes"].sum(),
    "LinkedIn" : df["LinkedIn_Minutes"].sum()
}

#Draw a bar chart where each bar is a day and the height of the bar is the total screen time for that day.
plt.figure(figsize=(12,5))
plt.bar([f"D{i+1}" for i in range(len(df))],df["Total_Minutes"])
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.title("My Screen Time by Day")
plt.xticks(rotation=45)
plt.savefig("My_Screen_Time_by_Day.png",dpi=500)
plt.show()

plt.close()

#Calculate the total minutes for each of the four apps. Draw a bar chart comparing the four apps. Title it "Total Time by App".
plt.figure(figsize=(12,5))
plt.title("Total Time by App")
plt.bar(total_app.keys(),total_app.values())
plt.xlabel("Apps")
plt.ylabel("Minutes")
plt.savefig("Total_Time_by_App.png",dpi=500)
plt.show()

plt.close()

#Draw a chart with two lines: one for study minutes per day, one for total screen time per day. Add a legend so a reader knows which line is which.
plt.figure(figsize=(12,5))
plt.title("Comparision of InstaMinutes and Study Minutes")

plt.plot([f"D{i+1}" for i in range(len(df))],df["Total_Minutes"], marker="o",label="Total Minutes")
plt.plot([f"D{i+1}" for i in range(len(df))],df["Study_Minutes"],marker="o",label = "Study Minutes")
plt.xlabel("Days")
plt.ylabel("Minutes")
plt.xticks(rotation=45)
plt.legend()
plt.savefig("Comparision_of_InstaMinutes_and_Study_Minutes.png",dpi=500)
plt.show()

plt.close()

#Draw a pie chart showing what share of your total app time each app took.
plt.figure(figsize=(12,5))
plt.title("Share of the total apps")
plt.pie(total_app.values(),labels=total_app.keys(),autopct="%1.1f%%",startangle=90)
plt.savefig("Share_of_the_total_apps.png",dpi=500)
plt.show()

plt.close()