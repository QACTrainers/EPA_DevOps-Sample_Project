-- Records

CREATE TABLE if not exists records(
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(40),
    artist VARCHAR(40),
    genre CHAR(3),
    runtime INTEGER,
    total_stock INTEGER,
    cost FLOAT(2)
);

CREATE TABLE if not exists orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER,
    quantity INTEGER,
    total_cost FLOAT(2),
    date_time VARCHAR(30),
    FOREIGN KEY(item_id) REFERENCES records(record_id)
);

INSERT INTO records (title, artist, genre, runtime, total_stock, cost) VALUES ('Every Valley', 'Public Service Broadcasting', 'IND', 52, 150, 8.50);

INSERT INTO orders (item_id, quantity, total_cost, date_time) VALUES (1, 10, 17, '2023-02-07T12:37:53+0000')




-- Orders