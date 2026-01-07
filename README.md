# CRMROL

## Overview

**CRMROL** is a management software designed for the structured and centralized handling of customers and contacts.

The web application allows efficient collection, organization, and updating of information, and features an intuitive and flexible interface to simplify daily operations.

---

## Technologies Used

- **HTML**
- **CSS**
- **JavaScript**
- **Python (Flask)**
- **SQLite3**

---

## Features

- View contact by VAT code  
- View account by VAT code  
- Automatic account creation  
- Account details management  
- Contact details management  
- Delete account  
- Delete contact  

---

## Getting Started

### Prerequisites

- Python 3.x installed
- `pip` package manager available

---

## Environment Setup

### Create a Virtual Environment

```bash
mkdir myproject
cd myproject
py -3 -m venv .venv
```

### Activate the Virtual Environment

**Windows**
```bash
.venv\Scripts\activate
```

---

## Install Flask

```bash
pip install Flask
```

---

## Run the Flask Server

**Windows (PowerShell)**
```powershell
$env:FLASK_APP='name_of_the_application_.py'
$env:FLASK_DEBUG=1
flask run
```

---

## Access the Application

Open your browser and navigate to:

```
http://localhost:5000
```

---

## Notes

- Replace `name_of_the_application_.py` with the actual Flask application filename.
- Debug mode is enabled for development purposes only.
