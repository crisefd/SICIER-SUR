/*DROP TABLE IF EXISTS Person CASCADE;
CREATE TABLE Person(
	id VARCHAR(50) PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	tel_num VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL
);*/

DROP TABLE IF EXISTS Coordinator CASCADE;
CREATE TABLE Coordinator(
	id VARCHAR(50) PRIMARY KEY,
	/*id_person_fk VARCHAR(50),
	FOREIGN KEY(id_person_fk)
	REFERENCES Person(id) */
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	tel_num VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	is_active BOOLEAN NOT NULL,
	pass VARCHAR(50),
	UNIQUE(email)
);

DROP TABLE IF EXISTS Administrator CASCADE;
CREATE TABLE Administrator(
	id VARCHAR(50) PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	tel_num VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	is_active BOOLEAN NOT NULL,
	pass VARCHAR(50),
	UNIQUE(email)
	/*id_person_fk VARCHAR(50),
	FOREIGN KEY(id_person_fk)
	REFERENCES Person(id) */
);

/*DROP TABLE IF EXISTS Teacher CASCADE;
CREATE TABLE Teacher(
	id VARCHAR(50) PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	tel_num VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL
	id_person_fk VARCHAR(50),
	FOREIGN KEY(id_person_fk)
	REFERENCES Person(id)
);*/

DROP TABLE IF EXISTS MasterTeacher CASCADE;
CREATE TABLE MasterTeacher(
	id VARCHAR(50) PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	tel_num VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	sex VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL,
	marital_status VARCHAR(50) NOT NULL,
	institution VARCHAR(50) NOT NULL,
	grade VARCHAR(50) NOT NULL,
	secretariat VARCHAR(50) NOT NULL,
	area VARCHAR(50) NOT NULL,
	is_active BOOLEAN NOT NULL,
	pass VARCHAR(50),
	UNIQUE(email)
	/*id_teacher_fk VARCHAR(50),
	FOREIGN KEY(id_teacher_fk)
	REFERENCES Teacher(id)*/ 
);

DROP TABLE IF EXISTS LeaderTeacher CASCADE;
CREATE TABLE LeaderTeacher(
	id VARCHAR(50) PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	tel_num VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	sex VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL,
	marital_status VARCHAR(50) NOT NULL,
	institution VARCHAR(50) NOT NULL,
	department VARCHAR(50) NOT NULL,
	grade VARCHAR(50) NOT NULL,
	secretariat VARCHAR(50) NOT NULL,
	area VARCHAR(50) NOT NULL,
	is_active BOOLEAN NOT NULL,
	pass VARCHAR(50),
	UNIQUE(email)
	/*id_teacher_fk VARCHAR(50),
	FOREIGN KEY(id_teacher_fk)
	REFERENCES Teacher(id) */
);

DROP TABLE IF EXISTS MT_labor_exp CASCADE;
CREATE TABLE MT_labor_exp(
	id_MT_fk VARCHAR(50) NOT NULL,
	item VARCHAR(100) NOT NULL,
	FOREIGN KEY(id_MT_fk)
	REFERENCES MasterTeacher(id),
	PRIMARY KEY (id_MT_fk, item)
);

DROP TABLE IF EXISTS LT_labor_exp CASCADE;
CREATE TABLE LT_labor_exp(
	id_LT_fk VARCHAR(50) NOT NULL,
	item VARCHAR(100) NOT NULL,
	FOREIGN KEY(id_LT_fk)
	REFERENCES LeaderTeacher(id),
	PRIMARY KEY (id_LT_fk, item)
);

DROP TABLE IF EXISTS MT_academic_backg CASCADE;
CREATE TABLE MT_academic_backg(
	id_MT_fk VARCHAR(50) NOT NULL,
	item VARCHAR(100) NOT NULL,
	FOREIGN KEY(id_MT_fk)
	REFERENCES MasterTeacher(id),
	PRIMARY KEY(id_MT_fk, item)
);

DROP TABLE IF EXISTS LT_academic_backg CASCADE;
CREATE TABLE LT_academic_backg(
	id_LT_fk VARCHAR(50) NOT NULL,
	item VARCHAR(100) NOT NULL,
	FOREIGN KEY(id_LT_fk)
	REFERENCES LeaderTeacher(id),
	PRIMARY KEY(id_LT_fk, item)
);

DROP TABLE IF EXISTS Course CASCADE;
CREATE TABLE Course(
	id VARCHAR(50) NOT NULL,
	description VARCHAR(100) NOT NULL,
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	PRIMARY KEY(id)
);

