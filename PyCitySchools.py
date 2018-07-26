# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

#COMPLETE

#Count the number of unique school names
unique_schools=data_complete.groupby("school_name")
Total_Schools=len(unique_schools)

#Count the number of rows; assumes each row represents a unique student
Total_Students=data_complete["school_name"].count()

#Sum budget column for each unique school - currently repeats for each student in a school (create a new data frame with just 1 row per school)
unique_budget=data_complete["budget"].unique()
Total_Budget=unique_budget.sum()

#average math_score
Avg_Math=data_complete["math_score"].mean()

#average reading
Avg_Reading=data_complete["reading_score"].mean()

#Count number >=70 on math, divide by Total_Students
i=0
for score in data_complete["math_score"]:
    if score>=70:
        i=i+1
Math_Pass=((i/Total_Students)*100)

#Count number >=70 on reading, divide by Total_Students
j=0
for score in data_complete["reading_score"]:
    if score>=70:
        j=j+1
Reading_Pass=((j/Total_Students)*100)

Overall_Pass=(Math_Pass+Reading_Pass)/2


d={"Total Schools":[Total_Schools],
    "Total Students":[Total_Students],
   "Total Budget":[Total_Budget],
   "Average Math":[Avg_Math],
   "Average Reading":[Avg_Reading],
   "Math Passing Rate":[Math_Pass],
   "Reading Passing Rate":[Reading_Pass],
   "Overall Passing Rate":[Overall_Pass]}

dist_summ=pd.DataFrame(data=d)

dist_summ["Total Students"] = dist_summ["Total Students"].map("{:,}".format)
dist_summ["Total Budget"] =dist_summ["Total Budget"].map("${:,.2f}".format)

#Show District Summary
print(dist_summ.head())

#Create a new df with only relevant columns, using data_complete as starting point - COMPLETE
school_df=data_complete[["school_name","type", "size","budget", "math_score", "reading_score"]]

#Add new columns to the new df: funding per student - COMPLETE
per_student=school_df["budget"]/school_df["size"]
school_df["Per Student Budget"]=per_student



#Add new columns to the new df: pass rate by school for math
math_pass_by_school=school_df.groupby("school_name")["math_score"].apply(lambda c: ((c>=70).sum()/len(c)*100))
math_pass_by_school=pd.DataFrame(data=math_pass_by_school)
school_df = pd.merge(school_df, math_pass_by_school, how="left", on=["school_name", "school_name"])

#Add new columns to the new df: pass rate by school for reading
reading_pass_by_school=school_df.groupby("school_name")["reading_score"].apply(lambda c: ((c>=70).sum()/len(c)*100))
reading_pass_by_school=pd.DataFrame(data=reading_pass_by_school)
school_df = pd.merge(school_df, reading_pass_by_school, how="left", on=["school_name", "school_name"])


#Add new columns to the new df: overall pass rate
overall_pass_by_school=(school_df["math_score_y"]+school_df["reading_score_y"])/2
overall_pass_by_school=pd.Series(overall_pass_by_school)

school_df["Overall Pass Rate"] = overall_pass_by_school.values

#Adjust the math score to be average for each school - COMPLETE
math_avg_by_school = school_df.groupby('school_name')['math_score_x'].mean()
math_avg_by_school=pd.DataFrame(data=math_avg_by_school)
school_df = pd.merge(school_df, math_avg_by_school, how="left", on=["school_name", "school_name"])

#Adjust the reading score to be average for each school - COMPLETE
read_avg_by_school = school_df.groupby('school_name')['reading_score_x'].mean()
read_avg_by_school=pd.DataFrame(data=read_avg_by_school)
school_df = pd.merge(school_df, read_avg_by_school, how="left", on=["school_name", "school_name"])
school_df.head()

