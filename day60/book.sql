create database book_db;
create table book (
id int primary key auto_increment,
book_name varchar(255) not null,
press_id int not null
);

create table author(
id int primary key auto_increment,
name varchar(100) not null
);

create table press(
id int primary key auto_increment,
name varchar(100) not null ,
address varchar (255) not null
);
create table book2author(
id int primary key auto_increment,
book_id int,
author_id int
)