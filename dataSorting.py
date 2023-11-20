import csv

data=[]
with open("archive_dataset.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data.append(row)

header=data[0]
planet_data=data[1:]

for data_point in planet_data:
    data_point[2]=data_point[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("archive_dataset_sorted1.csv","a+") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(planet_data)

with open("archive_dataset_sorted.csv") as input,open("dataset_sorted_1.csv","w",newline="") as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
            
            
