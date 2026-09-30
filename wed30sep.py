name = input("Name ? ")
age = int(input("Age ?"))
programmingLanguage = input("Favourite programming language")
hours_studied = int(input("Hours Studied ?"))

age_next_year = age + 1
study_time_minutes = hours_studied * 60

study_time_greater = hours_studied > 1
print("Student Profile")
print("-----------------")
print("Name: %s" % name)
print("Age: {0}".format(age))
print("Age next year: %d" % age_next_year)
print(
    "Study time: {0} hours \nStudy time in minutes: {1}".format(
        hours_studied, study_time_minutes
    )
)
print("Studied for more than 1 hour: %s" % study_time_greater)
print("Favourite language: " + programmingLanguage)
