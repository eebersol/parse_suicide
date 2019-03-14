import csv




"Country Name",

"1975"
"1976"
"1977"
"1978"
"1979"
"1980"
"1981"
"1982"
"1983"
"1984"
"1985"
"1986"
"1987"
"1988"
"1989"
"1990"
"1991"
"1992"
"1993"
"1994"
"1995"
"1996"
"1997"
"1998"
"1999"
"2000"
"2001"
"2002"
"2003"
"2004"
"2005"
"2006"
"2007"
"2008"
"2009"
"2010"
"2011"
"2012"
"2013"
"2014"
"2015"
"2016"
"2017"
"average"


def print_csv(newlist):
    f = open("result_pib_country.txt", "w")
    f.write("country, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, average\n")
    for line in newlist:
        finalline = line['name'] + "," + line['1975'] + "," + line['1976'] + "," + line['1977'] + "," + line['1978'] + "," + line['1979'] + "," + line['1980'] + "," + line['1981'] + "," + line['1982'] + "," + line['1983'] + "," + line['1984'] + "," + line['1985'] + "," + line['1986'] + "," + line['1987'] + "," + line['1988'] + "," + line['1989'] + "," + line['1990'] + "," + line['1991'] + "," + line['1992'] + "," + line['1993'] + "," + line['1994'] + "," + line['1995'] + "," + line['1996'] + "," + line['1997'] + "," + line['1998'] + "," + line['1999'] + "," + line['2000'] + "," + line['2001'] + "," + line['2002'] + "," + line['2003'] + "," + line['2004'] + "," + line['2005'] + "," + line['2006'] + "," + line['2007'] + "," + line['2008'] + "," + line['2009'] + "," + line['2010'] + "," + line['2011'] + "," + line['2012'] + "," + line['2013'] + "," + line['2014'] + "," + line['2015'] + "," + line['2016'] + "," + str(line['average'])
        f.write(finalline + "\n")


def get_country():
    countryList = []
    country = "Albania"
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
    i = 0
    for data in line:
        data = data.replace('"', "")
        if i >= 19 and i <= 60 and data:
            if len(data) > 2:
                counter += 1
                average += float(data)
        i += 1
    return average/counter


def test(data, countryList):
    print(data in countryList)

def exploit_pib():
    countryList = get_country()
    newlist = []
    with open('pib.csv','rb') as f:
         piblist = list(f)
         for line in piblist:
            line = line.split(',')
            line[0] = line[0].replace('"', '')
            if line[0]in countryList:
                country_data = {
                    'name': line[0],
                    "1975": line[19],
                    "1976": line[20],
                    "1977": line[21],
                    "1978": line[22],
                    "1979": line[23],
                    "1980": line[24],
                    "1981": line[25],
                    "1982": line[26],
                    "1983": line[27],
                    "1984": line[28],
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
    print_csv(newlist)



exploit_pib()