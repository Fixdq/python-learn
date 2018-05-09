create database db_home;

use db_home;
/*第一题*/
create table shop_info(
id int primary key auto_increment,
name char(16) not null,
production char(255) not null,
count int not null
);

insert into shop_info
(name,production,count) 
values
('A','甲',2),
('B','乙',4),
('C','丙',1)
;

select name from shop_info where count >=2;
select production from shop_info where count =2;
select name from shop_info where count =4;
update shop_info set count = 10 where name = 'A';
delete from shop_info where count = 1;

/*第二题*/
create table student1(
id int primary key auto_increment,
name char(16) not null,
course char(50) not null,
score int not null
);

insert into student1
(name,course,score)
values
('张三','语文',81),
('李四','语文',90),
('王五','语文',49)
;

select name from student1 where score >= 60;
select name from student1 where score >=90;
select name,course from student1 where score = 49;
update student1 set score=60 where name = '王五';
delete from student1 where name = '李四';

select * from student1;

/*第三题*/
create table student2(
id int primary key auto_increment,
name char(16) not null,
password char(128) not null,
age int not null,
reg_time datetime not null,
weight float not null
);

insert into student2
(name,password,age,reg_time,weight)
values
('fixd','123456er789',18,now(),65.5),
('fixd2','12d345678df9',28,now(),67.5),
('fixd3','1234d5678d9',38,now(),68.5),
('fixd4','12345dfff6789',48,now(),85.5)
;


select * from student2;









