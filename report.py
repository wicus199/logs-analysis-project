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

# Fetch the result of the first query
articles = c.fetchall()

c.execute("select authors.name, sum(articleSum.artViews) as authViews "
          "from articleSum, articles, authors "
          "where articleSum.title = articles.title and articles.author = authors.id "
          "group by authors.name order by authViews desc")

authors = c.fetchall()

# Close the database
db.close()

print("1. What are the three most popular articles of all time?\n")
# for statement to print the results of the query in a structured format
for row in articles:
    print('\t"{}" - {} views'.format(row[0], row[1]))

print("\n2. Who are the most popular article authors of all time?\n")
# for statement to print the results of each author's views
for row in authors:
    print('\t"{}" - {} views'.format(row[0], row[1]))
