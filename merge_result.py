

def print_result():
    f = open("result_per_years.txt", "w")
    f.write("country, population, percent, suicide_nbr, year\n")
    for line in finallist:
        finalline = str(line['country']) + ',' + str(line['population']) + ',' + str(line['percent']) + ',' + str(line['suicide_nbr']) + ',' + str(line['year']) + '\n'
        f.write(finalline)
    
    print("Result per years OK")


def get_data(country, res_pib_country):

    for elem in res_pib_country:
        line = str(elem).split(",")
        line[0] = line[0].replace("b'", "")

        print(line[0], country)
        if line[0] == country:
            return line
    return ""

def merge_data():

    finalist = []
    with open('result_per_country.txt','rb') as f:
        res_per_country = list(f)
    with open('result_pib_country.txt','rb') as f:
        res_pib_country = list(f)

    # for elem in res_per_country:
    #     print(country)
    #     country = country.replace("b'", "")
    print(len(res_per_country), len(res_pib_country))
    f = open("result_final.txt", "w")
    f.write("country,average_suicide,average_pib\n")
    for elem in res_per_country:
        
        line = str(elem).split(",")
        line[0] = line[0].replace("b'", "")

        data = get_data(line[0], res_pib_country)
        if len(data) > 1:
            line[2] = line[2].replace("\n", "")
            f.write(line[0] + ',' + line[2] + ',' + data[33])

    
merge_data()