import csv

def transform(ReadName, StartRow, StartColumn, EndRow = -1, EndColumn = -1, SaveName = ""):
	if not isinstance(StartRow, int):
		raise Exception('StartRow must be an int!')
	if not isinstance(StartColumn, int):
		raise Exception('StartColumn must be an int!')
	if not isinstance(EndRow, int):
		raise Exception('EndRow must be an int!')
	if not isinstance(EndColumn, int):
		raise Exception('EndColumn must be an int!')
	if not isinstance(SaveName, str):
		raise Exception('SaveName must be a string!')

	if EndRow < StartRow:
		raise Exception('EndRow < StartRow!')
	if EndColumn < StartColumn:
		raise Exception('EndColumn < StartColumn!')

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
			if count < StartRow or (count > EndRow and EndRow != -1):
				Ret.append(row)
				continue
			Ret.append([])

			for j in range(len(row)):
				if j + 1 > EndColumn and EndColumn != -1:
					Ret.append(["" for i in range(StartColumn-1)])
					Ret[-1] += row[j:-1]
					break
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