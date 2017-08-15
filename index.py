import sqlite3 as lite
import sys

sourcedb = raw_input("Please enter the name of the source database file (e.g. example.db) > ")
sqlquery = raw_input("Please enter a SELECT query to select/format the rows you'd like to have in the text file > ")
dest = raw_input("Please enter the destination file to write to (e.g. ~/Documents/example.txt) > ")
fields = raw_input("Please enter the full path to the file with the field lengths seperated by commas > ")
print "\n"
if ("drop" in sqlquery.lower()) or ("select" not in sqlquery.lower()):
	print "select queries only"
	sys.exit(1)
try:
	con = lite.connect(sourcedb)
	cur = con.cursor()    
	cur.execute(sqlquery)
	with open(fields, 'r') as f:
		fields = f.read().strip().split(',')
	with open(dest, 'a') as f:
		for x in cur.fetchall():
			for i, c in enumerate(x):
				if (i % (len(fields) + 1) == 0) and not (i == 0):
					f.write("\n")
				f.write(c + ' ' * (int(fields[i % len(fields)]) - len(c)))
	with open(dest, 'r') as f:
		print f.read()
except lite.Error, e:
	print "Error %s:" % e.args[0]
	sys.exit(1)