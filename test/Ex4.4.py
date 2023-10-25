months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

job = []
for x in range(12):
    job.append(x+1)

pair = dict(zip(months,job))
date = input("")
char = date[0]

while(True):
    if char.isdigit() == True:
        print("why")
        month,day,year = date.split("/")
        break
    elif char.isalpha() == True:
        month,day,year = date.split(" ")
        day = day.strip(",")
        day = int(day)
        if month in pair:
            month = pair[month]
            break
    else:
        continue

print(f"{year}", f"{month:02}", f"{day:02}", sep="-")
print(year, end="-")
print(f"{month:02}",end="-")
print(f"{day:02}")








# s = 1
# for month in months:
#     month[month] = s
#     s += 1
#     print(months[month],month)
