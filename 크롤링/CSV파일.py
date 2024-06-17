import csv
f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "박재훈", "클래식피지크", True])
wr.writerow([2, "크리스범스테드", "클래식피지크", False])
f.close()