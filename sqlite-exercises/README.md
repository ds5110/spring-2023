
# sqlite

In-class exercises for github classroom

# Setup

To create an environment with Python (sqlite3 is part of the Python standard library)...
```
conda create --name myenv
conda activate myenv
conda install -c conda-forge python
```

To remove this environment
```
conda deactivate
conda remove --name myenv --all
```

To save the environment as a cross-platform compatible ENV.yml file
```
conda env export --from-history>ENV.yml
```

To create an environment from an ENV.yml file
```
conda env create -n ENVNAME --file ENV.yml
```

* [sqlite3](https://docs.python.org/3/library/sqlite3.html) -- python.org
* [conda cheatsheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html) -- conda.io
* [ds5010 conda notes (spring 2023)](https://github.com/ds5010/spring-2023/blob/main/install.md) -- github.com/ds5010
* [ds5010 git notes (spring 2023)](https://github.com/ds5010/spring-2023/blob/main/git.md) -- github.com/ds5010

# Students database

## s0 -- demo exercise

Print all the info in the "student" table

```
make s0

The SQL...
SELECT * FROM student
The result...
0 ('0001', 'John', 'CS', None)
1 ('0002', 'Lucy', 'DS', 4.0)
2 ('0003', 'Aiden', 'CS', 3.33)
```
* If you're starting from scratch, then the student database will be created automatically by the Makefile
* You can also create a copy of the students database by hand (but again, this is unnecessary because of the Makefile)
```
make data/students.db
```
* To remove the database (e.g., so you can start over)
```
make clean
```

## Exercise s1 -- TBD

...
