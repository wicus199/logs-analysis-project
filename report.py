#!/usr/bin/python3

import psycopg2
import time

DBNAME = "news"

# Connect to the database
db = psycopg2.connect(database=DBNAME)
# Activate the cursor
c = db.cursor()
# Execute the query for the first question
c.execute("select articles.title, count(*) as artCount "
          "from articles, log where articles.slug = substring(log.path, 10) "
          "group by articles.title order by artCount desc limit 3")

# Fetch the result of the first query and store in articles
articles = c.fetchall()

c.execute("select authors.name, sum(articleSum.artViews) as authViews "
          "from articleSum, articles, authors "
          "where articleSum.title = articles.title "
          "and articles.author = authors.id "
          "group by authors.name order by authViews desc")

# Fetch the result of the second query and store in authors
authors = c.fetchall()

# Execute the query for the third question
c.execute("select "
          "all_requests.time,(error_requests.num_errors*100)::numeric"
          "/all_requests.num_requests as percent_error "
          "from error_requests, all_requests "
          "where error_requests.time = all_requests.time "
          "and (error_requests.num_errors*100)::numeric"
          "/all_requests.num_requests > 1 "
          "order by all_requests.time")

# Fetch the result for the third query and store in errors
errors = c.fetchall()

# Close the news database
db.close()

print("1. What are the three most popular articles of all time?\n")
# for statement to print results of top three articles in a structured format
for row in articles:
    print('\t"{}" - {} views'.format(row[0], row[1]))

print("\n2. Who are the most popular article authors of all time?\n")
# for statement to print the results of each author's total views
for row in authors:
    print('\t"{}" - {} views'.format(row[0], row[1]))

print("\n3. On which days did more than 1% of requests lead to errors?\n")
# for statement to print the days on which
# more than 1% of requests resulted in an error
for row in errors:
    print("\t{} {} {} - {:.2f}% errors".format(row[0].strftime("%d"),
                                               row[0].strftime("%B"),
                                               row[0].strftime("%Y"),
                                               row[1]))
