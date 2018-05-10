create database day38;
use day38;
/*
1 创建用户表 id，username,password
    id为自增且唯一约束
    username和password为主键
*/
create table user(
  id int not null unique auto_increment,
  username char(20) not null ,
  password char(50) not null ,
  primary key (username,password)
);


/*
2 插入三条数据，root ，123
                egon，456
                lqz，678
*/
insert into user
(username,password)
values
('root','123'),
('egon','456'),
('lqz','678')
;

/*
#用户组表
*/

create table usergroup(
  id int primary key auto_increment,
  groupname char(20) not null unique
);
/*
插入数据
*/
insert into usergroup
(groupname)
values
('IT部门'),
('销售部门'),
('财务部门'),
('总经理')
;


/*
5 创建主机表：id，ip
            id自增，主键
            ip唯一约束不为空，默认为127.0.0.1

*/

create table host(
  id int primary key auto_increment,
  ip char(15) not null unique default '127.0.0.1'
);

/*
插入数据
*/

insert into host
(ip)
values
('172.16.45.2'),
('172.16.31.10'),
('172.16.45.3'),
('172.16.31.11'),
('172.10.45.3'),
('172.10.45.4'),
('172.10.45.5'),
('192.168.1.20'),
('192.168.1.21'),
('192.168.1.22'),
('192.168.2.23'),
('192.168.2.223'),
('192.168.2.24'),
('192.168.3.22'),
('192.168.3.23'),
('192.168.3.24')
;

/*
创建业务表

*/
create table business(
  id int primary key auto_increment,
  business char(20) not null unique
);

/*
插入数据
*/

insert into business
(business)
values
('轻松贷'),
('随便花'),
('大富翁'),
('穷一生')
;



/*
关系表 user2usergroup
自行关联，外键约束
*/


create table user2usergroup(
  id int not null unique auto_increment,
  user_id int not null ,
  usergroup_id int not null ,
  primary key (user_id,usergroup_id),
  foreign key(user_id) references user(id),
  foreign key(usergroup_id) references usergroup(id)
);
/*
插入数据
*/
insert into user2usergroup
(user_id,usergroup_id)
values
(1,1),
(1,2),
(1,3),
(1,4),
(2,3),
(2,4),
(3,4)
;


/*
11 建关系：host与business
（自行关联，外键约束）
*/
create table host2business(
id int not null unique auto_increment,
host_id int not null ,
business_id int not null ,
primary key (host_id,business_id),
foreign key (host_id) references host(id),
foreign key (business_id) references business(id)
);
/*
插入数据
*/
insert into host2business
(host_id, business_id)
values
(1,1),
(1,2),
(1,3),
(2,2),
(2,3),
(3,4)
;


/*
13 建关系：user与host
（自行关联，外键约束）
*/

create table user2host(
  id int not null unique auto_increment,
  user_id int not null ,
  host_id int not null ,
  primary key (user_id,host_id),
  foreign key (user_id) references user(id),
  foreign key (host_id) references host(id)
);

/*
插入数据
*/

insert into user2host
(user_id,host_id)
values
(1,1),
(1,4),
(1,15),
(1,16),
(2,2),
(2,3),
(2,4),
(2,5),
(3,10),
(3,11),
(3,12)
;

desc user;
desc usergroup;
desc business;
desc host;
desc user2host;
desc user2usergroup;
desc host2business;
select * from user;
select * from usergroup;
select * from business;
select * from host;
select * from user2usergroup;
select * from user2host;
select * from host2business;





