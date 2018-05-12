# 1、查询所有的课程的名称以及对应的任课老师姓名
SELECT
	c.cname,
	t.tname
FROM
	course c
JOIN teacher t ON c.teacher_id = t.tid;

# 2、查询学生表中男女生各有多少人
SELECT
	gender,
	count(*)
FROM
	student
GROUP BY
	gender;

# 3、查询物理成绩等于100的学生的姓名
SELECT
	stu.sname
FROM
	student stu
JOIN score s ON stu.sid = s.student_id
WHERE
	s.num = 100
AND s.course_id = (
	SELECT
		cid
	FROM
		course
	WHERE
		cname = '物理'
);

# 4、查询平均成绩大于八十分的同学的姓名和平均成绩
SELECT
	stu.sname,
	t2.avgn
FROM
	student stu
JOIN (
	SELECT
		s.student_id sid,
		avg(s.num) avgn
	FROM
		score s
	GROUP BY
		s.student_id
	HAVING
		avg(s.num) > 80
) AS t2 ON stu.sid = t2.sid;

# 5、查询所有学生的学号，姓名，选课数，总成绩
SELECT
	stu.sid,
	stu.sname,
	t2.counts,
	t2.sums
FROM
	student stu
JOIN (
	SELECT
		s.student_id sid,
		count(course_id) counts,
		sum(num) sums
	FROM
		score s
	GROUP BY
		s.student_id
) AS t2 ON stu.sid = t2.sid;

# 6、 查询姓李老师的个数
SELECT
	count(*)
FROM
	teacher
WHERE
	tname LIKE '李%';

# 7、 查询没有报李平老师课的学生姓名
SELECT
	s.sname
FROM
	student s
WHERE
	s.sid NOT IN (
		SELECT
			c.student_id
		FROM
			score c
		WHERE
			c.course_id IN (
				SELECT
					cid
				FROM
					course
				JOIN teacher t ON course.teacher_id = t.tid
				WHERE
					t.tname = '李平老师'
			)
	);

# 8、 查询物理课程比生物课程高的学生的学号
SELECT
	stu.sid
FROM
	student stu
JOIN (
	SELECT
		s.student_id,
		s.num
	FROM
		score s
	WHERE
		s.course_id = (
			SELECT
				cid
			FROM
				course
			WHERE
				cname = '物理'
		)
) AS t1 ON t1.student_id = stu.sid
JOIN (
	SELECT
		s.student_id,
		s.num
	FROM
		score s
	WHERE
		s.course_id = (
			SELECT
				cid
			FROM
				course
			WHERE
				cname = '生物'
		)
) AS t2 ON t2.student_id = stu.sid
WHERE
	t1.num > t2.num;

# 9、 查询没有同时选修物理课程和体育课程的学生姓名
SELECT
	sname
FROM
	student
WHERE
	sid IN (
		SELECT
			student_id
		FROM
			score
		WHERE
			course_id IN (
				SELECT
					cid
				FROM
					course
				WHERE
					cname = '物理'
				OR cname = '体育'
			)
		GROUP BY
			student_id
		HAVING
			COUNT(course_id) = 1
	);

# 10、查询挂科超过两门(包括两门)的学生姓名和班级
SELECT
	stu.sname,
	c.caption
FROM
	student stu
JOIN class c ON stu.class_id = c.cid
WHERE
	stu.sid IN (
		SELECT
			student_id
		FROM
			score
		WHERE
			num < 60
		GROUP BY
			student_id
		HAVING
			count(course_id) > 1
	);

# 11 、查询选修了所有课程的学生姓名
SELECT
	sname
FROM
	student
WHERE
	sid IN (
		SELECT
			student_id
		FROM
			score
		GROUP BY
			student_id
		HAVING
			count(course_id) = (SELECT count(*) FROM course)
	);

# 12、查询李平老师教的课程的所有成绩记录
SELECT
	s2.sname,
	t1.cname,
	s.num
FROM
	score s
JOIN student s2 ON s.student_id = s2.sid
JOIN (
	SELECT
		cid,
		cname
	FROM
		course
	JOIN teacher t ON course.teacher_id = t.tid
	WHERE
		t.tname = '李平老师'
) AS t1 ON s.course_id = t1.cid;

# 13、查询全部学生都选修了的课程号和课程名
SELECT
	cid,
	cname
FROM
	course
WHERE
	cid IN (
		SELECT
			course_id
		FROM
			score
		GROUP BY
			score.course_id
		HAVING
			count(score.student_id) = (SELECT count(*) FROM student)
	);

# 14、查询每门课程被选修的次数
SELECT
	cname,
	t1.nums
FROM
	course
JOIN (
	SELECT
		course_id,
		count(student_id) AS nums
	FROM
		score
	GROUP BY
		score.course_id
) AS t1 ON cid = t1.course_id;

# 15、查询之选修了一门课程的学生姓名和学号
SELECT
	sname,
	sid
FROM
	student
JOIN (
	SELECT
		student_id
	FROM
		score
	GROUP BY
		student_id
	HAVING
		count(course_id) = 1
) AS t1 ON sid = t1.student_id;

# 16、查询所有学生考出的成绩并按从高到低排序（成绩去重）
SELECT DISTINCT
	num
FROM
	score
ORDER BY
	num DESC;

# 17、查询平均成绩大于85的学生姓名和平均成绩
SELECT
	sname,
	t1.avgn
FROM
	student stu
JOIN (
	SELECT
		student_id,
		avg(num) avgn
	FROM
		score
	GROUP BY
		student_id
	HAVING
		avg(num) > 85
) AS t1 ON stu.sid = t1.student_id;

# 18、查询生物成绩不及格的学生姓名和对应生物分数
SELECT
	sname,
	t1.num
FROM
	student
JOIN (
	SELECT
		student_id,
		num
	FROM
		score
	WHERE
		course_id = (
			SELECT
				cid
			FROM
				course
			WHERE
				cname = '生物'
		)
	AND num < 60
) AS t1 ON t1.student_id = sid;

# 19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名
SELECT
	sname
FROM
	student
WHERE
	sid = (
		SELECT
			student_id
		FROM
			score
		WHERE
			course_id IN (
				SELECT
					cid
				FROM
					course
				WHERE
					teacher_id = (
						SELECT
							tid
						FROM
							teacher
						WHERE
							teacher.tname = '李平老师'
					)
			)
		GROUP BY
			student_id
		ORDER BY
			avg(num) DESC
		LIMIT 1
	);

# 20、查询每门课程成绩最好的前两名学生姓名


SELECT
	cc.student_id,
	cc.course_id,
	cc.num
FROM
	(
		SELECT
			student_id,
			course_id,
			num
		FROM
			score
		ORDER BY
			num DESC
	) cc;

