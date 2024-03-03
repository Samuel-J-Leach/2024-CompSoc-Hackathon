-- database creation

DROP DATABASE IF EXISTS hackathon;

CREATE DATABASE hackathon;

USE hackathon;

-- table creation

-- course table
DROP TABLE IF EXISTS Course;

CREATE TABLE Course (
    COURSE_ID   INT UNSIGNED NOT NULL,
    title       VARCHAR(255) NOT NULL,
    PRIMARY KEY (COURSE_ID)
);

-- module table
DROP TABLE IF EXISTS Module;

CREATE TABLE Module (
    MODULE_ID   INT UNSIGNED NOT NULL,
    title       VARCHAR(255) NOT NULL,
    PRIMARY KEY (MODULE_ID)
);

-- module_course table
DROP TABLE IF EXISTS Module_Course;

CREATE TABLE Module_Course (
    MODULE  INT UNSIGNED NOT NULL,
    COURSE  INT UNSIGNED NOT NULL,
    PRIMARY KEY (MODULE, COURSE),
    FOREIGN KEY (COURSE) REFERENCES Course (COURSE_ID) ON DELETE CASCADE,
    FOREIGN KEY (MODULE) REFERENCES Module (MODULE_ID) ON DELETE RESTRICT
);

-- Convener table
DROP TABLE IF EXISTS Convener;

CREATE TABLE Convener (
    URN     INT UNSIGNED NOT NULL,
    FName   VARCHAR(255) NOT NULL,
    LName   VARCHAR(255) NOT NULL,
    MODULE  INT UNSIGNED NOT NULL,
    PRIMARY KEY (URN),
    FOREIGN KEY (MODULE) REFERENCES Module (MODULE_ID) ON DELETE RESTRICT
);

-- Student table
DROP TABLE IF EXISTS Student;

-- add email later if u want to
CREATE TABLE Student (
    URN         INT UNSIGNED NOT NULL,
    FName       VARCHAR(255) NOT NULL,
    LName       VARCHAR(255) NOT NULL,
    COURSE      INT UNSIGNED NOT NULL,
    preference  ENUM ('none','robotics','AI','cyber security','web development','databases','software engineering','electronic engineering','programming','circuit design','game development'),
    PRIMARY KEY (URN),
    FOREIGN KEY (COURSE) REFERENCES Course (COURSE_ID) ON DELETE RESTRICT
);

-- Department table
DROP TABLE IF EXISTS Department;

CREATE TABLE Department (
    DEPT_ID     INT UNSIGNED NOT NULL,
    title       VARCHAR(255) NOT NULL,
    PRIMARY KEY (DEPT_ID)
);

-- Academic table
DROP TABLE IF EXISTS Academic;

CREATE TABLE Academic (
    URN     INT UNSIGNED NOT NULL,
    FName   VARCHAR(255) NOT NULL,
    LName   VARCHAR(255) NOT NULL,
    DEPARTMENT  INT UNSIGNED NOT NULL,
    preference  ENUM ('none','robotics','AI','cyber security','web development','databases','software engineering','electronic engineering','programming','circuit design','game development'),
    PRIMARY KEY (URN),
    FOREIGN KEY (DEPARTMENT) REFERENCES Department (DEPT_ID) ON DELETE RESTRICT
);

-- Student_Academic_Module table
DROP TABLE IF EXISTS Student_Academic_Module;

CREATE TABLE Student_Academic_Module (
    STUDENT     INT UNSIGNED NOT NULL,
    ACADEMIC    INT UNSIGNED NOT NULL,
    MODULE      INT UNSIGNED NOT NULL,
    PRIMARY KEY (STUDENT, ACADEMIC, MODULE),
    FOREIGN KEY (STUDENT) REFERENCES Student (URN) ON DELETE CASCADE,
    FOREIGN KEY (ACADEMIC) REFERENCES Academic (URN) ON DELETE CASCADE,
    FOREIGN KEY (MODULE) REFERENCES Module (MODULE_ID) ON DELETE RESTRICT
);

-- Assessment table
DROP TABLE IF EXISTS Assessment;

CREATE TABLE Assessment (
    ASS_ID      INT UNSIGNED NOT NULL,
    Total_Mark  INT NOT NULL,
    Pass_Mark   INT NOT NULL,
    Weighting   INT NOT NULL,
    MODULE      INT UNSIGNED NOT NULL,
    CHECK (Weighting > 0),
    CHECK (Weighting <= 100),
    CHECK (Pass_Mark > 0),
    CHECK (Pass_Mark <= Total_Mark),
    CHECK (Total_Mark > 0),
    PRIMARY KEY (ASS_ID),
    FOREIGN KEY (MODULE) REFERENCES Module (MODULE_ID) ON DELETE RESTRICT
);

-- Mark table
DROP TABLE IF EXISTS Mark;

-- make sure to include validation in front end to ensure Mark is not more than Total_Mark
CREATE TABLE Mark (
    ASSESSMENT  INT UNSIGNED NOT NULL,
    STUDENT     INT UNSIGNED NOT NULL,
    ACADEMIC    INT UNSIGNED NOT NULL,
    Mark        INT NOT NULL,
    CHECK (Mark >= 0),
    PRIMARY KEY (ASSESSMENT, STUDENT, ACADEMIC),
    FOREIGN KEY (ASSESSMENT) REFERENCES Assessment (ASS_ID) ON DELETE RESTRICT,
    FOREIGN KEY (STUDENT) REFERENCES Student (URN) ON DELETE CASCADE,
    FOREIGN KEY (ACADEMIC) REFERENCES Academic (URN) ON DELETE CASCADE
);



-- Data insertion

-- Department data
INSERT INTO Department VALUES 
(010,'Department of Computer Science'),
(020,'Department of Electronics and Electrical Engineering');

-- Course data
INSERT INTO Course VALUES 
(100,'BSc Computer Science'),
(101,'BSc Computer Information Technology'),
(200,'MSc Data Science'),
(201,'MSc Security'),
(210,'MSc Electrical Engineering');

INSERT INTO Student VALUES 
(1234567,'Hallam','Saunders',100,'none'),
(2345678,'Leon','Queen',100,'none'),
(3456789,'Samuel','Leach',100,'none');

INSERT INTO Academic VALUES 
(0987654,'Joe','Appleton',010,'none'),
(9876543,'Joey','Lam',010,'none'),
(8765432,'Brijesh','Dongol',010,'none'),
(7654321,'John','Doe',020,'none'),
(6543210,'Skibidi','Rizzler',020,'none');

INSERT INTO Module VALUES 
(1026,'software engineering'),
(1027,'web and database systems'),
(1028,'computer security'),
(1030,'foundations of electronics'),
(1031,'foundations of computing');

INSERT INTO Convener VALUES 
(1029384,'John','Smith',1026),
(2938475,'Jane','Doe',1027),
(3847561,'Bob','Gunn',1028),
(4756102,'Samantha','Lee',1030),
(5610293,'Dave','Bourne',1031);

-- for modules that have two assessments, if one is failed, it goes to moderation
-- and the moderator can check whether they did well enough on the other assessment to pass the module
INSERT INTO Assessment VALUES 
(10260,100,40,100,1026),
(10270,100,40,100,1027),
(10280,100,40,100,1028),
(10300,100,40,100,1030),
(10310,100,40,70,1031),
(10311,100,40,30,1031);

-- add data for module_course table