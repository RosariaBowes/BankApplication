# Rosaria Banking – Secure Online Banking Web Application

## Overview

Rosaria Banking is a full-stack web application developed as part of my university studies to simulate a modern online banking system. The application allows users to register, securely log in, manage their accounts, transfer funds, make deposits, view transaction history, manage payment cards, and update their profile through a responsive web interface.

The project was designed to demonstrate backend development, database management, authentication, secure transaction handling, and modern front-end design using Python and Flask.

---

## Features

### Public Website

* Responsive landing page
* About page
* Banking services page
* Contact page
* Responsive navigation
* Modern banking branding
* Light and dark mode support

### User Dashboard

Authenticated users can:

* Securely log in and log out
* View account balance
* View account details
* Transfer money between accounts
* Deposit funds
* View transaction history
* Manage bank cards
* View payment history
* Recharge mobile balance
* View exchange rates
* Update profile information
* Toggle between light and dark mode

---

## Technologies Used

### Backend

* Python 3
* Flask
* Flask Sessions
* SQL Database
* Jinja2 Templates

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript
* Font Awesome

### Database

The application stores:

* User information
* Bank accounts
* Transactions
* Payment cards
* Deposits
* Transfers
* Profile information

---

## Project Structure


app/
│
├── routes/
│   ├── root/
│   └── user/
│
├── templates/
│   ├── root/
│   └── user/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── database/
│
└── app.py


---

## Key Functionality

### Authentication

Users are required to register before accessing online banking features. Secure sessions are used to protect authenticated pages and prevent unauthorised access.

### Account Management

Each user can manage their banking information through a personalised dashboard displaying balances, account details and recent activity.

### Transactions

The application supports:

* Deposits
* Transfers
* Payment history
* Transaction history

Each transaction updates the database and records a history entry for auditing purposes.

### Card Management

Users can view their virtual debit card within the banking portal. The project includes a custom-designed Rosaria Banking card matching the application's branding.

### User Experience

The interface was redesigned using a consistent navy, gold and white colour palette to create a modern banking experience. Components were styled to provide consistency across public pages and authenticated dashboard pages.

---

## Security Features

* Password authentication
* Protected routes
* Session management
* Input validation
* Database-backed user accounts

---

## Skills Demonstrated

This project demonstrates knowledge of:

* Full-stack web development
* Python programming
* Flask framework
* Relational databases
* SQL queries
* CRUD operations
* Authentication and session management
* Transaction processing
* Responsive web design
* UI/UX design principles
* Version control using Git
* Software debugging and testing

---

## Future Improvements

Potential future enhancements include:

* REST API implementation
* Two-factor authentication (2FA)
* Email verification
* Password reset functionality
* Real-time notifications
* Admin dashboard
* Advanced fraud detection
* Currency conversion API integration
* Open Banking API integration

---

## Learning Outcomes

Developing Rosaria Banking significantly improved my understanding of modern web application development. Throughout the project I gained practical experience in designing relational databases, implementing secure authentication, managing financial transactions, debugging full-stack applications, and creating a consistent user interface.

The project also strengthened my software engineering skills through iterative development, code refactoring, problem solving, and applying user-centred design principles to create a professional banking application.

---

## Author

**Rosaria Bowes**

