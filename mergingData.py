import csv

data1=[]
data2=[]

with open("final.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data1.append(row)

with open("dataset_sorted_1.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data2.append(row)

headers_1=data1[0]
planet_data_1=data1[1:]

headers_2=data2[0]
planet_data_2=data2[1:]

headers=headers_1+headers_2
planet_data=[]

for index,data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("merged_file.csv","a+") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)