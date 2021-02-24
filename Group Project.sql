create database backup_Project;
use backup_Project;

CREATE TABLE instructors_table(
  Instructor_ID INT NOT NULL  PRIMARY KEY ,
  Instructor_FirstName VARCHAR(45) NULL,
  Instructor_LastName VARCHAR(45) NULL,
  Instructor_Qualification VARCHAR(45) NULL,
  Company_ID INT
 );

ALTER TABLE instructors_table ADD CONSTRAINT Company_ID FOREIGN KEY (Company_ID) REFERENCES company_table (Company_ID);
  DESCRIBE instructors_table;

  
  INSERT INTO instructors_table VALUE('0001','Ahmad', 'Achikzai','Master','1010');
  INSERT INTO instructors_table VALUE('0002','Mahmood', 'Mahmoodzai','Master','1919');
  INSERT INTO instructors_table VALUE('0003','Salahuddin', 'daudzai','Master','1818');
  INSERT INTO instructors_table VALUE('0004','Safdar', 'Hayat','Master','1717');
  INSERT INTO instructors_table VALUE('0005','Mirza', 'Walizada','Master','1616');
  INSERT INTO instructors_table VALUE('0006','Ali', 'Ahmadzai','Master','1515');
  INSERT INTO instructors_table VALUE('0007','Idris', 'Totakhil','Master','1414');
  INSERT INTO instructors_table VALUE('0008','Shaban', 'Maynazai','Master','1313');
  INSERT INTO instructors_table VALUE('0009','Khider', 'Hayat','Master','1212');
  INSERT INTO instructors_table VALUE('0010','Mohammad', 'Hayat','Master','2222');
  
  select* from instructors_table;


  CREATE TABLE buildings_table (
  Building_ID INT PRIMARY KEY,
  Building_Name VARCHAR(45) NULL
);
  
  describe buildings_table;
  
  
INSERT INTO buildings_table VALUE('01','Building A');
INSERT INTO buildings_table VALUE('02','Building B');
INSERT INTO buildings_table VALUE('03','Building C');
INSERT INTO buildings_table VALUE('04','Building D');
INSERT INTO buildings_table VALUE('05','Building E');
INSERT INTO buildings_table VALUE('06','Building F');
INSERT INTO buildings_table VALUE('07','Building G');
INSERT INTO buildings_table VALUE('08','Building H');
INSERT INTO buildings_table VALUE('09','Building I');
INSERT INTO buildings_table VALUE('10','Building J');

Select* from buildings_table;
  
  
  CREATE TABLE classrooms_table (
  Classroom_ID INT PRIMARY KEY,
  Building_ID INT,
	FOREIGN KEY (Building_ID) REFERENCES buildings_table (Building_ID));
describe classrooms_table;
INSERT INTO classrooms_table VALUE('110','10');
INSERT INTO classrooms_table VALUE('120','09');
INSERT INTO classrooms_table VALUE('130','08');
INSERT INTO classrooms_table VALUE('140','07');
INSERT INTO classrooms_table VALUE('150','06');
INSERT INTO classrooms_table VALUE('160','05');
INSERT INTO classrooms_table VALUE('170','04');
INSERT INTO classrooms_table VALUE('180','03');
INSERT INTO classrooms_table VALUE('190','02');
INSERT INTO classrooms_table VALUE('200','01');

select* from classrooms_table;




  CREATE TABLE company_table (
  Company_ID INT NOT NULL,
  Company_Name VARCHAR(45) NULL,
  Company_Contact_Email VARCHAR(45) NULL,
  Company_Address VARCHAR(45) NULL,
  Instructor_ID INT NULL,
  PRIMARY KEY (Company_ID),
    FOREIGN KEY (Instructor_ID) REFERENCES instructors_table (Instructor_ID)
    );
    
    describe company_table;
    
