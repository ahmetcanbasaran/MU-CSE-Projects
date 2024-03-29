/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [BranchCode]
      ,[BranchName]
      ,[DepartmentID]
  FROM [DATABASE_OF_GATEM].[dbo].[BRANCH]

  go

  CREATE PROCEDURE SHOW_LESSONS_OF_STUDENTS @stID int
	AS
	SELECT rs.StudentID,rs.ClassCode,l.LessonName,(t.fName +' '+t.lName) as TeacherName
   FROM REGULAR_STUDENT rs,TEACHER_CLASS_LESSON tcl,LESSON l,TEACHER t
   WHERE rs.ClassCode=tcl.ClassCode AND tcl.TeacherID=t.ID
   AND l.LessonCode=tcl.LessonCode AND rs.StudentID=@stID
   go


   CREATE PROCEDURE SHOW_STUDENTS_TO_TEACHER @tID int,@lessonCode varchar(10)
 AS
 SELECT rs.*,c.ClassroomName
   FROM REGULAR_STUDENT rs,TEACHER_CLASS_LESSON tcl,CLASSROOM c
   WHERE rs.ClassCode=tcl.ClassCode AND tcl.TeacherID=@tID AND tcl.LessonCode=@lessonCode
     AND c.ClassroomCode=tcl.ClassroomCode

	 go

	 CREATE PROCEDURE ITEM_BORROW_SYSTEM @stID int,@matID VARCHAR(50),@lim smallint,@mode bit
 AS
 DECLARE @date SMALLDATETIME
 DECLARE @amount int
 DECLARE @val int
 SELECT @amount=RepositoryAmount
 FROM MATERIAL
 WHERE ProductCode=@matID
 if(@mode=1)
   BEGIN
     SELECT @val=StudentID FROM STUDENT_MATERIAL
     WHERE StudentID=@stID AND MaterialID=@matID
   END
 SET @date = GETDATE()
     if(substring(@matID,1,3)='253' AND @amount>0 AND @mode=0)
         BEGIN
           INSERT INTO STUDENT_MATERIAL
           VALUES(@stID,@matID,@date,DATEADD(DAY,@lim,@date))
           UPDATE MATERIAL
             SET RepositoryAmount-=1
           WHERE ProductCode=@matID
         END
     --else if(@mode=0)
       --BEGIN
         --RAISERROR(15600,-1,-1,'ITEM IS NOT AVAILABLE')
       --END
     if(@mode=1 AND @val is NOT NULL)
         BEGIN
           DELETE FROM STUDENT_MATERIAL
           WHERE StudentID=@stID AND MaterialID=@matID
           UPDATE MATERIAL
             SET RepositoryAmount+=1
           WHERE ProductCode=@matID
         END

EXEC ITEM_BORROW_SYSTEM 13018,'253.2.3.1.2-11',3,0