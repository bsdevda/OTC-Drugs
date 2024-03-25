# OTC Drugs

### TABLE OF CONTENTS
1. About
2. Git
3. UML
4. Requirement Engineering
5. Analysis
6. DDD - Domain Driven Design
7. Metrics
8. Clean Code Development
9. Build Management
10. Unit Tests
11. IDE
12. Functional Programming


## 1. Project Summary

This Flask-based project aims to make it easier to sell medical goods. It has basic functionality, including a homepage, catalog page, and checkout page. The goal of the project and its essential elements are summarized below.

## 2. Git
The git version history for the project: [click here](https://github.com/bsdevda/OTC-Drugs/commits/main/?before=5318dc60090c4c5b315af21572cad407c4858575+35)

## 1. UML Diagram
UML Diagrams created with Lucid:
 - Dynamic: [Activity Diagram](https://github.com/bsdevda/OTC-Drugs/blob/main/UMLs/Activity%20diagram.png)
 - Static: [Class Diagram](https://github.com/bsdevda/OTC-Drugs/blob/main/UMLs/UML%20class.png) and [Use Case Diagram](https://github.com/bsdevda/OTC-Drugs/blob/main/UMLs/Use%20Case.png)

## Requirements Engineering
Two types of requirements engineering were performed for this project. Please find the following link for your reference:
 - [Self-made](https://www.notion.so/Requirements-Engineering-d8e730a826de41e0b3b26fdb6cde1cbf?pvs=4)
 - [Jira]() 

## Analysis

 - Analysis Link - https://github.com/bsdevda/OTC-Drugs/blob/main/Analysis/Analysis.pdf

## DDD
 - Event Storming Diagram: ![Event Storming](https://github.com/bsdevda/OTC-Drugs/blob/main/ddd/ddd.jpg)
 - Core Domain Chart: ![Core Domain](https://github.com/bsdevda/OTC-Drugs/blob/main/ddd/ddd2.jpg)

## Metrics

 - SonarQube Link - https://github.com/bsdevda/OTC-Drugs/tree/main/Metrics

## CLEAN CODE DEVELOPMENT
The code follows clean code development techniques by using meaningful variable names, explicit function operations, and a modular structure. It also uses input validation for user registration and cart management, promoting robustness while maintaining a high degree of code readability.

## BUILD MANAGEMENT

## UNIT TESTS

## IDE
Since that project is a web application I used a simple code editor: "Visual Studio Code". It is very convenient for debugging web applications and offers many features that I used for my project.
Some of the features I used for the development of the project:
 - Live server
 - Autofill HTML
 - Inbuilt file explorer
Some of my favorite shortcuts are:
 - ```Ctrl+F``` (Find in code)
 - ```Ctrl+Z``` (To Undo)
 - ```Ctrl+Alt+O``` (Open code with live server)

## FUNCTIONAL PROGRAMMING


## Advantages

### Main Page

The homepage is the first point of contact for users and acts as an introduction to your medical supplies store. Key characteristics include:

- Display of popular or prominent medical products.
- General information about the mission or goal of the store.
- Access to the catalog page.

### Catalog Page

The catalog page offers a list of medical supplies that are currently available. It allows users to do the following:

- Look through a variety of medical products.
- Search and filter for certain things.
- View product information and photographs in detail.

### Page of Checkout

Users can complete their purchases on the checkout page. It includes:

- A simple shopping cart for reviewing selected items.
- The option to input shipping and payment details.
- Order confirmation and a receipt.

### User Authentication

Consider introducing user authentication elements such as: improved security and user experience.

- Registration and login for users.
- User profiles that include order history.
- Account management and password recovery.
