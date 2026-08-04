CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists musique(
        id integer primary key autoincrement,
        composer_artist text,
            title text
                    );
create table if not exists country(
        id integer primary key autoincrement,
        name text
                    );
create table if not exists cutlery(
        id integer primary key autoincrement,
        name text,
            country_id text
                    );
create table if not exists places(
        id integer primary key autoincrement,
        name text
                    );
create table if not exists station(
        id integer primary key autoincrement,
        place_id text,
            name text
                    );
create table if not exists traveler(
        id integer primary key autoincrement,
        station_id text,
            user_id text,
            is_dissident text,
            age_group text
                    );
create table if not exists social_media_account(
        id integer primary key autoincrement,
        traveler_id text,
            platform_name text,
            follower_count text
                    );
create table if not exists pop_culture_quote(
        id integer primary key autoincrement,
        content text,
            quote_type text
                    );
create table if not exists news_video(
        id integer primary key autoincrement,
        link text
                    );
create table if not exists ai_news_video(
        id integer primary key autoincrement,
        news_video_id text,
            link text,
            anomaly_type text
                    );
create table if not exists musician_pic(
        id integer primary key autoincrement,
        pic text,
            title text
                    );
create table if not exists traveling_ticket(
        id integer primary key autoincrement,
        date_depart text,
            date_arrivee text,
            aeroport_ville_code_postal text
                    );
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            phone text,
            country_id text,
            email text,
            password text
                    );
create table if not exists childhood_meal(
        id integer primary key autoincrement,
        cutlery_id text,
            child_age text,
            innocence_level text,
            emotion_description text,
            user_id text
                    );
create table if not exists adult_cruelty_meal(
        id integer primary key autoincrement,
        cutlery_id text,
            cruelty_level text,
            perception_of_food text,
            user_id text
                    );
