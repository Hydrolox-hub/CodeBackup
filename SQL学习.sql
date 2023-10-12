-- Active: 1695730306959@@127.0.0.1@3308@db_school
#创建数据库 
 CREATE DATABASE db_school
 DEFAULT CHARACTER SET GB2312
 DEFAULT COLLATE GB2312_chinese_ci;

 ALTER DATABASE db_school
 DEFAULT CHARACTER SET gb2312
 DEFAULT COLLATE gb2312_chinese_ci;

 USE db_school
 CREATE TABLE tb_student
 (
    studentNo CHAR(10) NOT NULL UNIQUE,
    studentName VARCHAR(20)NOT NULL,
    sex CHAR(2),
    birthday DATE,
    native VARCHAR(20),
    nation VARCHAR(10),
    classNo CHAR(6)
 ) ENGINE=InnoDB;


 CREATE TABLE tb_student1
 (
    studentNo INT(10) NOT NULL UNIQUE AUTO_INCREMENT,
    studentName VARCHAR(20)NOT NULL,
    sex CHAR(2),
    birthday DATE,
    native VARCHAR(20),
    nation VARCHAR(10),
    classNo CHAR(6)
 ) ENGINE=InnoDB;

 CREATE TABLE tb_student2
 (
    studentNo CHAR(10) NOT NULL UNIQUE,
    studentName VARCHAR(20)NOT NULL,
    sex CHAR(2),
    birthday DATE,
    native VARCHAR(20),
    nation VARCHAR(10) DEFAULT'汉',
    classNo CHAR(6)
 ) ENGINE=InnoDB;

 DROP TABLE tb_student;
 CREATE TABLE db_school.tb_student
 (
    studentNo CHAR(10),
    studentName VARCHAR(20)NOT NULL,
    sex CHAR(2) NOT NULL,
    birthday DATE,
    native VARCHAR(20),
    nation VARCHAR(10) DEFAULT'汉',
    classNo CHAR(6),
    CONSTRAINT PK_student PRIMARY KEY(studentNo)
 ) ENGINE=InnoDB;

CREATE TABLE tb_class
(
   classNo CHAR(6) PRIMARY KEY,
   className VARCHAR(20) NOT NULL  UNIQUE,
   department VARCHAR(30) NOT NULL,
   grade SMALLINT,
   classNum TINYINT
)ENGINE=InnoDB;

DROP TABLE tb_class;

CREATE TABLE tb_class
(
   classNo CHAR(6) PRIMARY KEY,
   className VARCHAR(20) NOT NULL,
   department VARCHAR(30) NOT NULL,
   grade SMALLINT,
   classNum TINYINT,
   CONSTRAINT UQ_class UNIQUE(className)
)ENGINE=InnoDB;

CREATE TABLE tb_course
(
   courseNo CHAR(6),
   courseName VARCHAR(20) NOT NULL,
   credit INT NOT NULL,
   courseHour INT NOT NULL,
   term CHAR(2),
   priorCourse CHAR(6),
   CONSTRAINT PK_course PRIMARY KEY(courseNo),
   CONSTRAINT FK_course FOREIGN KEY(priorCourse)
   REFERENCES tb_course(courseNo),
   CONSTRAINT CK_course CHECK(credit=courseHour/16)
)ENGINE=InnoDB;

CREATE TABLE tb_score
(
   studentNo CHAR(10),
   courseNo CHAR(6),
   score FLOAT CHECK(score>=0 AND score<=100),
   CONSTRAINT PK_score PRIMARY KEY(studentNo,courseNo),
   CONSTRAINT FK_score1 FOREIGN KEY(studentNo)
   REFERENCES tb_student(studentNo),
   CONSTRAINT FK_score2 FOREIGN KEY(courseNo)
   REFERENCES tb_course(courseNo)
)ENGINE=InnoDB;
 