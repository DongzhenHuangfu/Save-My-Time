import csv

def transform(ReadName, StartRow, StartColumn, SaveName = ""):
	if SaveName == "":
		SaveName = ReadName + "_transform.csv"
	else:
		SaveName += ".csv"

	with open(ReadName + ".csv", "rt", encoding="utf-8") as ReadFile:
		CSVFile = csv.reader(ReadFile)
		count = 0
		Ret = []

		for row in CSVFile:
			count += 1
			if count < StartRow:
				Ret.append(row)
				continue
			Ret.append([])

			for j in range(len(row)):
				if j + 1 <= StartColumn:
					Ret[-1].append(row[j])
				else:
					if row[j] == "":
						continue
					else:
						Ret.append(["" for i in range(StartColumn-1)])
						Ret[-1].append(row[j])
	with open(SaveName, "wt", encoding="utf-8", newline="") as SaveFile:
		CSVWriter = csv.writer(SaveFile)
		for row in Ret:
			CSVWriter.writerow(row)