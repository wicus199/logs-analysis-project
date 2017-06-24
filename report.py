#!/usr/bin/python3

import psycopg2

DBNAME = "news"

# Connect to the database
db = psycopg2.connect(database=DBNAME)
# Activate the cursor
c = db.cursor()
# Execute the query for the first question
c.execute("select articles.title, count(*) as artCount "
          "from articles, log where articles.slug = substring(log.path, 10) "
          "group by articles.title order by artCount desc limit 3")

# Fetch the result of the query
articles = c.fetchall()
# Close the database
db.close()

print("1. What are the three most popular articles of all time?\n")
# For statement to print the results of the query in a structured format
for row in articles:
    print('\t"{}" - {} views'.format(row[0], row[1]))
