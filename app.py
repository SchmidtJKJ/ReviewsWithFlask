from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/addReview')
def newReview():
    return render_template('addReview.html')


@app.route('/saveReview', methods=['POST', 'GET'])
def addReview():
    if request.method == 'POST':
        try:
            uname = request.form['Username']
            movie = request.form['Movie']
            rating = request.form['Rating']
            rvw = request.form['Comment']
            img = request.form['Image']
            acting = request.form['Acting']
            story = request.form['Story']
            price = request.form['BoxOffice']

            with sql.connect("reviewData.db") as con:
                cur = con.cursor()
                dateTime=str(con.DATETIME('now', 'local'))
                cur.execute("INSERT INTO Reviews(Username, Movie, ReviewTime, Rating, Review) "
                            "VALUES (?,?,?,?,?), (uname, movie, dateTime, rating, rvw)")
                cur.execute("INSERT INTO Ratings(Movie, Acting, Story, BoxOffice, Overall)"
                            "VALUES(?,?,?,?,?,?) (movie, acting, img, story, price, rating)")
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("index.html", msg=msg)
            con.close()


@app.route('/getReview')
def showReview():
    con = sql.connect("reviewData.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT Username, Review, Overall FROM Reviews WHERE Restaurant = request.form['restaurant']")

    rows = cur.fetchall()
    return render_template("showReviews.html", rows=rows)


@app.route('/getReport')
def showReports():
    conn = sql.connect("reviewData.db")
    conn.row_factory = sql.Row

    cursor = conn.cursor()
    cursor.execute("SELECT Username, Review, Overall FROM Ratings WHERE Restaurant = request.form['restaurant']")

    rows = cursor.fetchall()
    return render_template("showReviews.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
