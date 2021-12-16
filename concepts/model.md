User
----
user_id PK int
spotify_user_id string INDEX
display_name string INDEX
email string INDEX
spotify_uri string
created_date datetime
updated_date datetime

RefreshToken
----
id PK int
user_id int INDEX # one user to one token
token string
created_date datetime
updated_date datetime

Tracks
----
track_id PK int
spotify_track_id string INDEX
user_id int INDEX #many users to many tracks 
created_date datetime
updated_date datetime

Artists
----
artist_id PK int
spotify_artist_id string INDEX
user_id int INDEX #many users to many tracks 
created_date datetime
updated_date datetime

Games
----
game_id PK int
game_hash string INDEX 
# created with the stage data
owner_id int INDEX 
# one owner user_id to one game
stage_id int INDEX 
# one game has many stages
scoreboard_id int INDEX 
# one game has one scoreboard 

Stages
----
stage_id PK int
puzzle_type int
puzzle_details str
choice_id int 
# one stage has many choices


Choices
----
choice_id PK int
asset_type int
asset_id str
# many assets will be a SPOTIFY_ARTIST_ID or SPOTIFY_TRACK_ID
correct bool
# correct or incorrect Binary Bit


ScoreBoard
----
# unique constraint between the player_id + game_id
score_board_id PK int
game_id int
player_id int
score int






Order
----
OrderID PK int
CustomerID int FK >- Customer.CustomerID
TotalAmount money
OrderStatusID int FK >- os.OrderStatusID

OrderLine as ol
----
OrderLineID PK int
OrderID int FK >- Order.OrderID
ProductID int FK >- p.ProductID
Quantity int

# Table documentation comment 1 (try the PDF/RTF export)
Product as p # Table documentation comment 2
----
ProductID PK int
# Field documentation comment 1
# Field documentation comment 2 
Name varchar(200) UNIQUE # Field documentation comment 3
Price money

OrderStatus as os
----
OrderStatusID PK int
Name UNIQUE string
