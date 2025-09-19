CREATE TABLE class(
	id INT(10) NOT NULL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	description TEXT NOT NULL
);

show tables;

INSERT INTO class (id, name, description)
	VALUES (1, "HTML", "Kelas belajar HTML");

SELECT * FROM class;

INSERT INTO class (id, name, description)
	VALUES
		(2, "CSS", "Kelas belajar CSS"),
		(3, "Javascript", "Kelas belajar Javascript"),
		(4, "Bootstrap", "Kelas belajat Bootstrap");

SELECT * FROM class;

SELECT `id`, `name` FROM class;

SELECT * FROM class;
where id = 2

update class
  set description = "Kelas untuk belajar HTML"
  where id = 1;

UPDATE class
  set name = "Cascading Stylesheey"
    description = "Kelas untuk belajar CSS"
  WHERE id = 2;

delete FROM class
  WHERE ID = 3;

SELECT * FROM class;

  