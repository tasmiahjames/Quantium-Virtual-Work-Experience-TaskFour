import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./data.csv"

#open output file
with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)

    #add the three fields
    header = ["sales", "date", "region"]
    writer.writerow(header)

    #loop through all files
    for file_name in os.listdir(DATA_DIRECTORY):
        #read cvs file
        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            #loop through each role in cvs file
            row_index = 0
            for input_row in reader:
                if row_index > 0:
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    transaction_date = input_row[3]
                    region = input_row[4]

                    #identify and process pink morsel transactions
                    if product == "pink morsel":
                        # finish formatting data
                        price = float(raw_price[1:])
                        sale = price * int(quantity)

                        #write
                        output_row = [sale, transaction_date, region]
                        writer.writerow(output_row)
                row_index += 1
