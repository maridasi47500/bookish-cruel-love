
mkdir templates 
python3 scaffold.py musique composer_artist title
python3 scaffold.py country name
python3 scaffold.py cutlery name country_id:references
python3 scaffold.py places name
python3 scaffold.py station place_id:references name
python3 scaffold.py traveler station_id:references user_id:references is_dissident age_group
python3 scaffold.py social_media_account traveler_id:references platform_name follower_count
python3 scaffold.py pop_culture_quote content quote_type
python3 scaffold.py news_video link
python3 scaffold.py ai_news_video news_video_id:references link anomaly_type
python3 scaffold.py musician_pic pic:file title
python3 scaffold.py traveling_ticket date_depart date_arrivee aeroport_ville_code_postal
python3 scaffold.py user username phone country_id:references email password
python3 scaffold.py childhood_meal cutlery_id:references child_age innocence_level emotion_description user_id:references
python3 scaffold.py adult_cruelty_meal cutlery_id:references cruelty_level perception_of_food user_id:references
