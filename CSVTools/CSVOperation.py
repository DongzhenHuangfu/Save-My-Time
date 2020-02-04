import csv

class CSVOperator:
	def __init__(self, FileName):
		CSVFile = open(FileName + ".csv", "rt", encoding="utf-8")
		self.CSVFile = csv.reader(CSVFile)
		self.FileName = FileName

	def Transform(self, StartColumn, StartRow, SaveFile = True, OutName=""):
		if OutName == "":
			OutName = self.FileName + "_transform.csv"
		self.CSVTransform = []
		count = 0
		for row in self.CSVFile:
			count += 1
			if count < StartColumn:
				self.CSVTransform.append(row)
				continue
			self.CSVTransform.append([])
			for j in range(len(row)):
				if j + 1 <= StartRow:
					self.CSVTransform[-1].append(row[j])
				else:
					if row[j] == "":
						continue
					else:
						self.CSVTransform.append(["" for i in range(StartRow - 1)])
						self.CSVTransform[-1].append(row[j])
		if SaveFile:
			with open(OutName, "wt", encoding="utf-8", newline="") as FileTansform:
				CSVWriter = csv.writer(FileTansform)
				for row in self.CSVTransform:
					CSVWriter.writerow(row)