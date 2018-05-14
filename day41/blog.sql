-- 创建视图
create view teacher2course as
  select *
  from teacher
    join course
      on teacher.tid = course.teacher_id;

-- 使用视图 就是把视图当做一张表去使用
select *
from teacher2course;

-- 修改视图
-- 语法：ALTER VIEW 视图名称 AS SQL语句
alter view teacher2course as
  select *
  from teacher
    join course
      on teacher.tid = course.teacher_id
  where teacher.tid > 2;

-- 删除视图
drop view teacher2course;

-- ------触发器
CREATE TABLE cmd (
  id       INT PRIMARY KEY auto_increment,
  USER     CHAR(32),
  priv     CHAR(10),
  cmd      CHAR(64),
  sub_time datetime, #提交时间
  success  enum ('yes', 'no') #0代表执行失败
);


CREATE TABLE errlog (
  id       INT PRIMARY KEY auto_increment,
  err_cmd  CHAR(64),
  err_time datetime
);

-- 创建触发器
delimiter //
create trigger tri_after_insert_cmd after insert on cmd for each row
begin
  if NEW.success ='no' then
    insert into errlog(err_cmd, err_time) VALUES (NEW.cmd,NEW.sub_time);
  end if;
end //
delimiter ;
-- 使用触发器
-- 触发器无法有用户直接调用，而是由对表的【增、删、改】操作被动触发
-- 删除触发器
drop trigger tri_after_insert_cmd;

-- 测试向cmd表中插入数据
insert into cmd (USER, priv, cmd, sub_time, success)
  value ('fixd', '0755', 'ls -l /etc', NOW(), 'yes'),
  ('fixd', '0755', 'cat /etc/passwd', NOW(), 'no'),
  ('fixd', '0755', 'useradd xxx', NOW(), 'no'),
  ('fixd', '0755', 'ps aux', NOW(), 'yes');

-- 查询
select * from cmd;
select * from errlog;


-- --------------------------------------

create table user(
  id int primary key auto_increment,
  name char(32),
  balance int
);

insert into user (name, balance)
values
  ('wsb', 1000),
  ('fixd', 1000),
  ('ysb', 1000);

-- ----事务的使用
drop procedure if exists t_update;   -- 如果事务存在 删除
delimiter //
CREATE procedure t_update()         -- 创建  t_update()事务
  begin -- 开始
    -- 声明变量
    declare t_error integer;
    -- 捕获异常  有异常  t_error = 1
    declare continue HANDLER for sqlexception set t_error = 1;

    start transaction;

    update user
    set balance = 900
    where name = 'wsb'; #买支付100元
    update user
    set balance = 1010
    where name = 'fixd'; #中介拿走10元
    update user
    set balance = 1090
    where name = 'ysb'; #卖家拿到90元
    -- 如果 t_error = 1  rollback   执行回滚操作
    if t_error = 1 then
      rollback ;
    else
    -- 没错误  就直接commit
      commit ;
    end if ;
  end // -- 结束
delimiter ;
call t_update();

-- 创建事务
drop procedure if exists t_update;
delimiter //
create procedure t_update()
  begin
    declare exit handler for sqlexception rollback ;
    start transaction ;
    update user
    set balance = 900
    where name = 'wsb'; #买支付100元
    update user
    set balance = 1010
    where name = 'fixd'; #中介拿走10元
    update user
    set balance = 1090
    where name = 'ysb'; #卖家拿到90元
    commit ;
  end //
delimiter ;
call t_update();

