## Synopsis

This project is part of the Full Stack web developer nanodegree from Udacity. An 
internal reporting tool uses infromation from a newspaper site SQL database 
to discover what kid of articles the site's readers like. The database contains 
more than 1 million entries.

Three questions are answered in this project:
1. What are the three most popular articles of all time?
2. Who are the most popular authors of all time?
3. On what days did more than 1% of HTTP requests lead to errors?

## Motivation

The motivation behind this project is to build a solid foundation of SQL 
database skills. Interaction with a live database is done both from the command 
line and from Python code. Complex queries are built and refined and then used 
to draw business conclusions from data.

Building informative summaries from logs is a real task that is often used in 
engineering and business. This project provides practical experience in doing 
that. 

## Installation


## View creation

For the python script to execute without any errors, the user first needs to create views that are used in some of the queries. Creating views makes the code look cleaner and easier to understand. The following views were created:

1. The first created view's purpose is to count the number of views for each 
article in the database.
To create the view, enter the following into the database:
  * create view articleSum as select articles.title, count(*) as artViews 
from articles, log where articles.slug = substring(log.path, 10) 
group by articles.title order by artViews desc; 
2. The second created view's purpose is to calculate the number of HTTP requests 
that resulted in an error. To create the view, enter the following into the 
database:
  * create view error_requests as select log.time::timestamp::date, count(*) as num_errors 
from log where log.status != '200 OK' 
group by log.time::timestamp::date 
order by log.time::timestamp::date;
3. The third created view's purpose is to count all the requests that happened 
in a day, for every day. To create the view, enter the following into the 
terminal:
  * create view all_requests as select log.time::timestamp::date, count(*) as num_requests 
from log group by log.time::timestamp::date order by log.time::timestamp::date;

## Tests

## Contributors

## License 
