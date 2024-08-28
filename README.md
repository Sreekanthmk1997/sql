# Employee Management System

## Project Overview
This is a Django-based Employee Management System. The project provides a simple interface to manage employee records, including adding, updating, viewing, and deleting employee details.

## Features
- Add, update, and delete employee records.
- View all employees in a list format.
- Search employees by name or department.

## Technologies Used
- **Backend:** Django
- **Database:** PostgreSQL (or any other database you are using)
- **Frontend:** HTML, CSS (with optional JavaScript)

## Database Structure

### Employee Table
The `Employee` table consists of the following fields:

| Field Name       | Data Type     | Description                      |
|------------------|---------------|----------------------------------|
| `id`             | Integer (PK)  | Unique identifier for each employee |
| `first_name`     | String        | First name of the employee       |
| `last_name`      | String        | Last name of the employee        |
| `email`          | String        | Email address of the employee    |
| `phone_number`   | String        | Contact number of the employee   |
| `department`     | String        | Department the employee belongs to |
| `position`       | String        | Job title of the employee        |
| `date_hired`     | Date          | Date when the employee was hired |
| `salary`         | Decimal       | Employee's salary                |

## Setup Instructions

### Prerequisites
- Python X.X.X
- Django X.X.X
- PostgreSQL (or other database)

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone <https://github.com/Sreekanthmk1997/sql.git>
