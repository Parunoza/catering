-- =====================
-- CATERING SYSTEM DB
-- =====================

-- Drop Tables if needed
DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS menu_items CASCADE;
DROP TABLE IF EXISTS tables CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- =====================
-- USERS (Admins, Kellner etc.)
-- =====================
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'waiter', 'kitchen', 'bar')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================
-- TABLES (Tische im Restaurant)
-- =====================
CREATE TABLE restaurant_tables (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================
-- MENU ITEMS (Speisen & Getränke)
-- =====================
CREATE TABLE menu_items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(20) NOT NULL CHECK (type IN ('food', 'drink')),
    price DECIMAL(6, 2) NOT NULL CHECK (price >= 0),
    available BOOLEAN DEFAULT TRUE
);

-- =====================
-- ORDERS (Bestellungen pro Tisch)
-- =====================
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    table_id INTEGER NOT NULL REFERENCES restaurant_tables(id) ON DELETE CASCADE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('open', 'in_progress', 'ready', 'delivered', 'cancelled')),
    created_by INTEGER NOT NULL REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================
-- ORDER ITEMS (Einzelne Produkte in einer Bestellung)
-- =====================
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    menu_item_id INTEGER NOT NULL REFERENCES menu_items(id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    note TEXT
);

select * from tisch;
select * from orders;
select * from order_items;
select * from menu_items;
select * from users;

drop table tisch