DROP TABLE IF EXISTS Course_Activity CASCADE;
CREATE TABLE Course_Activity(
	id_course_fk VARCHAR(50) NOT NULL,
	activity VARCHAR(50),
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	weight FLOAT NOT NULL,--cambio de shaitan--
	FOREIGN KEY(id_course_fk)
	REFERENCES Course(id),
	PRIMARY KEY(activity),
	UNIQUE(activity)
);
/*
DROP TABLE IF EXISTS Activity_Grade CASCADE;
CREATE TABLE Activity_Grade(
	id_course_fk VARCHAR(50) NOT NULL,
	activity_fk VARCHAR NOT NULL,
	weight FLOAT NOT NULL,
	FOREIGN KEY(id_course_fk, activity_fk)
	REFERENCES Course_Activity(id_course_fk, activity),
	PRIMARY KEY(id_course_fk, activity_fk, weight)
);*/

DROP TABLE IF EXISTS Course_Cohort CASCADE;
CREATE TABLE Course_Cohort(
	id_course_fk VARCHAR(50) NOT NULL,
	cohort VARCHAR(50) NOT NULL,
	FOREIGN KEY(id_course_fk)
	REFERENCES Course(id),
	PRIMARY KEY(id_course_fk, cohort)
	--UNIQUE(cohort)
	
);

DROP TABLE IF EXISTS LT_Cohort CASCADE;
CREATE TABLE LT_Cohort(
	id_LT_fk VARCHAR(50) NOT NULL,
	id_course_fk VARCHAR(50) NOT NULL,
	cohort_fk VARCHAR(50) NOT NULL,
	FOREIGN KEY(id_LT_fk)
	REFERENCES LeaderTeacher(id),
	FOREIGN KEY(id_course_fk, cohort_fk)
	REFERENCES Course_Cohort(id_course_fk, cohort),
	PRIMARY KEY(id_LT_fk, id_course_fk, cohort_fk)
	
);

DROP TABLE IF EXISTS Activity_Grade_LT;
CREATE TABLE Activity_Grade_LT(
	id_LT_fk VARCHAR(50) NOT NULL,
	activity_fk VARCHAR(50) NOT NULL,
	score FLOAT,
	FOREIGN KEY(id_LT_fk)
	REFERENCES LeaderTeacher,
	FOREIGN KEY(activity_fk)
	REFERENCES Course_Activity(activity),
	PRIMARY KEY (id_LT_fk, activity_fk)

);

DROP TABLE IF EXISTS Enrollment CASCADE;
CREATE TABLE Enrollment(
	id_MT_fk VARCHAR(50) NOT NULL,
	id_LT_fk VARCHAR(50) NOT NULL,
	id_course_fk VARCHAR(50) NOT NULL,
	def_grade FLOAT,
	FOREIGN KEY(id_MT_fk)
	REFERENCES MasterTeacher(id),
	FOREIGN KEY(id_course_fk)
	REFERENCES Course(id),
	FOREIGN KEY(id_LT_fk)
	REFERENCES LeaderTeacher(id),
	PRIMARY KEY(id_MT_fk, id_course_fk)
	
);



ALTER TABLE Activity_Grade_LT OWNER TO shaitan;
ALTER TABLE Course_activity OWNER TO shaitan;
ALTER TABLE Administrator OWNER TO shaitan;
ALTER TABLE Coordinator OWNER TO shaitan;
ALTER TABLE MasterTeacher OWNER TO shaitan;
ALTER TABLE LeaderTeacher OWNER TO shaitan;
ALTER TABLE Course OWNER TO shaitan;
ALTER TABLE Enrollment OWNER TO shaitan;
ALTER TABLE Course_Cohort OWNER TO shaitan;
ALTER TABLE LT_academic_backg OWNER TO shaitan;
ALTER TABLE MT_academic_backg OWNER TO shaitan;
ALTER TABLE LT_labor_exp OWNER TO shaitan;
ALTER TABLE MT_labor_exp OWNER TO shaitan;
ALTER TABLE LT_Cohort OWNER TO shaitan;

------POBLACIÓN PRUEBA-----------------------------

---- Admin------

INSERT INTO Administrator values ('11111', 'shaitan', 'Tigreros', '123456', 'Cali', 'tigreros@gmail.com', TRUE, '12345ADMIN');
INSERT INTO Administrator values ('11115', 'cristhian', 'fuertes', '654321', 'Cali', 'fuertes@gmail.com', TRUE, '54321ADMIN');