school_df = school_df.rename(columns={"school_name":"School Name",
                                      "type":"School Type",
                                      "budget":"Budget",
                                      "size":"Total Students",
                                      "math_score_y":"% Passing Math",
                                      "reading_score_y":"% Passing Reading",
                                      "math_score_y":"% Passing Math",
                                      "math_score_x_y":"Average Math Score",
                                      "reading_score_x_y":"Average Reading Score"})

#Remove raw score columns - COMPLETE
del school_df["math_score_x_x"]
del school_df["reading_score_x_x"]

#Save complete, non-formatted dataframe for later
comp_school_df=school_df

#Reformat students and budget columns
school_df["Total Students"] = school_df["Total Students"].map("{:,}".format)
school_df["Budget"] =school_df["Budget"].map("${:,.2f}".format)
school_df["Per Student Budget"] =school_df["Per Student Budget"].map("${:,.2f}".format)

#Remove duplicate rows
school_unique_df=school_df.drop_duplicates()
school_unique_df=school_unique_df.set_index("School Name")
print(school_unique_df)

## School Summary


## Top Performing Schools (By Passing Rate)

#Top 5 schools
top_schools_df = school_unique_df.sort_values("Overall Pass Rate", ascending=False)
print(top_schools_df.head(5))

## Bottom Performing Schools (By Passing Rate)

#Bottom 5 schools
bottom_schools_df = school_unique_df.sort_values("Overall Pass Rate")
print(bottom_schools_df.head(5))



## Math Scores by Grade

grade_9=data_complete.loc[data_complete["grade"]=="9th"]
grade_9_math=grade_9[["school_name","math_score"]]
grade_9_math=grade_9_math.groupby("school_name").mean()
grade_9_math.reset_index(level=0, inplace=True)
grade_9_math = grade_9_math.rename(columns={"school_name":"School Name",
                                      "math_score":"9th Grade Avg Math Score"})

grade_10=data_complete.loc[data_complete["grade"]=="10th"]
grade_10_math=grade_10[["school_name","math_score"]]
grade_10_math=grade_10_math.groupby("school_name").mean()
grade_10_math.reset_index(level=0, inplace=True)
grade_10_math = grade_10_math.rename(columns={"school_name":"School Name",
                                              "math_score":"10th Grade Avg Math Score"})

grade_11=data_complete.loc[data_complete["grade"]=="11th"]
grade_11_math=grade_11[["school_name","math_score"]]
grade_11_math=grade_11_math.groupby("school_name").mean()
grade_11_math.reset_index(level=0, inplace=True)
grade_11_math = grade_11_math.rename(columns={"school_name":"School Name",
                                      "math_score":"11th Grade Avg Math Score"})

grade_12=data_complete.loc[data_complete["grade"]=="12th"]
grade_12_math=grade_12[["school_name","math_score"]]
grade_12_math=grade_12_math.groupby("school_name")
grade_12_math=grade_12_math.mean()
grade_12_math.reset_index(level=0, inplace=True)
grade_12_math = grade_12_math.rename(columns={"school_name":"School Name",
                                      "math_score":"12th Grade Avg Math Score"})

grade_12_math

math_summ = pd.merge(grade_11_math,grade_12_math, how="left", on=["School Name","School Name"])
math_summ = pd.merge(grade_10_math,math_summ, how="left", on=["School Name","School Name"])
math_summ = pd.merge(grade_9_math,math_summ, how="left", on=["School Name","School Name"])
print(math_summ)

## Reading Score by Grade 

grade_9=data_complete.loc[data_complete["grade"]=="9th"]
grade_9_reading=grade_9[["school_name","reading_score"]]
grade_9_reading=grade_9_reading.groupby("school_name").mean()
grade_9_reading.reset_index(level=0, inplace=True)
grade_9_reading = grade_9_reading.rename(columns={"school_name":"School Name",
                                      "reading_score":"9th Grade Avg Reading Score"})

