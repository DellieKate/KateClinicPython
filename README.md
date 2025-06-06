##__*Python Assessment*__

# **Project Title**
KLM Clinic Patient Registry

## **Description**
- An app designed to sort patients' details and recommended laboratory tests in a clinic setting

### **Features:**
    1. Input basic patient details (reception interface). 
    2. Look up patient’s files and recommends laboratory tests based on age and sex (doctor’s interface). 
    3. Print patient’s records as PDF. 
    4. Export list of patients into a CSV file. 

## **Installation:**

*Prerequisites:*
- Python version 3.13 should be installed. 

*Create a virtual environment (in bash terminal):*
- python -m venv venv
- source venv/bin/activate

*Once in virtual environment, install dependencies:*
- pip install -r requirements.txt

## **Usage:**

1. Run project in terminal. 
    - python3 clinic.py
2. Input options in main menu.
3. In reception interface, follow prompts to enter details. (Note: A patient ID will be generated that will be used for patient look up.) A CSV file is created and be accessed and printed.
4. In doctor interface, search patient using ID. The system will display a report with an option to print as a PDF.

## **Project Structure:**

*Files:*
1. clinic.py 
- main file where options provided help navigate the whole app
2. reception.py
- interface where user inputs patient’s details
- creates CSV file to store all patients details
3. doctor.py
- user can search patient’s ID and displays data with recommended laboratory tests
- generates report printable as a PDF
4. entities.py
- contain entity definitions
5. create_pdf.py
- methods to generate PDF
6. requirements.txt
- lists the required modules and packages to run the app

## **License:**

This app is licensed under the [Apache License 2.0](https://github.com/DellieKate/KateClinicPython/blob/main/LICENSE)

## **References:**
[W3schools](https://www.w3schools.com/python/default.asp)
[Canvas](https://edstem.org/au/courses/23675/lessons)
[Phyton](https://www.python.org/)
