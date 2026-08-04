from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_musique", methods=["GET","POST"])
def add_one_musique():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musique (composer_artist,title) values (:composer_artist,:title)",hey)
        user = query_db('select * from musique')

        return render_template("musiqueform.html", musiques=user, one_user=one_user, the_title="add new musique")


    user = query_db('select * from musique')
    one_user = query_db("select * from musique limit 1", one=True)
    return render_template("musiqueform.html", musiques=user, one_user=one_user, the_title="add new musique")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_cutlery", methods=["GET","POST"])
def add_one_cutlery():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into cutlery (name,country_id) values (:name,:country_id)",hey)
        user = query_db('select * from cutlery')

        return render_template("cutleryform.html", cutlerys=user, one_user=one_user, the_title="add new cutlery", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from cutlery')
    one_user = query_db("select * from cutlery limit 1", one=True)
    return render_template("cutleryform.html", cutlerys=user, one_user=one_user, the_title="add new cutlery", touslescountry=touslescountry)

@app.route("/add_one_places", methods=["GET","POST"])
def add_one_places():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into places (name) values (:name)",hey)
        user = query_db('select * from places')

        return render_template("placesform.html", placess=user, one_user=one_user, the_title="add new places")


    user = query_db('select * from places')
    one_user = query_db("select * from places limit 1", one=True)
    return render_template("placesform.html", placess=user, one_user=one_user, the_title="add new places")

@app.route("/add_one_station", methods=["GET","POST"])
def add_one_station():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesplace= query_db("select * from place")

        one_user = query_db("insert into station (place_id,name) values (:place_id,:name)",hey)
        user = query_db('select * from station')

        return render_template("stationform.html", stations=user, one_user=one_user, the_title="add new station", touslesplace=touslesplace)


    touslesplace= query_db("select * from place")

    user = query_db('select * from station')
    one_user = query_db("select * from station limit 1", one=True)
    return render_template("stationform.html", stations=user, one_user=one_user, the_title="add new station", touslesplace=touslesplace)

@app.route("/add_one_traveler", methods=["GET","POST"])
def add_one_traveler():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesstation= query_db("select * from station")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into traveler (station_id,user_id,is_dissident,age_group) values (:station_id,:user_id,:is_dissident,:age_group)",hey)
        user = query_db('select * from traveler')

        return render_template("travelerform.html", travelers=user, one_user=one_user, the_title="add new traveler", touslesstation=touslesstation, touslesuser=touslesuser)


    touslesstation= query_db("select * from station")

    touslesuser= query_db("select * from user")

    user = query_db('select * from traveler')
    one_user = query_db("select * from traveler limit 1", one=True)
    return render_template("travelerform.html", travelers=user, one_user=one_user, the_title="add new traveler", touslesstation=touslesstation, touslesuser=touslesuser)

@app.route("/add_one_social_media_account", methods=["GET","POST"])
def add_one_social_media_account():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslestraveler= query_db("select * from traveler")

        one_user = query_db("insert into social_media_account (traveler_id,platform_name,follower_count) values (:traveler_id,:platform_name,:follower_count)",hey)
        user = query_db('select * from social_media_account')

        return render_template("social_media_accountform.html", social_media_accounts=user, one_user=one_user, the_title="add new social_media_account", touslestraveler=touslestraveler)


    touslestraveler= query_db("select * from traveler")

    user = query_db('select * from social_media_account')
    one_user = query_db("select * from social_media_account limit 1", one=True)
    return render_template("social_media_accountform.html", social_media_accounts=user, one_user=one_user, the_title="add new social_media_account", touslestraveler=touslestraveler)

@app.route("/add_one_pop_culture_quote", methods=["GET","POST"])
def add_one_pop_culture_quote():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into pop_culture_quote (content,quote_type) values (:content,:quote_type)",hey)
        user = query_db('select * from pop_culture_quote')

        return render_template("pop_culture_quoteform.html", pop_culture_quotes=user, one_user=one_user, the_title="add new pop_culture_quote")


    user = query_db('select * from pop_culture_quote')
    one_user = query_db("select * from pop_culture_quote limit 1", one=True)
    return render_template("pop_culture_quoteform.html", pop_culture_quotes=user, one_user=one_user, the_title="add new pop_culture_quote")

@app.route("/add_one_news_video", methods=["GET","POST"])
def add_one_news_video():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into news_video (link) values (:link)",hey)
        user = query_db('select * from news_video')

        return render_template("news_videoform.html", news_videos=user, one_user=one_user, the_title="add new news_video")


    user = query_db('select * from news_video')
    one_user = query_db("select * from news_video limit 1", one=True)
    return render_template("news_videoform.html", news_videos=user, one_user=one_user, the_title="add new news_video")

@app.route("/add_one_ai_news_video", methods=["GET","POST"])
def add_one_ai_news_video():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesnews_video= query_db("select * from news_video")

        one_user = query_db("insert into ai_news_video (news_video_id,link,anomaly_type) values (:news_video_id,:link,:anomaly_type)",hey)
        user = query_db('select * from ai_news_video')

        return render_template("ai_news_videoform.html", ai_news_videos=user, one_user=one_user, the_title="add new ai_news_video", touslesnews_video=touslesnews_video)


    touslesnews_video= query_db("select * from news_video")

    user = query_db('select * from ai_news_video')
    one_user = query_db("select * from ai_news_video limit 1", one=True)
    return render_template("ai_news_videoform.html", ai_news_videos=user, one_user=one_user, the_title="add new ai_news_video", touslesnews_video=touslesnews_video)

@app.route("/add_one_musician_pic", methods=["GET","POST"])
def add_one_musician_pic():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        one_user = query_db("insert into musician_pic (pic,title) values (:pic,:title)",hey)
        user = query_db('select * from musician_pic')

        return render_template("musician_picform.html", musician_pics=user, one_user=one_user, the_title="add new musician_pic")


    user = query_db('select * from musician_pic')
    one_user = query_db("select * from musician_pic limit 1", one=True)
    return render_template("musician_picform.html", musician_pics=user, one_user=one_user, the_title="add new musician_pic")

@app.route("/add_one_traveling_ticket", methods=["GET","POST"])
def add_one_traveling_ticket():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into traveling_ticket (date_depart,date_arrivee,aeroport_ville_code_postal) values (:date_depart,:date_arrivee,:aeroport_ville_code_postal)",hey)
        user = query_db('select * from traveling_ticket')

        return render_template("traveling_ticketform.html", traveling_tickets=user, one_user=one_user, the_title="add new traveling_ticket")


    user = query_db('select * from traveling_ticket')
    one_user = query_db("select * from traveling_ticket limit 1", one=True)
    return render_template("traveling_ticketform.html", traveling_tickets=user, one_user=one_user, the_title="add new traveling_ticket")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,phone,country_id,email,password) values (:username,:phone,:country_id,:email,:password)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','phone','country_id','email','password']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','phone','country_id','email','password']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','phone','country_id','email','password']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_childhood_meal", methods=["GET","POST"])