grade_10=data_complete.loc[data_complete["grade"]=="10th"]
grade_10_reading=grade_10[["school_name","reading_score"]]
grade_10_reading=grade_10_reading.groupby("school_name").mean()
grade_10_reading.reset_index(level=0, inplace=True)
grade_10_reading = grade_10_reading.rename(columns={"school_name":"School Name",
                                              "reading_score":"10th Grade Avg Reading Score"})

grade_11=data_complete.loc[data_complete["grade"]=="11th"]
grade_11_reading=grade_11[["school_name","reading_score"]]
grade_11_reading=grade_11_reading.groupby("school_name").mean()
grade_11_reading.reset_index(level=0, inplace=True)
grade_11_reading = grade_11_reading.rename(columns={"school_name":"School Name",
                                      "reading_score":"11th Grade Avg Reading Score"})

grade_12=data_complete.loc[data_complete["grade"]=="12th"]
grade_12_reading=grade_12[["school_name","reading_score"]]
grade_12_reading=grade_12_reading.groupby("school_name")
grade_12_reading=grade_12_reading.mean()
grade_12_reading.reset_index(level=0, inplace=True)
grade_12_reading = grade_12_reading.rename(columns={"school_name":"School Name",
                                      "reading_score":"12th Grade Avg Reading Score"})

grade_12_reading

reading_summ = pd.merge(grade_11_reading,grade_12_reading, how="left", on=["School Name","School Name"])
reading_summ = pd.merge(grade_10_reading,reading_summ, how="left", on=["School Name","School Name"])
reading_summ = pd.merge(grade_9_reading,reading_summ, how="left", on=["School Name","School Name"])
print(reading_summ)

## Scores by School Spending


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
spend_groups = ["<$585", "$585-615", "$615-645", "$645-675"]


# Slice the data and place it into bins
reading_pass_by_school=data_complete.groupby("school_name")["reading_score"].apply(lambda c: ((c>=70).sum()/len(c)*100))
reading_pass_by_school_df=pd.DataFrame(data=reading_pass_by_school)
data_complete = pd.merge(data_complete,reading_pass_by_school_df, how="left", on=["school_name","school_name"])
math_pass_by_school=data_complete.groupby("school_name")["math_score"].apply(lambda c: ((c>=70).sum()/len(c)*100))
math_pass_by_school_df=pd.DataFrame(data=math_pass_by_school)
data_complete = pd.merge(data_complete,math_pass_by_school_df, how="left", on=["school_name","school_name"])
per_student=data_complete["budget"]/data_complete["size"]
data_complete["Per Student Budget"]=per_student
data_complete["School Spend Range"] = pd.cut(data_complete["Per Student Budget"], spending_bins, labels=spend_groups)
overall_pass=data_complete["reading_score_y"]*.5+data_complete["math_score_y"]*.5
data_complete["Overall Pass"]=overall_pass
school_by_budget = data_complete.groupby("School Spend Range").mean()
school_by_budget = school_by_budget.rename(columns={"math_score_y":"% Passing Math",
                                      "reading_score_y":"% Passing Reading",
                                      "math_score_x":"Average Math Score",
                                      "reading_score_x":"Average Reading Score"})


del school_by_budget["size"]
del school_by_budget["School ID"]
del school_by_budget["budget"]
del school_by_budget["Student ID"]
del school_by_budget["Per Student Budget"]


print(school_by_budget)

## Scores by School Size


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

data_complete["Size Range"] = pd.cut(data_complete["size"], size_bins, labels=group_names)
school_by_size = data_complete.groupby("Size Range").mean()
school_by_size = school_by_size.rename(columns={"math_score_y":"% Passing Math",
                                      "reading_score_y":"% Passing Reading",
                                      "math_score_x":"Average Math Score",
                                      "reading_score_x":"Average Reading Score"})

del school_by_size["size"]
del school_by_size["School ID"]
del school_by_size["budget"]
del school_by_size["Student ID"]
del school_by_size["Per Student Budget"]

print(school_by_size)

## Scores by School Type


school_by_type = comp_school_df.groupby('School Type').mean()
school_by_type
