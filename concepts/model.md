User
----
user_id PK int
spotify_user_id string UNIQUE
display_name string INDEX
email string UNIQUE
spotify_uri string UNIQUE
created_date datetime
updated_date datetime

RefreshToken
----
id PK int
user_id int FK - User.user_id UNIQUE
# one user to one token
token string UNIQUE
created_date datetime
updated_date datetime

Tracks
----
track_id PK int
spotify_track_id string UNIQUE
user_id int INDEX FK >-< User.user_id
#many users to many tracks 
created_date datetime
updated_date datetime

Artists
----
artist_id PK int
spotify_artist_id string UNIQUE
user_id int INDEX FK >-< User.user_id
# many users to many tracks 
created_date datetime
updated_date datetime

Games
----
game_id PK int
game_hash string UNIQUE
# created with the stage data + owner_id + created_date
owner_id int INDEX FK - User.user_id
# one owner user_id to one game
stages int INDEX FK -< Stages.stage_id
# one game has many stages
scoreboard_id int INDEX FK - ScoreBoard.score_board_id
# one game has one scoreboard 

Stages
----
stage_id PK int
puzzle_type int
puzzle_details str
choice_id int FK -< Choices.choice_id
# one stage has many choices


Choices
----
choice_id PK int
asset_type int
spotify_asset_id str
# many assets will be a SPOTIFY_ARTIST_ID or SPOTIFY_TRACK_ID
correct bool
# correct or incorrect Binary Bit


ScoreBoard
----
# unique constraint between the player_id + game_id
# COMPOSITE KEY
score_board_id PK int
game_id PK int FK - Games.game_id
player_id PK int FK - User.user_id
score int