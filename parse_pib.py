def rmv_b(country): # Permet de supprimer le b' qui ce met souvent en general avant le nom du pays, ceci a un rapport avec le type de la variables qui serait un byte ?
    return country.replace("b'", "")

def print_csv(newlist):
    f = open("result_pib_country.txt", "w")

    f.write("country, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, average\n")
    for line in newlist:
        f.write(rmv_b(line['name']) + "," + \
                    line['1985'] + "," + line['1986'] + "," + line['1987'] + "," + line['1988'] + "," + line['1989'] + "," + line['1990'] + "," + \
                        line['1991'] + "," + line['1992'] + "," + line['1993'] + "," + line['1994'] + "," + line['1995'] + "," + line['1996'] + "," + \
                            line['1997'] + "," + line['1998'] + "," + line['1999'] + "," + line['2000'] + "," + line['2001'] + "," + line['2002'] + "," + \
                                line['2003'] + "," + line['2004'] + "," + line['2005'] + "," + line['2006'] + "," + line['2007'] + "," + line['2008'] + "," + \
                                    line['2009'] + "," + line['2010'] + "," + line['2011'] + "," + line['2012'] + "," + line['2013'] + "," + line['2014'] + "," + \
                                        line['2015'] + "," + line['2016'] + "," + str(line['average']) + '\n')

def get_country():
    countryList = []
    country     = 0

    with open('master.csv','rb') as f:
        dataset = list(f)
        for line in dataset:
            line = str(line).split(",")
            if line[0] != country:
                countryList.append(country)
            country = line[0]
    return countryList
 
def make_average(line):
    average = 0
    counter = 0
    i       = 0

    for data in line:
        data = data.replace('"', "")
        if i >= 29 and i <= 60 and data:
            if len(data) > 2:
                counter += 1
                average += float(data)
        i += 1
    return average/counter

def exploit_pib():
    # On recupere la liste de pays dont nous avons les informations a propos des suicides
    countryList = get_country()
    newlist     = []
    # On lit pib.csv
    with open('pib.csv','rb') as f:
         #On met les data dans une liste
         piblist = list(f)
         
         # On parcours la liste pour get les informations dont nous avons besoin
         for line in piblist:
            line    = str(line).split(',')
            line[0] = line[0].replace('"', '')

            if line[0] in countryList:
                country_data = {
                    'name': line[0],
                    "1985": line[29],
                    "1986": line[30],
                    "1987": line[31],
                    "1988": line[32],
                    "1989": line[33],
                    "1990": line[34],
                    "1991": line[35],
                    "1992": line[36],
                    "1993": line[37],
                    "1994": line[38],
                    "1995": line[39],
                    "1996": line[40],
                    "1997": line[41],
                    "1998": line[42],
                    "1999": line[43],
                    "2000": line[44],
                    "2001": line[45],
                    "2002": line[46],
                    "2003": line[47],
                    "2004": line[48],
                    "2005": line[49],
                    "2006": line[50],
                    "2007": line[51],
                    "2008": line[52],
                    "2009": line[53],
                    "2010": line[54],
                    "2011": line[55],
                    "2012": line[56],
                    "2013": line[57],
                    "2014": line[58],
                    "2015": line[59],
                    "2016": line[60],
                    "average": make_average(line)
                }
                newlist.append(country_data)
    # On display print le resultat
    print_csv(newlist)



exploit_pib()