----- coord----
INSERT INTO Coordinator values ('21111', 'daniel', 'Henao', '09876', 'Cali', 'henao@gmail.com', TRUE, '12345coord');
INSERT INTO Coordinator values ('21115', 'fabian', 'cano', '67890', 'Cali', 'cano@gmail.com', TRUE, '54321coord');

-----MT------

INSERT INTO MasterTeacher values ('1143829284', 'Oscar', 'Tigreros', '3739490', 'Cali', 'Oscar@gmail.com', 'M', '1989-12-12', 'soltero', 'Univalle', 'Ingeniero de Sistemas', 'algo', 'discretas', TRUE, 'pass123');
INSERT INTO MasterTeacher values ('1143829285', 'Julian', 'Casas', '3739491', 'Cali', 'Julian@gmail.com', 'M', '1990-02-07', 'casado', 'Univalle', 'Ingeniero electronico', 'algo', 'SO', TRUE, 'pass124');
INSERT INTO MasterTeacher values ('1143829286', 'Mauricio', 'Castaño', '3739492', 'Cali', 'Mauricio@gmail.com', 'M', '1970-06-11', 'soltero', 'Javeriana', 'Quimico', 'algo', 'Química organica', TRUE, 'pass125');
INSERT INTO MasterTeacher values ('1143829287', 'Oscar', 'Pardo', '3739493', 'Palmira', 'OscarPardo@gmail.com', 'M', '1976-12-12', 'soltero', 'Icesi', 'Lic. Matematicas', 'algo', 'Geometria', TRUE, 'pass126');	
INSERT INTO MasterTeacher values ('1143829288', 'Maria', 'Quintero', '3739494', 'Buga', 'Maria@gmail.com', 'F', '1989-04-02', 'casada', 'Autonoma', 'Ingeniera Química', 'algo', 'Química inorganica', TRUE, 'pass127');

----MT exp lab-----

INSERT INTO MT_labor_exp values ('1143829284', 'Eduguia matematicas 2 años');
INSERT INTO MT_labor_exp values ('1143829285', 'QIQ Calculo 9 meses');
INSERT INTO MT_labor_exp values ('1143829286', 'GIQ Química 4 años');
INSERT INTO MT_labor_exp values ('1143829287', 'IEF Estadistica 5 años');
INSERT INTO MT_labor_exp values ('1143829288', 'IEF Química 2 años');

---MT acad back-----
INSERT INTO MT_academic_backg values('1143829284', 'CIER-SUR matematicas 1');
INSERT INTO MT_academic_backg values('1143829284', 'CIER-SUR matematicas 2');
INSERT INTO MT_academic_backg values('1143829285', 'CIER-SUR Química 1');
INSERT INTO MT_academic_backg values('1143829287', 'CIER-SUR matematicas 1');
INSERT INTO MT_academic_backg values('1143829287', 'CIER-SUR matematicas 2');

---LT----

INSERT INTO LeaderTeacher values ('1243829284', 'Fernando', 'Bolaños', '2739490', 'Cali', 'Fernando@gmail.com', 'M', '1983-12-12', 'soltero', 'Univalle','Sistemas', 'Ingeniero de Sistemas', 'algo', 'discretas', TRUE, 'lpass123');
INSERT INTO LeaderTeacher values ('1243829285', 'Daniel', 'Henao', '2739491', 'Cali', 'Daniel@gmail.com', 'M', '1983-02-07', 'casado', 'Univalle', 'electronica', 'Ingeniero electronico', 'algo', 'SO', TRUE, 'lpass124');
INSERT INTO LeaderTeacher values ('1243829286', 'Camilo', 'Castaño', '2739492', 'Cali', 'Camilo@gmail.com', 'M', '1983-06-11', 'soltero', 'Javeriana', 'Química', 'Quimico', 'algo', 'Química organica', TRUE, 'lpass125');
INSERT INTO LeaderTeacher values ('1243829287', 'Andres', 'Rojas', '2739493', 'Palmira', 'Andres@gmail.com', 'M', '1983-12-12', 'soltero', 'Icesi', 'matematicas', 'Lic. Matematicas', 'algo', 'Geometria', TRUE, 'lpass126');	
INSERT INTO LeaderTeacher values ('1243829288', 'Maria', 'Rojas', '2739494', 'Buga', 'MariaR@gmail.com', 'F', '1983-04-02', 'casada', 'Autonoma', 'Química', 'Ingeniera Química', 'algo', 'Química inorganica', TRUE, 'lpass127');

