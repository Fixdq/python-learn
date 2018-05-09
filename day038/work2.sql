create database db_school;
use db_school;

create table class(
  cid int primary key auto_increment,
  caption char(20) not null
);

insert into class
(caption)
values
('三年二班'),
('一年三班'),
('三年一班')
;

create table student(
  sid int primary key auto_increment,
  sname char(16) not null ,
  gender enum('男','女') not null default '男',
  class_id int not null ,
  foreign key (class_id) references class(cid)
);

create table teacher(
  tid int primary key auto_increment,
  tname char(16) not null
);
create table course(
  cid int primary key auto_increment,
  cname char(20) not null ,
  teacher_id int not null ,
  foreign key (teacher_id) references teacher(tid)
);
create table scoure(
  sid int primary key auto_increment,
  student_id int not null ,
  course_id int not null ,
  number int not null ,
  foreign key (student_id) references student(sid),
  foreign key (course_id) references course(cid)
);

insert into student
(sname,gender,class_id)
values
('钢弹','女',1),
('铁锤','女',1),
('山炮','男',2)
;


insert into teacher
(tname)
values
('剥夺'),
('苍龙'),
('菜刀')
;

insert into course
(cname, teacher_id)
values
('生物',1),
('体育',1),
('物理',2)
;
insert into scoure
(student_id, course_id, number)
    values
      (1,1,60),
      (1,2,59),
      (2,2,60),
      (3,3,60)
;
