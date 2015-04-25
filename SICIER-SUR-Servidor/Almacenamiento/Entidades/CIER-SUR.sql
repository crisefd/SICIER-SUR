DROP TABLE IF EXISTS Person CASCADE;/*
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
	is_active BOOLEAN NOT NULL
);

DROP TABLE IF EXISTS Administrator CASCADE;
CREATE TABLE Administrator(
	id VARCHAR(50) PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	tel_num VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	is_active BOOLEAN NOT NULL
	/*id_person_fk VARCHAR(50),
	FOREIGN KEY(id_person_fk)
	REFERENCES Person(id) */
);

DROP TABLE IF EXISTS Teacher CASCADE;/*
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
	is_active BOOLEAN NOT NULL
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
	grade VARCHAR(50) NOT NULL,
	secretariat VARCHAR(50) NOT NULL,
	area VARCHAR(50) NOT NULL,
	is_active BOOLEAN NOT NULL
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
	FOREIGN KEY(id_course_fk)
	REFERENCES Course(id),
	PRIMARY KEY(id_course_fk, activity)
);

DROP TABLE IF EXISTS Activity_Grade CASCADE;
CREATE TABLE Activity_Grade(
	id_course_fk VARCHAR(50) NOT NULL,
	activity_fk VARCHAR NOT NULL,
	FOREIGN KEY(id_course_fk, activity_fk)
	REFERENCES Course_Activity(id_course_fk, activity),
	PRIMARY KEY(id_course_fk, activity_fk)
);

DROP TABLE IF EXISTS Course_Cohort CASCADE;
CREATE TABLE Course_Cohort(
	id_course_fk VARCHAR(50) NOT NULL,
	cohort VARCHAR(50) NOT NULL,
	FOREIGN KEY(id_course_fk)
	REFERENCES Course(id),
	PRIMARY KEY(id_course_fk, cohort)
	
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

ALTER TABLE activity_grade OWNER TO crisefd;
ALTER TABLE Course_activity OWNER TO crisefd;
ALTER TABLE Administrator OWNER TO crisefd;
ALTER TABLE Coordinator OWNER TO crisefd;
ALTER TABLE MasterTeacher OWNER TO crisefd;
ALTER TABLE LeaderTeacher OWNER TO crisefd;
ALTER TABLE Course OWNER TO crisefd;
ALTER TABLE Enrollment OWNER TO crisefd;
ALTER TABLE Course_Cohort OWNER TO crisefd;
ALTER TABLE LT_academic_backg OWNER TO crisefd;
ALTER TABLE MT_academic_backg OWNER TO crisefd;
ALTER TABLE LT_labor_exp OWNER TO crisefd;
ALTER TABLE MT_labor_exp OWNER TO crisefd;


