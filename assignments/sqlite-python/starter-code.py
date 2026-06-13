import sqlite3
from sqlite3 import Connection

DB_PATH = "students.db"


def create_connection(db_path: str) -> Connection:
    """Create and return a SQLite database connection."""
    return sqlite3.connect(db_path)


def create_table(connection: Connection) -> None:
    """Create the students table if it does not exist."""
    with connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                grade INTEGER NOT NULL,
                email TEXT
            )
            """
        )


def insert_student(connection: Connection, name: str, grade: int, email: str) -> None:
    """Insert a new student record into the database."""
    with connection:
        connection.execute(
            "INSERT INTO students (name, grade, email) VALUES (?, ?, ?)",
            (name, grade, email),
        )


def get_all_students(connection: Connection) -> list[tuple]:
    """Return all student records."""
    cursor = connection.execute("SELECT id, name, grade, email FROM students")
    return cursor.fetchall()


def get_student_by_id(connection: Connection, student_id: int) -> tuple | None:
    """Return a student record by ID."""
    cursor = connection.execute(
        "SELECT id, name, grade, email FROM students WHERE id = ?", (student_id,)
    )
    return cursor.fetchone()


def update_student_grade(connection: Connection, student_id: int, new_grade: int) -> None:
    """Update the grade of a student record."""
    with connection:
        connection.execute(
            "UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id)
        )


def delete_student(connection: Connection, student_id: int) -> None:
    """Delete a student record from the database."""
    with connection:
        connection.execute("DELETE FROM students WHERE id = ?", (student_id,))


def print_students(students: list[tuple]) -> None:
    """Print a list of student records in a readable format."""
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}, Email: {student[3]}")


def main() -> None:
    connection = create_connection(DB_PATH)
    create_table(connection)

    insert_student(connection, "Aiden", 10, "aiden@example.com")
    insert_student(connection, "Mia", 11, "mia@example.com")
    insert_student(connection, "Noah", 12, "noah@example.com")

    print("All students:")
    print_students(get_all_students(connection))

    print("\nStudent with ID 1:")
    print(get_student_by_id(connection, 1))

    update_student_grade(connection, 1, 11)
    print("\nUpdated student with ID 1:")
    print(get_student_by_id(connection, 1))

    delete_student(connection, 2)
    print("\nStudents after deletion:")
    print_students(get_all_students(connection))


if __name__ == "__main__":
    main()
