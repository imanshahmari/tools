#CSV to txt convertor
import csv
csv_file = r"C:\Users\Arman\Downloads\Documents\utterances-2sp.csv"
txt_file = r"I:\New folder\New.txt"

with open(txt_file, "w",encoding="UTF-8") as my_output_file: #Look at the encoding in the csv file and put it here to do the conversion
    with open(csv_file, "r",encoding="UTF-8") as my_input_file:
        [ my_output_file.write(",".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
