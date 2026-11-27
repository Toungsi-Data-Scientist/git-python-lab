import csv


file_path = r"C:\Users\TOUNGSI JIJG\Downloads\Unit04\datasets\rectangles_data.csv"

with open(file_path, "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        width = float(row["width"])

        length = float(row["length"])

        area = width * length

        print("Rectangle ID:", row["id"])

        print("Area:", round(area, 2))

        print("-------------------")