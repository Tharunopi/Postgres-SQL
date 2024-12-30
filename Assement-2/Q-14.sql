SELECT starttime FROM cd.bookings AS book
WHERE book.memid = (SELECT memid FROM cd.members AS mem
WHERE firstname = 'David' AND surname = 'Farrell')