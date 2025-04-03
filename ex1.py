import csv
from io import TextIOWrapper
from zipfile import ZipFile

# opens file.
enrollment_outfile = open("enrollment.csv", 'w' , encoding='UTF8')
enrollment_outwriter = csv.writer(enrollment_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)


# process_file goes over all rows in original csv file, and sends each row to process_row()
def process_file():
  with ZipFile('enrollment.zip') as zf:
      with zf.open('enrollment.csv', 'r') as infile:
          reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
          for row in reader:
              # TO DO splits row into the different csv table files
              enrollment_outwriter.writerow(row)
  enrollment_outfile.close()

# return the list of all tables
def get_names():
    return ["enrollment"]


if __name__ == "__main__":
    process_file()

