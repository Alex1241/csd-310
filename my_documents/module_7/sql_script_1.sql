
CREATE USER 'userA'@'localhost' IDENTIFIED WITH mysql_native_password BY "SQLtest";
GRANT ALL PRIVILEGES ON pysports.* TO 'userA'@'localhost';
DROP USER IF EXISTS 'userA'@'localhost';

CREATE TABLE team (
    player_id   INT     Not Null    AUTO_INCREMENT,
    first_name VARCHAR(75)      NOT NULL,
    last_name VARCHAR(75)       NOT NULL,
    team_id     INT     NOT NULL,

    PRIMARY KEY(player_id)
    CONSTRAINT  fk team
    FOREIGN KEY(team_id)
        References team(team_id)
);

INSERT INTO team( team_name, mascot )  VALUES ( 'Team Gandalf', 'White Wizards' );

DROP TABLE IF EXISTS player;

SELECT team_id FROM team WHERE team_name = "Team Sauron";

