SELECT facid, SUM(slots) FROM cd.bookings
WHERE EXTRACT(MONTH FROM starttime) = 9 AND EXTRACT(YEAR FROM starttime) = 2012
GROUP BY facid
ORDER BY SUM(slots) ASC