INSERT INTO company_table VALUE('2222','Cisco','cisco.com','Darul-Aman Road', '10');
INSERT INTO company_table  VALUES ('1212', 'IBM', 'nobodycares@ywouldthey.com', 'Pol-e-Charkhi', '9');
INSERT INTO company_table VALUES ('1313', 'Hasib And Bros', 'Hasib@gmail.com', 'Kartey 3', '8');
INSERT INTO company_table VALUES ('1414', 'Sey@r', 'seyar@yahoo.com', 'Kolola pushta', '7');
INSERT INTO company_table VALUES ('1515', 'Maihan Zamin ', 'Watan@gmail.com', 'Taimani', '6');
INSERT INTO company_table VALUES ('1616', 'Ali Electronics', 'Ali@hotmail.com', 'Khwaja bughra', '5');
INSERT INTO company_table VALUES ('1717', 'Microsoft ', 'Microsoft@microsoft.com', 'Pol-e-Sokhta', '4');
INSERT INTO company_table VALUES ('1818', 'Apple', 'apple@icloud.com', 'Froshgah', '3');
INSERT INTO company_table VALUES ('1919', 'Google', 'googe@gmail.com', 'Sharinaw', '2');
INSERT INTO company_table VALUES ('1010', 'Dell', 'Dell@gmail.com', 'Paykob-e-Naswar','1');
select* from company_table;
    
    
    
    
    
    
    
    
    CREATE TABLE programs_table (
  Program_ID INT NOT NULL,
  Program_Name VARCHAR(45) NULL,
 Start_Date DATE,
  End_Date Date,
  Program_Description VARCHAR(45) NULL,
  Company_ID INT NULL,
  PRIMARY KEY (Program_ID),
    FOREIGN KEY (Company_ID) REFERENCES company_table (Company_ID)
  );
  

    describe programs_table;
    
  
    INSERT INTO programs_table VALUES ('303030', 'HCI Program', '2019-1-1','2020-1-1','It is goinng to be about hci','2222');
    INSERT INTO programs_table VALUES ('303040', 'IT Program', '2019-1-1','2020-1-1','It is goinng to be about pcs','1212');
    INSERT INTO programs_table VALUES ('303050', 'Communications Program', '2019-1-1','2020-1-1','It is goinng to be about communicating','1313');
    INSERT INTO programs_table VALUES ('303060', 'Ethics Program', '2019-1-1','2020-1-1','It is goinng to be about ettiquette','1414');
    INSERT INTO programs_table VALUES ('303070', 'Database Program', '2019-1-1','2020-1-1','It is goinng to be about making a datbase','1515');
    INSERT INTO programs_table VALUES ('303080', 'Games Program', '2019-1-1','2020-1-1','It is goinng to be about games','1616');
    INSERT INTO programs_table VALUES ('303090', 'Design Program', '2018-1-1','2019-1-1','It is goinng to be about designing','1717');
    INSERT INTO programs_table VALUES ('303100', 'Web Program', '2018-1-1','2019-1-1','It is goinng to be about web development','1818');
    INSERT INTO programs_table VALUES ('303110', 'Intro Program', '2018-1-1','2019-1-1','It is goinng to be about programming','1919');
    INSERT INTO programs_table VALUES ('303120', 'Hacking Program', '2018-1-1','2019-1-1','It is goinng to be about hacking','1010');
    INSERT INTO programs_table VALUES ('303130', 'Hacking Program II', '2018-1-1','2019-1-1','Extended hacking','1010');
 
    
    
    CREATE TABLE participants_table (
  Participant_ID INT NOT NULL PRIMARY KEY ,
  Partcipant_FirstName VARCHAR(45),
  Participant_LastName VARCHAR(45) ,
  Participant_Age INT,
  Participant_PhoneNo INT,
  Participant_Email VARCHAR(45) UNIQUE,
  PRIMARY KEY(Participant_ID,Partcipant_FirstName)
  );

insert into participants_table values('36762', 'Sulaiman','Hayat','21', '0700564884','sulaiman.Hayat@auaf.edu.af');
insert into participants_table values('31564', 'Mohammad','reza','20', '0700561644','mohammad.reza@auaf.edu.af');
insert into participants_table values('36154', 'khider','Hayat','25', '0700597884','khider.Hayat@auaf.edu.af');
insert into participants_table values('36164', 'ali','anwari','24', '0768764885','ali.anwari@auaf.edu.af');
insert into participants_table values('26762', 'Shah ','kliman','20', '070658484','Shah.klimant@auaf.edu.af');
insert into participants_table values('16762', 'steve','Austin','27', '0704562484','Steve.austin.Hayat@auaf.edu.af');
insert into participants_table values('35464', 'Mark','Ruffalo','26', '0798984884','Mark.ruffalo@auaf.edu.af');
insert into participants_table values('25464', 'John','Cena','42', '0700562484','john.cena@auaf.edu.af');
insert into participants_table values('15463', 'Magnus','Carlsen','27', '0799444884','magnus.carlsen@auaf.edu.af');
insert into participants_table values('23497', 'Hou','Yifan','26', '0700985134','hou.yifan@auaf.edu.af');


describe participants_table;

select*from participants_table;



 CREATE TABLE modules_table (
  Module_ID INT NOT NULL,
  Module_Name VARCHAR(45) NULL,
  Module_Assessment VARCHAR(45) NULL,
  Program_ID INT NULL,
  Company_ID INT NULL,
  PRIMARY KEY (Module_ID),
    FOREIGN KEY (Company_ID) REFERENCES company_table (Company_ID),
    FOREIGN KEY (Program_ID) REFERENCES programs_table (Program_ID)
   );
   
   describe modules_table;
   
   
   
   insert into modules_table value('10001','Module#1','very good', '303030','1212');
   insert into modules_table value('10002','Module#2',' good', '303040','1313');
   insert into modules_table value('10003','Module#3','not good', '303050','1414');
   insert into modules_table value('10004','Module#4','good', '303060','1515');
   insert into modules_table value('10005','Module#5','excellent', '303070','1616');
   insert into modules_table value('10006','Module#6','bad', '303080','1717');
   insert into modules_table value('10007','Module#7','fairly good', '303090','1818');
   insert into modules_table value('10008','Module#8','not bad', '303100','1919');
   insert into modules_table value('10009','Module#9','magnificent', '303110','2222');
   insert into modules_table value('10010','Module#10','extraordinary', '303120','1010');  
   
   select* from modules_table;
   
