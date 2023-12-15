SELECT c.login AS "courierLogin",
       COUNT(o.id) AS "countDelivery"
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY c.login;