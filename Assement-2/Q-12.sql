SELECT facid, SUM(slots) FROM cd.bookings
GROUP BY facid 
HAVING SUM(slots) >= 1000
ORDER BY facid