----LT exp lab-----

INSERT INTO LT_labor_exp values ('1243829284', 'Colombo 2 años');
INSERT INTO LT_labor_exp values ('1243829285', 'Colombo 2 años');
INSERT INTO LT_labor_exp values ('1243829286', 'Colombo 2 años');
INSERT INTO LT_labor_exp values ('1243829287', 'Colombo 2 años');
INSERT INTO LT_labor_exp values ('1243829288', 'Colombo 2 años');

---LT acad back----

INSERT INTO LT_academic_backg values('1243829284', 'CIER-SUR Ofimatica 1');
INSERT INTO LT_academic_backg values('1243829285', 'CIER-SUR Ofimatica 1'); 
INSERT INTO LT_academic_backg values('1243829286', 'CIER-SUR Ofimatica 1'); 
INSERT INTO LT_academic_backg values('1243829287', 'CIER-SUR Ofimatica 1'); 
INSERT INTO LT_academic_backg values('1243829288', 'CIER-SUR Ofimatica 1'); 

------Courso-------

INSERT INTO Course values('252525M', 'Curso basico de Ofimatica nivel 1', '2015-05-24', '2015-07-05');
INSERT INTO Course values('252526M', 'Curso basico de Ofimatica nivel 2', '2015-05-24', '2015-07-05');
INSERT INTO Course values('252527M', 'Curso basico de Ofimatica nivel 3', '2015-05-24', '2015-07-05');

------ Course Act-----

INSERT INTO Course_Activity values('252525M', '45456A', '2015-05-30', '2015-06-05', '0.333');
INSERT INTO Course_Activity values('252525M', '45457A', '2015-06-30', '2015-07-05', '0.333');
INSERT INTO Course_Activity values('252525M', '45458A', '2015-07-30', '2015-08-05', '0.333');
INSERT INTO Course_Activity values('252526M', '45459A', '2015-05-30', '2015-06-05', '0.333');
INSERT INTO Course_Activity values('252526M', '45450A', '2015-06-30', '2015-07-05', '0.333');
INSERT INTO Course_Activity values('252526M', '45451A', '2015-07-30', '2015-08-05', '0.333');
INSERT INTO Course_Activity values('252527M', '45452A', '2015-05-30', '2015-06-05', '0.333');
INSERT INTO Course_Activity values('252527M', '45453A', '2015-06-30', '2015-07-05', '0.333');
INSERT INTO Course_Activity values('252527M', '45454A', '2015-07-30', '2015-08-05', '0.333');


----- Act grade-------
--INSERT INTO Activity_Grade values('252525M', '45456A', '0.333');
--INSERT INTO Activity_Grade values('252525M', '45457A', '0.333');
--INSERT INTO Activity_Grade values('252525M', '45458A', '0.333');
--INSERT INTO Activity_Grade values('252526M', '45459A', '0.333');
--INSERT INTO Activity_Grade values('252526M', '45450A', '0.333');
--INSERT INTO Activity_Grade values('252526M', '45451A', '0.333');
--INSERT INTO Activity_Grade values('252527M', '45452A', '0.333');
--INSERT INTO Activity_Grade values('252527M', '45453A', '0.333');
--INSERT INTO Activity_Grade values('252527M', '45454A', '0.333');

--- Act grade Lt---

INSERT INTO Activity_Grade_LT values('1243829284', '45456A', '3.7');
INSERT INTO Activity_Grade_LT values('1243829285', '45459A', '4.2');
INSERT INTO Activity_Grade_LT values('1243829286', '45452A', '2.7');

-----Course cohort -----

INSERT INTO Course_Cohort values('252525M', '1');
INSERT INTO Course_Cohort values('252526M', '1');
INSERT INTO Course_Cohort values('252527M', '1');

----LT Cohort-----

INSERT INTO LT_Cohort values('1243829284', '252525M','1' );
INSERT INTO LT_Cohort values('1243829285', '252526M','1' );
INSERT INTO LT_Cohort values('1243829286', '252527M','1' );

----Enrrol------

INSERT INTO Enrollment values('1143829284', '1243829284', '252525M','0.0');
INSERT INTO Enrollment values('1143829284', '1243829285', '252526M','0.0');
INSERT INTO Enrollment values('1143829285', '1243829286', '252526M','0.0');
INSERT INTO Enrollment values('1143829285', '1243829287', '252527M','0.0');
INSERT INTO Enrollment values('1143829286', '1243829286', '252525M','0.0');
