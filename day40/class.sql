
create database db_test;
use db_test;
create table userinfo
(id int primary key auto_increment,
name char(16) not null ,
password char(20) not null
);

insert into userinfo(name,password)
values
('fixd','123'),
('kitty','456');

select * from userinfo;