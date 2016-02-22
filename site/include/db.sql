-- Drop tables that the database will use

DROP TABLE Member;
DROP TABLE Project;
DROP TABLE Groups;
DROP TABLE Group_relation;

-- Implement tables needed

CREATE TABLE Member
(
	ID INT NOT NULL AUTO_INCREMENT,
	Tel VARCHAR(15),	  -- +45-XX-XX-XX-XX <- 15 tegn max?
	Email VARCHAR(255),
	Website VARCHAR(255),
	LastName VARCHAR(255) NOT NULL,
	FirstName VARCHAR(255),   -- NOT NULL?
	Location VARCHAR(255), 	  -- Office
	Workplace VARCHAR(255), 
	Status VARCHAR(255),	  -- Professor, Lektor etc.
	PRIMARY KEY (ID)
)ENGINE=InnoDB;

CREATE TABLE Project
(
	PID INT NOT NULL AUTO_INCREMENT, -- Project ID
	Owner INT NOT NULL,
	Deadline DATE,
	Subject VARCHAR(255),
	PRIMARY KEY (PID),
	FOREIGN KEY (Owner) REFERENCES Member(ID)
)ENGINE=InnoDB;

CREATE TABLE Groups
(
	GID INT NOT NULL AUTO_INCREMENT, -- Group ID
	GName VARCHAR(255),
	GLocation VARCHAR(255),
	PRIMARY KEY (GID)
)ENGINE=InnoDB;

CREATE TABLE Group_relation
(
	GID INT NOT NULL,
	ID INT NOT NULL,
	-- PID INT NOT NULL,
	PRIMARY KEY (GID, ID),
	FOREIGN KEY (GID) REFERENCES Groups(GID),
	FOREIGN KEY (ID) REFERENCES Member(ID)
)ENGINE=InnoDB;
