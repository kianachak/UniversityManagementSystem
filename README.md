# University Management System

A simple university management system built with Python using Object-Oriented Programming (OOP).

## What is it?

University Management System is a Python-based application that simulates the basic operations of a university. It manages different university entities, including departments, professors, students, courses, and enrollments.

The project is designed using Object-Oriented Programming principles, with each entity represented by a separate class and organized into individual Python modules. These classes interact with each other to simulate relationships and operations within a university environment.

## Features

- **Departments**
  - Add and remove professors
  - Assign a head professor
  - Manage department students and courses
  - View department information and available courses

- **Professors**
  - Assign professors to courses
  - Set professor availability
  - Assign schedules to courses
  - Approve or reject courses
  - Enter student grades

- **Students**
  - View student information
  - Enroll in approved courses
  - Prevent duplicate active enrollments
  - View enrollment history
  - View active course schedules

- **Courses**
  - Store course information
  - Assign professors and schedules
  - Track course approval status
  - View enrolled students
  - Store course rejection reasons

- **Enrollments**
  - Track student course enrollments
  - Store semester and grade information
  - Manage enrollment statuses (Enrolled, Completed, Dropped, Failed)
  - Update enrollment status based on student grades

## What I Learned

- Understanding and applying Object-Oriented Programming principles
- Designing classes and creating objects
- Organizing a Python project into multiple modules
- Working with object attributes and instance methods
- Managing relationships between different classes and objects
- Using object references to connect related entities
- Implementing one-to-many relationships between objects
- Working with lists to manage collections of objects
- Using conditional logic to control application behavior
- Handling object interactions across multiple Python modules
- Implementing basic validation and preventing duplicate operations
- Testing class methods and interactions between objects

## How to Run

To run University Management System, make sure Python is installed on your system and run:

```bash
python main.py
```

## Example

```text
================================
   University Management System
================================

Department: Computer Engineering
Head Professor: Dr. Smith

Professors:
- Dr. Smith
- Dr. Johnson

Students:
- Alice
- Bob

Courses:
- Introduction to Programming
- Data Structures

================================
Course Approval
================================

Course: Introduction to Programming
Professor: Dr. Johnson
Schedule: Saturday 10:00-12:00

Course approved.

================================
Student Enrollment
================================

Student: Alice
Course: Introduction to Programming
Semester: 7

Enrollment successful.
```