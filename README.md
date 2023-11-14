# HirePhD-Event hosting platform comparison: LinkedIn Vs Eventbrite
HirePhD conduct frequent event for career enhancement, knowledge transfer for PhD graduates. These events were advertised in linkedin initially and eventbrite later. The purpose of this project is to analyse the participants turnover when the event is advertised in either of the two platforms. 
# Event Platform Comparison Project

## Overview
This project aims to provide a comprehensive comparison between two popular event hosting platforms: LinkedIn Events and Eventbrite. The goal is to help make informed decisions when choosing a platform for hosting their events.

## Introduction

In the age of digital networking and event management, choosing the right platform is crucial for the success of your events. This project explores the strengths and weaknesses of two major event hosting platforms, LinkedIn Events and Eventbrite. By comparing various aspects such as user interface, customization options, audience reach, and analytics, we aim to assist users in making an informed decision based on their specific needs. In this instance we are comparing the 2 platforms for user turnaround statistics. 
## Features

**User Interfac:** A visual comparison of the user interfaces of LinkedIn Events and Eventbrite.
**Dataset:** The data comprised of headers enlisted below, each column representing [ Order ID, Order Date....Any particular career path you'd like to hear more about?]
**The data comprised of the following head:**
'Order ID', 'Order Date', 'Attendee Status', 'First Name', 'Last Name', 'Email', 'Event Name', 'Ticket Quantity', 'Ticket Type', 'Ticket Price', 'Buyer First Name', 'Buyer Last Name', 'Buyer Email', 'Order #', 'Prefix', 'Quantity', 'Order Type', 'Total Paid', 'Eventbrite Fees', 'Eventbrite Payment Processing', 'Which of the following best describes you?', 'Do you agree to be contacted by recruiters?', 'Do you agree to receive future events and news from the event organizers?', 'Do you agree to receive news from the event partner(s)?', "Any question you'd like to ask the speaker?", 'Could we follow up with you through email?', 'Billing Address 1', 'Billing Address 2', 'Billing City', 'Billing State', 'Billing Zip', 'Billing Country', 'Job Title', 'Company', 'ID', 'Attendee #', 'Currency', 'Fees Paid', 'Type', 'Questions', 'Suggestion', 'Mailing_list', 'Recruiter_contact', 'Any question you’d like to ask the speaker?', 'Price Tier', 'Group', 'Home Address 1', 'Home Address 2', 'Home City', 'Home State', 'Home Zip', 'Home Country', 'Name', 'Buyer Name', 'If you have a question prepared for the event, please type here. ', 'Cell Phone', 'Would you like to join HirePhD Slack peer support community?', 'Event ID', "Any questions you'd like to ask the presenter?", "Any particular career path you'd like to hear more about?", 'By signing up for the event, you agree to receive future events and news from the event organizers.', 'Do you agree to be contacted by recruiters? ', "Any questions you'd like to ask the presenter? ", 'Which of the following best describes you? ', "Any particular career path you'd like to hear more about? "

**Steps**
#Data Cleaning/Wrangling: 
    -Concatenated all the files into a single file
    -Replaced NA with 0
    -Checked for duplicates across rows and columns and removed if any
    -Changed the datestamp format throughout the 'Order Date' column to maintain a similar datetime datatype
    
#Data View:
    -Checked for total number of rows/user
#Data Analysis:
    - Calculated the max and min date/or range of date in the list
    - Counted the candidates spanning a specific date - to separate the data into the two groups-Linkedin hosted and Eventbrite hosted
    - (Calculated the total amount collected during the 2 events)
    - Calculated the maximum and minimum amount spent by users.

**Installation**


