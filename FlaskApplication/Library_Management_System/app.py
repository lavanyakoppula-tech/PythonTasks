from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

# =====================================================
# FLASK APP
# =====================================================

app = Flask(__name__)

app.secret_key = "library_secret"

# =====================================================
# MYSQL CONNECTION
# =====================================================

app.config["SQLALCHEMY_DATABASE_URI"] = \
    "mysql+pymysql://root:root@localhost:3306/LibManagSys_db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =====================================================
# STUDENTS TABLE
# =====================================================

class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    student_name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    department = db.Column(
        db.String(100),
        nullable=False
    )

# =====================================================
# LIBRARIANS TABLE
# =====================================================

class Librarian(db.Model):

    __tablename__ = "librarians"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    librarian_name = db.Column(
        db.String(100),
        nullable=False
    )

    librarian_id = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    shift_time = db.Column(
        db.String(50),
        nullable=False
    )

    availability = db.Column(
        db.Boolean,
        default=True
    )

# =====================================================
# BOOKS TABLE
# =====================================================

class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    author = db.Column(
        db.String(100),
        nullable=False
    )

    isbn = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    available = db.Column(
        db.Boolean,
        default=True
    )

# =====================================================
# ISSUED BOOK TABLE
# =====================================================

class IssuedBook(db.Model):

    __tablename__ = "issued_books"

    issue_id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id")
    )

    librarian_id = db.Column(
        db.Integer,
        db.ForeignKey("librarians.id")
    )

    book_id = db.Column(
        db.Integer,
        db.ForeignKey("books.id")
    )

    issued_date = db.Column(
        db.Date,
        nullable=False
    )

    return_deadline = db.Column(
        db.Date,
        nullable=False
    )

    days_allowed = db.Column(
        db.Integer,
        default=7
    )

    fine_amount = db.Column(
        db.Integer,
        default=0
    )

    returned = db.Column(
        db.Boolean,
        default=False
    )

# =====================================================
# CREATE TABLES
# =====================================================

with app.app_context():

    db.create_all()

# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():

    return render_template("index.html")

# =====================================================
# STUDENTS CRUD
# =====================================================

@app.route("/students", methods=["GET", "POST"])
def students():

    if request.method == "POST":

        try:

            student = Student(

                student_name=request.form.get(
                    "student_name"
                ),

                email=request.form.get(
                    "email"
                ),

                department=request.form.get(
                    "department"
                )
            )

            db.session.add(student)

            db.session.commit()

            flash("Student Added Successfully")

        except Exception as e:

            db.session.rollback()

            flash(f"Error: {str(e)}")

        return redirect("/students")

    students = Student.query.all()

    return render_template(
        "students.html",
        students=students
    )

@app.route("/update-student/<int:id>",
methods=["GET", "POST"])
def update_student(id):

    student = Student.query.get(id)

    if request.method == "POST":

        student.student_name = request.form.get(
            "student_name"
        )

        student.email = request.form.get(
            "email"
        )

        student.department = request.form.get(
            "department"
        )

        db.session.commit()

        flash("Student Updated Successfully")

        return redirect("/students")

    return render_template(
        "update_student.html",
        student=student
    )

@app.route("/delete-student/<int:id>")
def delete_student(id):

    student = Student.query.get(id)

    db.session.delete(student)

    db.session.commit()

    flash("Student Deleted Successfully")

    return redirect("/students")

# =====================================================
# LIBRARIANS CRUD
# =====================================================

@app.route("/librarians", methods=["GET", "POST"])
def librarians():

    if request.method == "POST":

        librarian = Librarian(

            librarian_name=request.form.get(
                "librarian_name"
            ),

            librarian_id=request.form.get(
                "librarian_id"
            ),

            shift_time=request.form.get(
                "shift_time"
            ),

            availability=True
        )

        db.session.add(librarian)

        db.session.commit()

        flash("Librarian Added Successfully")

        return redirect("/librarians")

    librarians = Librarian.query.all()

    return render_template(
        "librarians.html",
        librarians=librarians
    )

