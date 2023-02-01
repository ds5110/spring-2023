# Recreate the student/course/enrolled database with primary-key constraints
# This script throws an error because primary keys aren't unique in data

import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()

cur.execute("CREATE TABLE student (sid text, name text, major text, gpa real, primary key(sid))")
cur.execute("CREATE TABLE course (crn text, course text, dept text, term text, primary key(crn))")
cur.execute("CREATE TABLE enrolled (sid text, crn text, grade text)")

cur.execute('''INSERT INTO student
  (sid, name, major, gpa) VALUES
  ('0001', 'John', 'CS', NULL),
  ('0002', 'Lucy', 'DS', 4.00),
  ('0003', 'Aiden', 'CS', 3.33),
  ('0003', 'Jill', 'CS', 3.8)''')

cur.execute('''INSERT INTO course
  (crn, course, dept, term) VALUES
  ('00234', 'Intro CS', 'CS', 'Fall2020'),
  ('00653', 'Intro DS', 'CS', 'Fall2020'),
  ('00783', 'Algorithms', 'CS', 'Fall2020'),
  ('01945', 'ML & AI', 'EE', 'Spring2021')''')

cur.execute('''INSERT INTO enrolled
  (sid, crn, grade) VALUES
  ('0002', '00653', 'A'),
  ('0002', '01945', NULL),
  ('0003', '00783', 'B+')''')

con.commit()
con.close()