def add_one_childhood_meal():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescutlery= query_db("select * from cutlery")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into childhood_meal (cutlery_id,child_age,innocence_level,emotion_description,user_id) values (:cutlery_id,:child_age,:innocence_level,:emotion_description,:user_id)",hey)
        user = query_db('select * from childhood_meal')

        return render_template("childhood_mealform.html", childhood_meals=user, one_user=one_user, the_title="add new childhood_meal", touslescutlery=touslescutlery, touslesuser=touslesuser)


    touslescutlery= query_db("select * from cutlery")

    touslesuser= query_db("select * from user")

    user = query_db('select * from childhood_meal')
    one_user = query_db("select * from childhood_meal limit 1", one=True)
    return render_template("childhood_mealform.html", childhood_meals=user, one_user=one_user, the_title="add new childhood_meal", touslescutlery=touslescutlery, touslesuser=touslesuser)

@app.route("/add_one_adult_cruelty_meal", methods=["GET","POST"])
def add_one_adult_cruelty_meal():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescutlery= query_db("select * from cutlery")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into adult_cruelty_meal (cutlery_id,cruelty_level,perception_of_food,user_id) values (:cutlery_id,:cruelty_level,:perception_of_food,:user_id)",hey)
        user = query_db('select * from adult_cruelty_meal')

        return render_template("adult_cruelty_mealform.html", adult_cruelty_meals=user, one_user=one_user, the_title="add new adult_cruelty_meal", touslescutlery=touslescutlery, touslesuser=touslesuser)


    touslescutlery= query_db("select * from cutlery")

    touslesuser= query_db("select * from user")

    user = query_db('select * from adult_cruelty_meal')
    one_user = query_db("select * from adult_cruelty_meal limit 1", one=True)
    return render_template("adult_cruelty_mealform.html", adult_cruelty_meals=user, one_user=one_user, the_title="add new adult_cruelty_meal", touslescutlery=touslescutlery, touslesuser=touslesuser)