CREATE TABLE sessions_table (
  Session_ID INT NOT NULL,
  Session_Name VARCHAR(45) NULL,
  Session_Timing TIME NULL,
  Session_Duration INT NULL,
  Program_ID INT NULL,
  Classroom_ID INT NULL,
  Company_ID INT NULL,
  PRIMARY KEY (Session_ID),
    FOREIGN KEY (Program_ID) REFERENCES programs_table (Program_ID),
    FOREIGN KEY (Classroom_ID) REFERENCES classrooms_table (Classroom_ID),
    FOREIGN KEY (Company_ID) REFERENCES company_table (Company_ID)
);

describe sessions_table;
insert into sessions_table values('1',"first day",'12:30','80','303030','200','1010');
insert into sessions_table values('2',"second day",'11:00','80','303040','190','2222');
insert into sessions_table values('3',"Third day",'12:30','80','303050','180','1212');
insert into sessions_table values('4',"Fourth day",'1:00','80','303060','170','1313');
insert into sessions_table values('5',"Fifth day",'4:00','80','303070','160','1414');
insert into sessions_table values('6',"sixth day",'3:00','80','303080','150','1515');
insert into sessions_table values('7',"Seventh day",'3:30','80','303090','140','1616');
insert into sessions_table values('8',"eighth day",'4:30','80','303100','130','1717');
insert into sessions_table values('9',"ninth day",'5:50','80','303110','120','1818');
insert into sessions_table values('10',"tenth day",'3:30','80','303120','110','1919');

select* from sessions_table;




CREATE TABLE Enrollments_Table(
Enrollment_ID INT PRIMARY KEY,
Enroll_Date DATE,
Enroll_Time TIME,
Session_ID INT,
Program_ID INT,
Company_ID INT,
Participant_ID INT,
Partcipant_FirstName VARCHAR(45),
FOREIGN KEY(Session_ID)REFERENCES sessions_table(Session_ID),
FOREIGN KEY(Program_ID)REFERENCES programs_table(Program_ID) ,
FOREIGN KEY(Company_ID )REFERENCES company_table(Company_ID),
FOREIGN KEY(Participant_ID,Partcipant_FirstName)REFERENCES participants_table(Participant_ID,Partcipant_FirstName)
);

describe Enrollments_Table; 
select*from Enrollments_Table;

insert into Enrollments_Table values('11','2019-1-1','1:00','1','303030', '2222','23497','Hou');
insert into Enrollments_Table values('12','2019-1-1','1:30','1','303040', '1010','31564','Mohammad');
insert into Enrollments_Table values('13','2019-1-1','1:40','1','303050', '1212','36762','Sulaiman');
insert into Enrollments_Table values('14','2019-1-1','5:00','1','303060', '1313','36154','khider');
insert into Enrollments_Table values('15','2019-1-1','3:00','1','303070', '1414','36164','ali');
insert into Enrollments_Table values('16','2019-1-1','3:20','1','303080', '1515','26762','Shah ');
insert into Enrollments_Table values('17','2019-1-1','2:30','1','303090', '1616','16762','steve');
insert into Enrollments_Table values('18','2019-1-1','8:00','1','303100', '1717','35464','Mark');
insert into Enrollments_Table values('19','2019-1-1','4:00','1','303110', '1818','25464','John');
insert into Enrollments_Table values('20','2019-1-1','3:00','1','303120', '1919','15463','Magnus');
insert into Enrollments_Table values('21','2019-1-1','1:30','1','303030', '1010','31564','Mohammad');
select* from Enrollments_Table;






































#Q1
select Company_Name from company_table order by Company_Name asc;
#Q2
select Instructor_FirstName from instructors_table where Company_ID ='1717';
#Q3
SELECT Company_ID,Program_Name, COUNT(*) FROM programs_table GROUP BY  Company_ID;
#Q4
select Program_ID, count(*) from enrollments_table group by Program_ID order by Program_ID ;
#Q5
insert into sessions_table values('11',"eleventh day",'3:30','80','303120','110','2222');
#Q6
select Partcipant_FirstName,Participant_ID,Program_ID from enrollments_table group by Participant_ID ; 
#Q7
select* from programs_table;
select Program_ID,Program_Name,Start_Date,End_date from programs_table where Start_Date and End_date between '2019-01-01' and '2019-01-01';
