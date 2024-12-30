SELECT name, membercost FROM cd.facilities
WHERE membercost > 0 AND membercost < (monthlymaintenance * 0.02)