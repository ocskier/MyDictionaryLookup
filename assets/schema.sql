CREATE DATABASE video_games_db;
USE video_games_db;
CREATE TABLE games(
	id INT NOT NULL AUTO_INCREMENT,
	Name TEXT NOT NULL,
	Genre TEXT NOT NULL,
	ESRB_Rating TEXT,
	Platform TEXT NOT NULL,
	Publisher TEXT,
	Developer TEXT,
	Critic_Score TEXT,
	User_Score TEXT,
	Year INT,
	PRIMARY KEY(id)
);