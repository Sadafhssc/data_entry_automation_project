# Data Entry Automation

## Overview

This project automates a repetitive property data-entry workflow using Python.

The application collects property information from a Zillow-style property listing website, extracts relevant details through web scraping, and automatically enters the collected data into a Google Form using Selenium.

The submitted responses can then be organized and reviewed through Google Sheets.

## Workflow

```text
Property Listings
       |
       v
   Web Scraping
       |
       v
 Property Data
       |
       v
 Browser Automation
       |
       v
  Google Forms
       |
       v
 Google Sheets
```

## Features

* Extracts property listing URLs
* Extracts property addresses
* Extracts property prices
* Parses HTML using BeautifulSoup
* Automates browser interactions with Selenium WebDriver
* Automatically fills Google Form fields
* Submits multiple property records
* Automates repetitive data-entry tasks

## Technologies

* Python
* Requests
* BeautifulSoup
* Selenium WebDriver
* Google Forms
* Google Sheets

## How It Works

### 1. Web Scraping

The application sends an HTTP request to the target property listing page and parses the HTML using BeautifulSoup.

The scraper extracts relevant information including:

* Property address
* Property price
* Property URL

### 2. Data Processing

The extracted property information is stored and organized in Python data structures so it can be mapped to the corresponding Google Form fields.

### 3. Browser Automation

Selenium WebDriver opens the Google Form and locates the required input fields.

The script automatically enters the collected property information into the appropriate fields.

### 4. Form Submission

After completing the form, Selenium submits the response and proceeds to the next form submission.

This process is repeated for multiple property listings without requiring manual data entry.

## Architecture

```text
                    Python Application
                           |
              +------------+------------+
              |                         |
              v                         v
      Requests +                  Selenium
      BeautifulSoup              WebDriver
              |                         |
              v                         v
      Property Listings          Google Forms
              |                         |
              +------------+------------+
                           |
                           v
                     Google Sheets
```

## Project Structure

```text
data_entry_automation_project/
│
└── PythonProject21/
    └── main.py
```

## Project Demonstration

A demonstration of the automation workflow is available on LinkedIn:

[View Project Demo on LinkedIn](https://lnkd.in/p/dNjbgK5P)

The demonstration shows how property listing information can be collected and transferred to a Google Form automatically, reducing repetitive manual data-entry work.


## Learning Outcomes

This project provided practical experience with:

* Web scraping and HTML parsing
* HTTP requests
* Browser automation
* Selenium WebDriver
* Automated form interaction
* Data extraction and transformation
* Repetitive task automation
* Integrating multiple tools into a single workflow

## Use Case

The project demonstrates how repetitive data-entry workflows can be automated by combining web scraping with browser automation.

The same approach can be adapted to other structured data-collection workflows where information needs to be extracted from web pages and transferred into forms or spreadsheets.

## Author

**Sadaf Javed**

Software Engineering Student | MERN Developer | Python & Automation Enthusiast

[GitHub](https://github.com/Sadafhssc) · [LinkedIn](https://www.linkedin.com/in/sadaf-javed/)
