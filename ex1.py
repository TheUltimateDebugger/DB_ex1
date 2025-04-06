import csv
from io import TextIOWrapper
from zipfile import ZipFile

name2writers = {}

# duplacate prevention
countries = {}
years = {}
universities = {}
gotin = {}
incomegroups = {}
regions = {}

name2data = {"Country": countries, "Year": years, "University": universities, "GotIn": gotin,
             "Income_Group": incomegroups, "Region" : regions}
writer2file = {}


def preprocessing(file_names):
    for file_name in file_names:
        temp = open(file_name + ".csv", 'w', encoding='UTF8')
        name2writers[file_name] = csv.writer(temp, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        writer2file[name2writers[file_name]] = temp

# process_file goes over all rows in original csv file, and sends each row to process_row()
def process_file():
    with ZipFile('enrollment.zip') as zf:
        with zf.open('enrollment.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            for row in reader:
                process_row(row)
                # TO DO splits row into the different csv table files
        for name in get_names():
            writer = name2writers[name]
            data = name2data[name]
            for entry in data.keys():
                writer.writerow(data[entry])
            writer2file[writer].close()


# return the list of all tables


def process_row(row):
    # print(row)
    country = row[0]
    country_code = row[1]
    region = row[2]
    incomegroup = row[3]

    countries[country_code] = [country, country_code, region, incomegroup]
    incomegroups[incomegroup] = [incomegroup]
    regions[region] = [region]
    iau_id1 = row[4]
    eng_name = row[5]
    orig_name = row[6]
    foundedyr = row[7]

    years[foundedyr] = [foundedyr]

    yrclosed = row[8]

    years[yrclosed] = [yrclosed]

    private01 = row[9]
    latitude = row[10]
    longitude = row[11]
    phd_granting = row[12]
    divisions = row[13]
    specialized = row[14]
    yrstudent5 = row[15]
    student5_est = row[16]

    gotin[iau_id1, yrstudent5] = [yrstudent5, iau_id1, student5_est]

    universities[iau_id1] = [iau_id1, eng_name, orig_name, private01, latitude, longitude, specialized, divisions,
                             phd_granting, country_code, foundedyr, yrclosed]


def get_names():
    tables = ["GotIn", "University", "Country", "Income_Group", "Region", "Year"]
    return tables

preprocessing(get_names())

if __name__ == "__main__":
    process_file()
