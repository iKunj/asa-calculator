# Table of Contents
- [Intro](#intro)
- [About](#about)
   - Technologies Used
   - Additional Featues
- [Installation & Execution](#installation--execution)
- [File Structure](#file-structure)

# Intro
In a biological context, it's often interesting to understand the molecular interfaces that exist within a protein structure. A molecular interface is a surface region of a protein that interacts with other molecules.

# About
This applications helps with calculation of the solvent accessible surface area (ASA) of a protein molecule before and after interaction with another molecule.

To achieve this, we make use of
1. React (For Frontend)
2. FastAPI (For backend)
3. RCSB PDB API (For access of information)

Additionally, I have added features like
1. Rouding of "Change in ASA" value.
2. Added Round value i.e. upto which decimal point.
3. Responsive Layouts.
4. Searching within the table across all the rows and columns.
5. Pagination of table to show limited entries along with options to change the number of entries.
6. Added CORS for unwanted access protection.
> Rouding of values is **Disabled** by default.

# Installation & Execution

Before installation make sure you have python3 & pip installed on your system. If not visit
1. https://www.python.org/downloads/
2. https://pip.pypa.io/en/stable/installation/

In Terminal 1:

```
$ pip install -r requirements.txt
$ cd backend
$ python3 main.py
```
> Optionally, execute **sh execute_fastapi.sh** to achieve the same.

In Terminal 2:
```
$ cd frontend/asa-change-monitor
$ npm install
$ npm start
```
> Optionally, execute **sh execute_react.sh** to achieve the same.

> **Note:** Without installing the **Dependencies**, the application will not behave as intended.


# File Structure
```
.
├── Readme.md
├── backend
│   ├── app
│   │   ├── api.py
│   │   ├── data.json
│   │   └── helper.py
│   └── main.py
├── frontend
│   └── asa-change-monitor
│       ├── package-lock.json
│       ├── package.json
│       ├── public
│       │   ├── favicon.ico
│       │   ├── index.html
│       │   ├── logo192.png
│       │   ├── logo512.png
│       │   ├── manifest.json
│       │   └── robots.txt
│       └── src
│           ├── App.css
│           ├── App.js
│           ├── App.test.js
│           ├── Tables.js
│           ├── index.css
│           ├── index.js
│           ├── logo.svg
│           ├── reportWebVitals.js
│           └── setupTests.js
└── requirements.txt
```