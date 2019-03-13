import csv

# 0     country,
# 1     year,
# 2     sex,
# 3     age,
# 4     suicides_no,
# 5     population,
# 6     suicides/100k pop,
# 7     country-year,
# 8     HDI for year,
# 9     gdp_for_year ($) ,
# 10    gdp_per_capita ($),
# 11    generation
finallist = []

def print_result_per_year():
    f = open("result_per_years.txt", "w")
    f.write("country, population, percent, suicide_nbr, year\n")
    for line in finallist:
        finalline = str(line['country']) + ',' + str(line['population']) + ',' + str(line['percent']) + ',' + str(line['suicide_nbr']) + ',' + str(line['year']) + '\n'
        f.write(finalline)
    
    print("Result per years OK")

def print_result_per_country(country, fd):
    i = 0
    percent_average = 0
    percent_bis = 0
    for elem in finallist:
        if country == elem['country'] and elem['population'] > 0:
            i += 1
            percent_average += (elem['population'] * elem["percent"])/100
    if i > 0:
        finalline = str(country) + ',' + str(percent_average/i) + '\n'
        f.write(finalline)
    
def get_average_per_year(dataset, country, year):
    percent = 0
    suicide = 0
    population = 0
    for line in dataset:
        line = str(line).split(",")
        if country == line[0] and year == int(line[1]):
            suicide += int(line[4])
            population += int(line[5])
    if population > 0:
        percent = (100 * int(suicide)) / float(population)
    obj = {
        'country':country,
        'year':year,
        'suicide_nbr':suicide,
        'percent':percent,
        'population':population
    }
    finallist.append(obj)
    year += 1
    if year == 2016:
        return
    else:
        get_average_per_year(dataset, country, year)

def get_country(dataset):
    country = "Albania"
    countryList = []
    for line in dataset:
        line = str(line).split(",")
        if line[0] != country:
            countryList.append(country)
        country = line[0]
    return countryList
 
with open('master.csv','rb') as f:
    mylist = list(f)
    countryList =  get_country(mylist)
    for country in countryList:
        print(country)
        get_average_per_year(mylist, country, 1985)
    f = open("result_per_country.txt", "w")
    f.write("country, percent_average\n")
    for country in countryList:
        print_result_per_country(country, f)
    print_result_per_year()





