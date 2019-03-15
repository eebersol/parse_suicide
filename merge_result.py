def rmv_b(country): # Permet de supprimer le b' qui ce met souvent en general avant le nom du pays, ceci a un rapport avec le type de la variables qui serait un byte ?
    return country.replace("b'", "")

def print_result():
    f = open("result_per_years.txt", "w")
    
    f.write("country, population, percent, suicide_nbr, year\n")
    for line in finallist:
        f.write(str(line['country']) + ',' +  str(line['population']) + ',' + str(line['percent']) + ',' + str(line['suicide_nbr']) + ',' + str(line['year']) + '\n')

def get_data(country, res_pib_country):

    for elem in res_pib_country:
        line = str(elem).split(",")
        line[0] = line[0].replace("b'", "")

        if line[0] == country:
            return line[33]
    return ""

def merge_data(): # on souhaite merge result_per_country et result_pid_country pour garder que les infornmations significatives
    finalist = []

    # On open les deux fichiers
    with open('result_per_country.txt','rb') as f:
        res_per_country = list(f)
        del res_per_country[0]
    with open('result_pib_country.txt','rb') as f:
        res_pib_country = list(f)
        del res_pib_country[0]
    
    # On créer et prépare l'entête du nouveau fichier
    f = open("result_final.txt", "w")
    f.write("country,average_suicide,average_pib\n")

    # On parcours le fichier result_per_country
    for elem in res_per_country:
        line    = str(elem).split(",")
        line[0] = rmv_b(line[0])
        # On recupere dans le fichier result_pib_country, le pays passeé en param
        data    = get_data(line[0], res_pib_country)
        # Si un pays est trouvé on exploit la data
        if len(data) > 1:
            f.write(line[0] + ',' + line[1] + '%,' + data[:(len(data)-3)] + '\n')

    
merge_data()