CREATE TABLE IF NOT EXISTS suppliers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    group_name VARCHAR(50),
    currency VARCHAR(20),
    supplier_folder VARCHAR(50)
);