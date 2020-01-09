#Given a date, return the corresponding day of the week for that date.

#The input is given as three integers representing the day, month and year respectively.

#Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

class Solution:

    #first dat at 2019, severed as the anchor day
    def __init__(self):

        self.day = int(2)
        self.year = int(2019)

    def firstDayOfTheYear(self, year: int) -> int:

        if year == self.year:
            return 2

        elif year > self.year:
            currentYear = self.year
            currentDay = self.day
            while currentYear != year:
                if currentYear % 4 == 0:
                    days = 366
                else:
                    days = 365
                currentDay = (currentDay + days) % 7
                currentYear = currentYear + 1
            return currentDay

        elif year < self.year:
            currentYear = self.year
            currentDay = self.day
            while currentYear != year:
                currentYear = currentYear - 1
                if currentYear % 4 == 0:
                    days = 366
                else:
                    days = 365
                currentDay = (currentDay - days) % 7
            return currentDay

        else:
            return -1

    def firstDayOfTheMonth(self, year: int, firstDayOfTheYear: int, targetMonth: int):

        month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if year % 4 == 0:
            month[2] = 29
        else:
            month[2] = 28

        currentMonth = 1
        currentDay = firstDayOfTheYear

        while currentMonth != targetMonth:
            currentDay = (currentDay + month[currentMonth]) % 7
            currentMonth = currentMonth + 1

        return currentDay

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        #print("first day of the Year: " + str(self.firstDayOfTheYear(year)))
        firstDayOfTheMonth = self.firstDayOfTheMonth(year, self.firstDayOfTheYear(year), month)
        #print("First day of the month: " + str(firstDayOfTheMonth))
        return str(days[(firstDayOfTheMonth + day - 1) % 7])

solution = Solution()
print(solution.dayOfTheWeek(29, 2, 2016))
