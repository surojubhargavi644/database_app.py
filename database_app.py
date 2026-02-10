import sqlite3

# 1. Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
print("Database connected successfully")

# 2. Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER
)
""")
conn.commit()
print("Table created successfully")

# 3. Insert user records (with error handling)
def insert_user(name, email, age):
    try:
        cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )
        conn.commit()
        print("User inserted successfully")
    except sqlite3.IntegrityError:
        print("Email already exists. User not added.")

# 4. Fetch all users
def fetch_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found")

# 5. Update user age
def update_user_age(email, new_age):
    cursor.execute(
        "UPDATE users SET age = ? WHERE email = ?",
        (new_age, email)
    )
    conn.commit()
    print("User updated successfully")

# 6. Delete user
def delete_user(email):
    cursor.execute(
        "DELETE FROM users WHERE email = ?",
        (email,)
    )
    conn.commit()
    print("User deleted successfully")

# ---------------- MAIN EXECUTION ----------------

# Insert users
insert_user("Ravi", "ravi@gmail.com", 23)
insert_user("Anita", "anita@gmail.com", 21)

# Fetch users
print("\nUser Records:")
fetch_users()

# Update user
update_user_age("ravi@gmail.com", 24)

# Fetch after update
print("\nUpdated User Records:")
fetch_users()

# Delete user
delete_user("anita@gmail.com")

# Fetch after delete
print("\nFinal User Records:")
fetch_users()

# 7. Close connection
conn.close()
print("\nDatabase connection closed")
