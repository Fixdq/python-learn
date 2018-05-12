# 1、查询所有的课程的名称以及对应的任课老师姓名
select
  c.cname,
  t.tname
from course c
  join teacher t
    on c.teacher_id = t.tid;

# 2、查询学生表中男女生各有多少人
select
  gender,
  count(*)
from student
group by gender;

# 3、查询物理成绩等于100的学生的姓名
select stu.sname
from student stu
  join score s on stu.sid = s.student_id
where s.num = 100 and s.course_id =
                      (select cid
                       from course
                       where cname = '物理');

# 4、查询平均成绩大于八十分的同学的姓名和平均成绩
select
  stu.sname,
  t2.avgn
from student stu
  join (select
          s.student_id sid,
          avg(s.num)   avgn
        from score s
        group by s.student_id
        having avg(s.num) > 80
       ) as t2
    on stu.sid = t2.sid
;



# 5、查询所有学生的学号，姓名，选课数，总成绩
select
  stu.sid,
  stu.sname,
  t2.counts,
  t2.sums
from student stu
  join
  (select
     s.student_id sid,
     count(course_id) counts,
     sum(num) sums
   from score s
   group by s.student_id) as t2
    on stu.sid = t2.sid

;
# 6、 查询姓李老师的个数
select count(*)
from teacher
where tname like '李%';

# 7、 查询没有报李平老师课的学生姓名
select s.sname
from student s
where s.sid not in (
  select c.student_id
  from score c
  where c.course_id in
        (select cid
         from course
           join teacher t on course.teacher_id = t.tid
         where t.tname = '李平老师'));
# 8、 查询物理课程比生物课程高的学生的学号

select stu.sid
from student stu
  join
  (select
     s.student_id,
     s.num
   from score s
   where s.course_id = (
     select cid
     from course
     where cname = '物理')) as t1 on t1.student_id = stu.sid
  join
  (select
     s.student_id,
     s.num
   from score s
   where s.course_id = (
     select cid
     from course
     where cname = '生物')
  ) as t2 on t2.student_id = stu.sid
where t1.num > t2.num
;

# 9、 查询没有同时选修物理课程和体育课程的学生姓名
select sname
from student
where sid in
      (select student_id
       from score
       where course_id
             in
             (select cid
              from course
              where cname = '物理' or cname = '体育')
       group by student_id
       having COUNT(course_id) = 1);


# 10、查询挂科超过两门(包括两门)的学生姓名和班级

select
  stu.sname,
  c.caption
from student stu
  join class c on stu.class_id = c.cid
where stu.sid in
      (
        select student_id
        from score
        where num < 60
        group by student_id
        having count(course_id) > 1);



# 11 、查询选修了所有课程的学生姓名
select sname
from student
where sid in (
  select student_id
  from score
  group by student_id
  having count(course_id) =
         (select count(*)
          from course)
);
# 12、查询李平老师教的课程的所有成绩记录
select
  s2.sname,
  t1.cname,
  s.num
from score s
  join student s2 on s.student_id = s2.sid
  join

  (select
     cid,
     cname
   from course
     join teacher t on course.teacher_id = t.tid
   where t.tname = '李平老师') as t1
    on s.course_id = t1.cid;


# 13、查询全部学生都选修了的课程号和课程名
select
  cid,
  cname
from course
where cid in
      (select course_id
       from score
       group by score.course_id
       having count(score.student_id) =
              (select count(*)
               from student));


# 14、查询每门课程被选修的次数
select cname,t1.nums
from course
join
(select course_id,count(student_id) as nums
       from score
       group by score.course_id) as t1
on cid = t1.course_id
;
# 15、查询之选修了一门课程的学生姓名和学号

select sname,sid
from student
join
(select student_id
from score
group by student_id
having count(course_id) =1)
as t1
on sid = t1.student_id
;

# 16、查询所有学生考出的成绩并按从高到低排序（成绩去重）

select
  distinct num
from score
order by num DESC ;

# 17、查询平均成绩大于85的学生姓名和平均成绩
select sname,t1.avgn
from student stu
join
(select student_id,avg(num) avgn from score
group by student_id
having avg(num)>85) as t1
on stu.sid = t1.student_id;

# 18、查询生物成绩不及格的学生姓名和对应生物分数

select sname,t1.num
from student
join
  (select student_id,num
from score
where course_id =
      (select cid
       from course
       where cname = '生物')and num <60) as t1
on t1.student_id = sid
;

# 19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名

select sname
from student
where sid =
      (select student_id
       from score
       where course_id in

             (select cid
              from course
              where teacher_id = (select tid
                                  from teacher
                                  where teacher.tname = '李平老师'))
       group by student_id
       order by avg(num) desc
       limit 1);




# 20、查询每门课程成绩最好的前两名学生姓名

select
  cc.student_id,
  cc.course_id,
  cc.num
from

  (select
     student_id,
     course_id,
     num
   from score
   order by num desc) cc
;
