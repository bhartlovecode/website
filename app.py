from flask import Flask, render_template, request, session
from database_code.registrationtable import db_connect
from datetime import date
from functools import wraps

app = Flask(__name__)
app.secret_key = '@#$%sdf34587#$%asdfeFSv'


# This decorator allows us to check if user is logged in
def status(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return "You must log-in to access this page"

    return wrapper


# noinspection PyUnresolvedReferences
@app.route('/')
def home():
    return render_template("index.html",
                           pageName='Home',
                           description='This will act as the home page template for website',
                           title='Home')


# noinspection PyUnresolvedReferences
@app.route('/index')
def index():
    return render_template('index.html',
                           pageName='Home',
                           description='This is the home page for the website',
                           title='Home')


# noinspection PyUnresolvedReferences
@app.route('/awards', methods=['GET', 'POST'])
def awards():
    if request.method == 'POST':
        return render_template('awards.html',
                               pageName='Awards',
                               description='This is the awards page for the website',
                               title='Awards',
                               message="Thank you for Voting!")
    return render_template('awards.html',
                           pageName='Awards',
                           description='This is the awards page for the website',
                           title='Awards',
                           message="")


# noinspection PyUnresolvedReferences
@app.route('/meals')
def meals():
    return render_template('meals.html',
                           pageName='Meals',
                           description='This is the awards page for the website',
                           title='Meals')


# noinspection PyUnresolvedReferences
@app.route('/activities')
def activities():
    return render_template('activities.html',
                           pageName='Activities',
                           description='This page displays the activities',
                           title='Activities')


# noinspection PyUnresolvedReferences
@app.route('/keynote')
def keynote():
    return render_template('keynote.html',
                           pageName='Keynote',
                           description='This page displays the keynote speakers',
                           title='Keynote')


# noinspection PyUnresolvedReferences
@app.route('/workshopschedule')
def workshop():
    return render_template('workshopschedule.html',
                           pageName='Schedule',
                           description='This page displays the workshop schedule',
                           title='Schedule')


# noinspection PyUnresolvedReferences
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        valid = request.cookies.get('valid')
        if valid == 'true':
            conn = db_connect()
            cur = conn.cursor()
            cookie = request.cookies.get("123456")
            cookie_data = cookie.split(",")
            print(cookie_data)
            title = cookie_data[0].split(":")[1]
            today = date.today()
            firstName = cookie_data[1].split(":")[1]
            lastName = cookie_data[2].split(":")[1]
            addressOne = cookie_data[3].split(":")[1]
            addressTwo = cookie_data[4].split(":")[1]
            city = cookie_data[5].split(":")[1]
            state = cookie_data[6].split(":")[1]
            zipcode = cookie_data[7].split(":")[1]
            telephone = cookie_data[8].split(":")[1]
            email = cookie_data[9].split(":")[1]
            website = cookie_data[10][8::]
            position = cookie_data[11].split(":")[1]
            company = cookie_data[12].split(":")[1]
            mealPack = cookie_data[13].split(":")[1]
            billing_firstName = cookie_data[24].split(":")[1]
            billing_lastName = cookie_data[25].split(":")[1]
            visa = cookie_data[26].split(":")[1]
            mastercard = cookie_data[27].split(":")[1]
            card_number = cookie_data[29].split(":")[1]
            csv = cookie_data[30].split(":")[1]
            exp_year = cookie_data[31].split(":")[1]
            exp_month = cookie_data[32].split(":")[1]
            java_one = cookie_data[15].split(":")[1]
            java_two = cookie_data[16].split(":")[1]
            python_checkbox_one = cookie_data[18].split(":")[1]
            python_checkbox_two = cookie_data[19].split(":")[1]
            prolog_one = cookie_data[21].split(":")[1]
            prolog_two = cookie_data[22].split(":")[1]

            mealChoice = "mealpack" if mealPack else "dinnerday2"

            if visa:
                card_type = "V"
            elif mastercard:
                card_type = "MC"
            else:
                card_type = "AE"

            sessionOne = "WorkShop A" if java_one else "Workshop B" if java_two else "WorkShop C"
            sessionTwo = "WorkShop D" if python_checkbox_one else "Workshop E" if python_checkbox_two else "WorkShop F"
            sessionThree = "WorkShop G" if prolog_one else "Workshop H" if prolog_two else "WorkShop I"

            cur.execute("""INSERT OR IGNORE INTO registrants (date, title, first_name, last_name, address_one,
                address_two, city, state, zipcode, telephone, email, website, position, company, meals,
                 billing_firstname, billing_lastname, card_type, card_number, card_csv, exp_year, exp_month,
                 session_one, session_two, session_three)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",
                        [today, title,
                         firstName, lastName,
                         addressOne,
                         addressTwo, city, state,
                         zipcode, telephone, email,
                         website,
                         position, company, mealChoice,
                         billing_firstName, billing_lastName,
                         card_type, card_number,
                         csv, exp_year, exp_month,
                         sessionOne, sessionTwo,
                         sessionThree])
            conn.commit()
            cur.close()
            conn.close()

            return (render_template('thankyou.html',
                                    pageName='Thank you!',
                                    description='This page displays the thank you page',
                                    title='Thank You!',
                                    date=today,
                                    myTitle=title,
                                    firstName=firstName,
                                    lastName=lastName,
                                    addressOne=addressOne,
                                    addressTwo=addressTwo,
                                    city=city,
                                    state=state,
                                    zipCode=zipcode,
                                    telephone=telephone,
                                    email=email,
                                    website=website,
                                    position=position,
                                    company=company,
                                    mealChoice=mealChoice,
                                    billingFirstName=billing_firstName,
                                    billingLastName=billing_lastName,
                                    cardType=card_type,
                                    cardNumber=card_number,
                                    csv=csv,
                                    expYear=exp_year,
                                    expMonth=exp_month,
                                    sessionOne=sessionOne,
                                    sessionTwo=sessionTwo,
                                    sessionThree=sessionThree))
        else:
            return render_template('registration.html',
                                   pageName='Registration',
                                   description='This page displays the registration form',
                                   title='Registration')

    return render_template('registration.html',
                           pageName='Registration',
                           description='This page displays the registration form',
                           title='Registration')


# noinspection PyUnresolvedReferences
@app.route('/admin')
@status
def admin():
    return render_template('admin.html',
                           pageName='Admin',
                           description='This page acts as the admin page',
                           title='Admin')


@app.route('/nametags8')
def nametags8():
    return render_template('nametags8.html')


@app.route('/nametags10')
def nametags10():
    return render_template('nametags10.html')


@app.route('/lists', methods=['GET', 'POST'])
def lists():
    if request.method == "POST":
        listOfRegs, title = handleListOption(request.form['listOption'])
        return render_template("listDisplay.html",
                               pageName="ListDisplay",
                               description="Displays a list of registrants",
                               title="List Display",
                               listTitle=title,
                               registrantList=listOfRegs)
    return render_template('lists.html',
                           pageName="Lists",
                           description="This page allows user to show lists of users",
                           title="Lists")


@app.route('/listDisplay')
def listDisplay():
    return render_template('listDisplay.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        conn = db_connect()
        cur = conn.cursor()
        username = request.form['username']
        password = request.form['password']
        # Grabs all of the user name and passwords
        cur.execute("SELECT username, password FROM users")
        users = cur.fetchall()
        cur.close()
        conn.close()

        # Iterates through users and determines if there is a match
        for user in users:
            tempDict = dict(user)
            if tempDict.get("username").strip('"') == username and tempDict.get("password").strip('"') == password:
                session['logged_in'] = True
                return render_template('admin.html',
                                       pageName="Admin",
                                       description="This page acts as the admin page",
                                       title="Admin"
                                       )
    # Renders default template if it does not match a login credential
    return render_template('login.html',
                           pageName="Login",
                           description="This page acts as the login page",
                           title="Login"
                           )


if __name__ == '__main__':
    app.run()


# Takes in the user's selection for the lists page and handles grabbing sqlite data
def handleListOption(selection):
    conn = db_connect()
    cur = conn.cursor()
    listOfRegs = []
    if selection == "all":
        cur.execute("SELECT * FROM registrants")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "All Registrants"
    elif selection == "Workshop A":
        cur.execute("SELECT * FROM registrants WHERE session_one = 'Workshop A'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Taking Workshop A"
    elif selection == "Workshop B":
        cur.execute("SELECT * FROM registrants WHERE session_one = 'Workshop B'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Taking Workshop B"
    elif selection == "Workshop C":
        cur.execute("SELECT * FROM registrants WHERE session_one = 'Workshop C'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Taking Workshop C"
    elif selection == "Workshop D":
        cur.execute("SELECT * FROM registrants WHERE session_two = 'Workshop D'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Taking Workshop D"
    elif selection == "Workshop E":
        cur.execute("SELECT * FROM registrants WHERE session_two = 'Workshop E'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Taking Workshop E"
    elif selection == "Workshop F":
        cur.execute("SELECT * FROM registrants WHERE session_two = 'Workshop F'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Taking Workshop F"
    elif selection == "Workshop G":
        cur.execute("SELECT * FROM registrants WHERE session_three = 'Workshop G'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Taking Workshop G"
    elif selection == "Workshop H":
        cur.execute("SELECT * FROM registrants WHERE session_three = 'Workshop H'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Taking Workshop H"
    elif selection == "Workshop I":
        cur.execute("SELECT * FROM registrants WHERE session_three = 'Workshop I'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Taking Workshop I"
    elif selection == "mealpack":
        cur.execute("SELECT * FROM registrants WHERE meals = 'mealpack'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Ordering the Meal Pack"
    else:
        cur.execute("SELECT * FROM registrants WHERE meals = 'dinnerday2'")
        rows = cur.fetchall()
        for row in rows:
            listOfRegs.append(dict(row).get("first_name") + " " + dict(row).get("last_name"))
        title = "People Ordering Dinner Day Two"
    cur.close()
    conn.close()
    return listOfRegs, title
