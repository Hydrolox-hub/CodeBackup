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

CREATE DATABASE db_sp
DEFAULT CHARACTER SET GB2312
DEFAULT COLLATE GB2312_chinese_ci;

CREATE TABLE S 
(
   SNO CHAR(5),
   SNAME VARCHAR(20) NOT NULL UNIQUE,
   STATUS SMALLINT,
   CITY VARCHAR(20),
   CONSTRAINT PK_S PRIMARY KEY (SNO),
   CONSTRAINT CK_S CHECK(CITY != 'London' OR STATUS=20)
)ENGINE=InnoDB;

CREATE TABLE P 
(
   PNO CHAR(5),
   PNAME VARCHAR(15) NOT NULL,
   COLOR VARCHAR(10) CHECK(COLOR IN ('Red','Yellow','Green','Blue')),
   WEIGHT INT,
   CONSTRAINT PK_P PRIMARY KEY (PNO) 
)ENGINE=InnoDB;

CREATE TABLE SP
(
   SNO CHAR(5),
   PNO CHAR(5),
   QTY INT,
   CONSTRAINT PK_SPJ PRIMARY KEY (SNO,PNO),
   CONSTRAINT FK_SPJ1 FOREIGN KEY (SNO)  REFERENCES S (SNO),
   CONSTRAINT FK_SPJ2 FOREIGN KEY (PNO)  REFERENCES P (PNO)
)ENGINE=InnoDB;
 
SELECT classNo,department,className FROM tb_class;

SELECT DISTINCT department FROM tb_class;

SELECT * FROM tb_course;

SELECT studentName,sex,'Age:',YEAR(NOW())-YEAR(birthday) FROM tb_student;

SELECT studentName AS 姓名,sex 性别,YEAR(NOW())-YEAR(birthday) 年龄 FROM tb_student;

SELECT courseName,credit,courseHour FROM tb_course WHERE courseHour>=64;

SELECT studentNo,studentName,native,nation FROM tb_student WHERE nation!='汉' and sex ='男';

SELECT studentName,sex,birthday FROM tb_student WHERE birthday BETWEEN '1996-01-01'AND'1996-12-31';

SELECT studentName,sex,birthday FROM tb_student WHERE birthday NOT BETWEEN '1996-01-01'AND'1996-12-31';

SELECT * FROM tb_student WHERE native IN ('北京','天津','上海');

SELECT * FROM tb_student WHERE native NOT IN ('北京','天津','上海');

SELECT studentNo,studentName,classNo FROM tb_student WHERE studentName LIKE  '李%';

SELECT studentNo,studentName,classNo FROM tb_student WHERE studentName NOT LIKE  '李%';

SELECT studentNo,studentName,classNo FROM tb_student WHERE studentName LIKE  '%明%';

SELECT studentNo,studentName,classNo FROM tb_student WHERE studentName LIKE  '李__';

SELECT * FROM tb_course WHERE courseName LIKE '%#_%'ESCAPE '#';