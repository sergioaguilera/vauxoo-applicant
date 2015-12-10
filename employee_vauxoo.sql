-- Your sql code in this file
-- NOTE: Please, don't add sentence to create database in this script file.
--       You can create database locally to test it.
--       Consider add ';' at end sentence.

CREATE TABLE employee (
    id          int primary key,
    first_name  varchar(20),
    last_name   varchar(20)
);

-- 4 empleados a insertar
insert into employee values ('sergio','aguilera',001);
insert into employee values ('manuel','rdz',002);
insert into employee values ('mario','sanchez',003);
insert into employee values ('javier','salas',004);


CREATE TABLE employee_department (
    id          int primary key,
    name        varchar(30),
    description varchar(80),
    id_employee int references employee(id)
);

-- 6 departamentos a insertar

insert into employee_department values (101,'finanzas','dpto de finanzas');
insert into employee_department values (102,'sistemas','dpto de sistemas');
insert into employee_department values (103,'admin','dpto de admin');
insert into employee_department values (104,'comunicacion','dpto de comunicacion');
insert into employee_department values (105,'merca','dpto de merca');
insert into employee_department values (106,'gerencia','dpto de gerencia');

CREATE TABLE employee_hobby (
);

-- ...
