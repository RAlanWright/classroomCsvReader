import csv

# Python with open will auto-close after finished executing
with open('2-13-19-grades.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    reader = list(reader) # Need to convert to a list to index / slice it
    # writer = csv.writer(csvfile) # To be used to generate a separate csv file; not currently implemented

    # Create a dict of header name -> column number
    headers = {col.strip(): n for n, col in enumerate(reader[0])}
    # Print("headers: ", headers) # Used to display the headers and their index.
    # Copy these "headers" into headers_i_want below from your first run. Issue copying the emoji from excel into the editor...

    # For headers_i_want, copy the output from the above print() for the data you want to display
    headers_i_want = ['🐹 Chapter 3 Assignment (7931)', '🐹 Chapter 4 Assignment (7932)', '🐹 Chapter 5 Assignment (7933)', '🐹 Chapter 6 Assignment (7934)']
    for row in reader[1:]: # Skip the first row because it's the header
        if (row[3] == "Alan and LC101 Memphis Winter 2019"): # Grab students from your section; Change this for your section
            for h in headers_i_want:
                print(row[0])
                print(h, "    ", row[headers[h]], end='')
                print()
            print("-" * 40) # Separate each student
            print()

