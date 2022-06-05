CREATE TABLE Director(
DirectorID SERIAL NOT NULL PRIMARY KEY,
DirectorName varchar(50) NOT NULL
);

CREATE TABLE Country(
CountryID SERIAL NOT NULL PRIMARY KEY,
Country varchar(50) NOT NULL
);

CREATE TABLE Movie(
   MovieID SERIAL NOT NULL,
   MovieTitle varchar (50) NOT NULL,
   ReleaseYear varchar(10) NOT NULL,
   CountryID INT NOT NULL,
   DirectorID INT NOT NULL,
   PRIMARY KEY(MovieID),
      FOREIGN KEY(CountryID) 
		REFERENCES Country(CountryID),
	  FOREIGN KEY(DirectorID) 
		REFERENCES Director(DirectorID)
);

INSERT INTO Director VALUES 
					(DEFAULT, 'Tim Miller'),
					(DEFAULT, 'James Wan'),
					(DEFAULT, 'Rajkumar Hirani'),
					(DEFAULT, 'Ridley Scott'),
					(DEFAULT, 'Todd Phillips'),
					(DEFAULT, 'Sam Mendes'),
					(DEFAULT, 'Christopher Nolan');
					

INSERT INTO Movie VALUES 
    				(DEFAULT, 'Superman vs Batman', '2016', 1, 1),
    				(DEFAULT, 'Deadpool', '2016', 1, 2),
    				(DEFAULT, 'Furious 7', '2015', 1, 3),
    				(DEFAULT, 'PK', '2014', 2, 4),
    				(DEFAULT, 'Gladiator', '2000', 3, 5),
    				(DEFAULT, 'The Hangover', '2009', 1, 6),
    				(DEFAULT, '3 Idiots', '2009', 2, 4),
    				(DEFAULT, 'Spectre', '2015', 3, 7),
    				(DEFAULT, 'Batman Begins', '2005', 1, 8),
    				(DEFAULT, 'The Dark Knight', '2008', 1, 8);
					
					
INSERT INTO Country VALUES 
					(DEFAULT, 'United States'),
					(DEFAULT, 'India'),
					(DEFAULT, 'United Kingdom');