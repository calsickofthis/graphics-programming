SELECT product.pid, product.productdesc, store.sid, store.location, product_store.Price
FROM product
INNER JOIN store
ON store.sid=product.pid

SELECT product.pid, product.productdesc, store.sid, store.location, product_store.Price
FROM product
LEFT JOIN store.sid
ON product_store.sid = store.sid

SELECT product.pid, product.productdesc, store.sid, store.location, product_store.Price
FROM product p
INNER JOIN product_store pds
 ON p.pid = pds.sid
INNER JOIN store s
 ON pds.cid = s.sid;



SELECT p.pid, p.productdesc, s.sid, s.location
FROM product p
INNER JOIN product_store sct
 ON s.sid = sct.sid
INNER JOIN store s
 ON sct.pid = c.sid;

 
 SELECT p.pid, p.productdesc, s.sid, s.location FROM product p INNER JOIN product_store sct ON p.pid = sct.sid INNER JOIN store s ON sct.sid = s.sid;