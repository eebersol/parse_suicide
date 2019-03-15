finallist = [] # variable global permettant de stocker la liste final

def rmv_b(country): # Permet de supprimer le b' qui ce met souvent en general avant le nom du pays, ceci a un rapport avec le type de la variables qui serait un byte ?
    return country.replace("b'", "")

def print_result_per_year(): # Print le resultat de la premiere merge
    newf = open("result_per_years.txt", "w")

    newf.write("country, population, suicide_nbr, year\n")
    for line in finallist:
        newf.write(str(line['country']) + ',' + \
                        str(line['population']) + ',' + \
                            str(line['suicide_nbr']) + ',' + \
                                str(line['year']) + '\n')

def print_result_per_country(country, fd): # Merge les differentes annees pour un meme pays, en une seule ligne
    population  = 0
    suicides    = 0
    years       = 0

    for elem in finallist:
        if country == elem['country'] and elem['population'] > 0:
            population  = elem['population']
            suicides    += elem['suicide_nbr']
            years       += 1
    if years > 0:
        percent_average_suicide = float(((100 * suicides)/(population))/years)
        percent_average_suicide = '%.4f'%(percent_average_suicide)
        fd.write(country + ',' + str(percent_average_suicide) + ',' + str(suicides/years) + '\n')
    
def get_average_per_year(dataset, country, year): # Merge les differentes data pour un meme pays et une meme date
    suicide     = 0
    population  = 0

    for line in dataset:
        line = str(line).split(",")
        # Si c'est le bon pays et la bonne anée alors tu concats les informations
        if country == rmv_b(line[0]) and year == int(line[1]):
            suicide     += int(line[4])
            population  += int(line[5])        
    
    finallist.append({
        'country'       : country,
        'year'          : year,
        'suicide_nbr'   : suicide,
        'population'    : population
    })
    
    if year + 1 == 2017:
        return 
    else:
        get_average_per_year(dataset, country, year + 1)

def get_country(dataset): # Recupère la liste de pays
    countryList = []
    country     = 0
    
    for line in dataset:
        line = str(line).split(",")
        if country and line[0] != country:
            countryList.append(country)
        country = line[0]
    return countryList
 
with open('master.csv','rb') as f:
    dataset         = list(f)
    # Recupere la liste des pays
    countries       = get_country(dataset)
    lencountries    = len(countries)
    i               = 0

    # Merge les lignes ayant le meme pays et la meme annee
    for country in countries:
        country = rmv_b(country)
        print(country, str(i) + "/" + str(lencountries))
        get_average_per_year(dataset, country, 1985)
        i += 1

    # Print le resultat de la merge
    print_result_per_year()

    # Merge les differentes annees pour un meme pays, en une seule ligne
    fd = open("result_per_country.txt", "w")    
    fd.write("country, percent_average, suicide_average\n")
    for country in countries:
        print_result_per_country(rmv_b(country), fd)





