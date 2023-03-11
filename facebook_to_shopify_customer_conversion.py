#!/usr/bin/python3

import csv,sys,argparse,os

def convert(input_file,output_file):
    shopify_csv_header = "First Name,Last Name,Email,Accepts Email Marketing,Company,Address1,Address2,City,Province,Province Code,Country,Country Code,Zip,Phone,Accepts SMS Marketing,Total Spent,Total Orders,Tags,Note,Tax Exempt"
    shopify_csv_header = shopify_csv_header.split(',')

    with open (output_file, "w", newline='') as csv_output_file:
        fieldnames = shopify_csv_header
        writer = csv.DictWriter(csv_output_file, fieldnames=fieldnames)
        writer.writeheader()

        with open(input_file) as csv_input_file:
            reader = csv.reader(csv_input_file)
            for row in reader:
                if row[0] == "Created":  #If the first element is "Created" the header was included so skip
                    continue
                print("pulling data from: \n" + " : ".join(row))
                print(row[1])
                name_row = row[1].split(" ")
                #Facebook puts first and last name in single field. Shopify has two fields.
                #Assume first part is first name and remaining parts are last name
                #to account for multiple names after first name
                first_name = name_row[0]
                last_name = ""
                for name in name_row[1:]:
                    last_name += name + " "
                last_name = last_name.rstrip()
                print("Adding: first name %s last name %s"%(first_name, last_name))
                writer.writerow({'First Name': first_name, 'Last Name': last_name, 'Email': row[2], 'Phone': row[3], 'Accepts Email Marketing':'yes'})

    csv_output_file.close()
    csv_input_file.close()

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input_file', type=str, help="Facebook csv file for input")
    parser.add_argument(dest='output_file', type=str, help="File for Shopify csv output")
    args = parser.parse_args()
    convert(args.input_file,args.output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
