SELECT starttime, name FROM cd.facilities AS fac
INNER JOIN cd.bookings AS book
ON fac.facid = book.facid
WHERE (book.starttime BETWEEN '2012-09-21 00:00:00' AND '2012-09-21 24:00:00') AND fac.name LIKE 'Tennis%'
ORDER BY book.starttime