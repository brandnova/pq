# PQ @ Delsu
An online platform where students can access tons of study materials like past questions, textbooks, and other study materials in PDF format.

# Django Installation and Setup Guide

This guide will walk you through the process of installing and running this scripts on your local PC.

## Prerequisites

Before you begin, ensure that you have the following installed on your system:

- Python (version 3.6 or higher)
- pip (Python package manager - Usually comes with Python)

## Installation Steps

1. **Create a Virtual Environment**: It's recommended to create a virtual environment to manage the project dependencies. Open your terminal or command prompt and run the following command:
   ```
   python -m venv myenv
   ```
   Replace `myenv` with the name you want to give to your virtual environment.

2. **Activate the Virtual Environment**: Navigate to the directory where you created your virtual environment and activate it. Run the following command:
   - On Windows:
     ```
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source myenv/bin/activate
     ```

3. **Install Django**: Once your virtual environment is activated, use pip to install Django. Run the following command:
   ```
   pip install django
   ```

## Running the Django Scripts

Now that you have Django installed, you now run the Django scripts on your local PC.

1. **Install the project dependencies**: In your terminal, run the following command:
   ```
   pip install -r requirements.txt
   ```
   Replace `myproject` with the name you want to give to your Django project.

2. **Navigate to the Project Directory**: Change into the directory of your Django project:
   ```
   cd PQdelsu
   ```

3. **Run the Development Server**: Start the Django development server by running the following command:
   ```
   python manage.py runserver
   ```

4. **Access the Local Development Server**: Once the server is running, open your web browser and navigate to `http://127.0.0.1:8000/` or `http://localhost:8000/` to view the Django project.

## Additional Resources

- [Project Sample](https://app.coursearena.com.ng): Viewa live sample of the project.
- [My portfolio](https://brandnova.github.io): Visit my portfolio website to contact me.

---
