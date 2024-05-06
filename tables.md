# Database-Final-Proj
# Tables 5-9

## Learning Objective Table

- This table stores learning objectives. To evaluate a program, learning objectives will need to be met. Each objective has a unqiue code, which we have set to an auto-incrementing integer as the primary key. The objective title is a unique string and has a limit of 120 characters, and there is additionally a description associated with a learning objective.

```
CREATE TABLE IF NOT EXISTS LearningObjective (
            ObjectiveCode INT AUTO_INCREMENT PRIMARY KEY,
            ObjectiveTitle VARCHAR(120) UNIQUE,
            Description VARCHAR(500)
)
```

## LearningObjective_Course Table

- This table allows each course to be associated with at least one learning objective and also that each objective must have at least one course associated with it. 
- The table contains two columns: the learning objective title that can contain 120 characters and a course ID which is unique to a course. 
- The primary key for this table is the combination of LearningObjectiveTitle and CourseID. 
- Foreign Key LearningObjectiveTitle references ObjectiveTitle from the LearningObjective Table
- Foreign Key CourseID references CourseID from the Course Table

```
CREATE TABLE IF NOT EXISTS LearningObjective_Course (
            LearningObjectiveTitle VARCHAR(120),
            CourseID VARCHAR(8),
            PRIMARY KEY (LearningObjectiveTitle, CourseID),
            FOREIGN KEY (LearningObjectiveTitle) REFERENCES LearningObjective(ObjectiveTitle),
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
        )
```

## Section Table

- This table represents a Course section. The table contains a Section ID (a 3 digit number), a Semester (Spring, Summer, Fall), a CourseID (unique to a Course), the number of students within a section and the ID of the instructor that teaches the section. 
- The Primary Key to this table is the combination of SectionID, Semester, CourseID and Year. 
- There is an index set up on SectionID, Semester and Year.
- Foreign Key CourseID references CourseID in the Course Table.
- Foreign Key InstructorID references InstructorID in the Instructor Table.

```
 CREATE TABLE IF NOT EXISTS Section (
            SectionID VARCHAR(3),
            Semester VARCHAR(6),
            Year INT,
            CourseID VARCHAR(8),
            NumStudents INT,
            InstructorID VARCHAR(8),
            PRIMARY KEY (SectionID, Semester, CourseID, Year),
            INDEX section_index (SectionID, Semester, Year),
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
            FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
        )
```

## Evaluation Table

- The Evaluation Table stores evaluations for a program. It has an EvaluationObjective (Learning Objective), a Degree Name, a Degree Level (ex: BS, BA), the number of students with A's, B's C's and F's, an Evaluation Description, an Instrctor ID, a Section ID, a Semester, a year and a Course ID. All of this information is important to fully complete an evaluation. The Primary Key is the combination of SectionID, CourseID and EvalObjective. Foreign Key CourseID references CourseID in Course Table. Foreign Key (SectionID, Semester, Year) references (SectionID, Semester, Year) in Section Table. Foreign Key (DegreeName, DegreeLevel) references (DegreeName, DegreeLevel) in Degree Table. Foreign Key InstructorID references InstructorID in Instructor Table.
```
CREATE TABLE IF NOT EXISTS Evaluation (
            EvalObjective VARCHAR(50),
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(5),
            A INT,
            B INT,
            C INT,
            F INT,
            EvaluationDescription VARCHAR(500),
            InstructorID VARCHAR(8),
            SectionID VARCHAR(3),
            Semester VARCHAR(6),
            Year INT,
            CourseID VARCHAR(8),
            PRIMARY KEY (SectionID, CourseID, EvalObjective), 
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
            FOREIGN KEY (SectionID, Semester, Year) REFERENCES Section(SectionID, Semester, Year), 
            FOREIGN KEY (DegreeName, DegreeLevel) REFERENCES Degree(DegreeName, DegreeLevel),
            FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
        )
```