@app.route("/update-librarian/<int:id>",
methods=["GET", "POST"])
def update_librarian(id):

    librarian = Librarian.query.get(id)

    if request.method == "POST":

        librarian.librarian_name = request.form.get(
            "librarian_name"
        )

        librarian.librarian_id = request.form.get(
            "librarian_id"
        )

        librarian.shift_time = request.form.get(
            "shift_time"
        )

        db.session.commit()

        flash("Librarian Updated Successfully")

        return redirect("/librarians")

    return render_template(
        "update_librarian.html",
        librarian=librarian
    )

@app.route("/delete-librarian/<int:id>")
def delete_librarian(id):

    librarian = Librarian.query.get(id)

    db.session.delete(librarian)

    db.session.commit()

    flash("Librarian Deleted Successfully")

    return redirect("/librarians")

# =====================================================
# BOOKS CRUD
# =====================================================

@app.route("/books", methods=["GET", "POST"])
def books():

    if request.method == "POST":

        book = Book(

            title=request.form.get("title"),

            author=request.form.get("author"),

            isbn=request.form.get("isbn"),

            category=request.form.get("category"),

            available=True
        )

        db.session.add(book)

        db.session.commit()

        flash("Book Added Successfully")

        return redirect("/books")

    books = Book.query.all()

    return render_template(
        "books.html",
        books=books
    )

@app.route("/update-book/<int:id>",
methods=["GET", "POST"])
def update_book(id):

    book = Book.query.get(id)

    if request.method == "POST":

        book.title = request.form.get("title")

        book.author = request.form.get("author")

        book.isbn = request.form.get("isbn")

        book.category = request.form.get(
            "category"
        )

        db.session.commit()

        flash("Book Updated Successfully")

        return redirect("/books")

    return render_template(
        "update_book.html",
        book=book
    )

@app.route("/delete-book/<int:id>")
def delete_book(id):

    book = Book.query.get(id)

    db.session.delete(book)

    db.session.commit()

    flash("Book Deleted Successfully")

    return redirect("/books")

# =====================================================
# ISSUE BOOK
# =====================================================

@app.route("/issue-book", methods=["GET", "POST"])
def issue_book():

    students = Student.query.all()

    librarians = Librarian.query.all()

    books = Book.query.filter_by(
        available=True
    ).all()

    if request.method == "POST":

        student_id = request.form.get(
            "student_id"
        )

        librarian_id = request.form.get(
            "librarian_id"
        )

        book_id = request.form.get(
            "book_id"
        )

        days = int(
            request.form.get("days")
        )

        fine_amount = 0

        if days > 15:

            fine_amount = (
                days - 15
            ) * 10

        book = Book.query.get(book_id)

        book.available = False

        issue = IssuedBook(

            student_id=student_id,

            librarian_id=librarian_id,

            book_id=book_id,

            issued_date=datetime.today().date(),

            return_deadline=(
                datetime.today().date() +
                timedelta(days=days)
            ),

            days_allowed=days,

            fine_amount=fine_amount,

            returned=False
        )

        db.session.add(issue)

        db.session.commit()

        flash("Book Issued Successfully")

        return redirect("/issued-books")

    return render_template(
        "issue_book.html",
        students=students,
        librarians=librarians,
        books=books
    )

# =====================================================
# ISSUED BOOKS
# =====================================================

@app.route("/issued-books")
def issued_books():

    issued_books = IssuedBook.query.all()

    return render_template(
        "issued_books.html",
        issued_books=issued_books
    )

# =====================================================
# RETURN BOOK
# =====================================================

@app.route("/return-book/<int:id>")
def return_book(id):

    issue = IssuedBook.query.get(id)

    issue.returned = True

    book = Book.query.get(issue.book_id)

    book.available = True

    db.session.commit()

    flash("Book Returned Successfully")

    return redirect("/issued-books")

# =====================================================
# LOGS
# =====================================================

@app.route("/logs")
def logs():

    logs = IssuedBook.query.all()

    return render_template(
        "logs.html",
        logs=logs
    )

# =====================================================
# RUN APP
# =====================================================

if __name__ == "__main__":

    app.run(debug=True)