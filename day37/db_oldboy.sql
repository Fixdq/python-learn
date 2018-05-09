/*
创建数据库
*/
create database db_oldboy;
use db_oldboy;

/*
创建 表
t_student
t_school
t_course
t_choose_course
*/
create table t_student(
id int not null primary key auto_increment,
name varchar(20) not null,
password varchar(50) not null,
age int(3) not null
);

create table t_school(
id int not null primary key auto_increment,
name varchar(50) not null,
address varchar(255) not null
);

create table t_course(
id int not null primary key auto_increment,
name varchar(20) not null,
price int(5) not null,
period int(2) not null,
school int not null,
constraint fk_school foreign key(school)  /*添加学校的外键*/
references t_school(id)
);

create table t_choose_course(
id int not null primary key auto_increment,
id_student int not null,
id_course int not null,
constraint fk_student foreign key(id_student)  /*添加学生的外键*/
references t_student(id),
constraint fk_course foreign key(id_course)  /*添加课程的外键*/
references t_course(id)
);

/*
插入数据
*/
insert into 
db_oldboy.t_student(name,password,age) 
values 
('张三','123',20),
('李四','111',18)
;

insert into 
db_oldboy.t_school(name,address)
values 
('oldboyBeijing','北京昌平'),
('oldboyShanghai','上海浦东')
;

insert into 
db_oldboy.t_course(name,price,period,school)
values 
('Python全栈开发一期',20000,5,2),
('Linux运维一期',200,2,2),
('Python全栈开发20期',20000,5,1)
;

insert into 
db_oldboy.t_choose_course(id_student,id_course)
values 
(1,1),
(2,2)
;


/*
显示表结构
*/
desc t_student;
desc t_school;
desc t_course;
desc t_choose_course;

/*
查询信息
*/
select name from t_course where school = 1;

select name from t_course where school = 2;

select name from t_student where age>19;

select name from t_course where period>4;










