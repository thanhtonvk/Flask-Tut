use master
go
create database Flask_TUT
go
use Flask_TUT
go
create table Account(
	Username char(10) primary key,
	Password char(10) not null,
	Address nvarchar(50) not null,
	Email nvarchar(50) not null
)
go
create proc login_account @username char(10), @password char(10)
as
begin
	select * from Account where Username = @username and Password = @password
end

go


create table Student(
Id int identity(1000,1) primary key,
[Name] nvarchar(50) not null,
DateOfBirth date,
[Address] nvarchar(50)
)

go
create proc get_all_student
as
begin
	select * from Student
end
go


--get student by id
create proc get_student_by_id @id int
as
begin
select * from Student where Id = @id
end
go


---insert
create proc insert_student @name nvarchar(50), @dateofbirth date, @address nvarchar(50)
as
begin
	insert into Student([Name],DateOfBirth,[Address]) values (@name,@dateofbirth,@address)
end
go

--update
create  proc update_student @id int, @name nvarchar(50), @dateofbirth date, @address nvarchar(50)
as
begin
	update Student set Name = @name, DateOfBirth = @dateofbirth, Address = @address where Id =@id
end
go

create proc delete_student @id int
as
begin
delete from Student where id = @id
end

select * from Student



