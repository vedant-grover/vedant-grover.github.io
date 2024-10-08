from pywebio import input, output, start_server
from pywebio.session import go_app

# Sample data
student_data = {
    "Grover": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Juneja": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Beamer": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Nguyen": {"dues": 299.27, "status": "Regular", "reqs": "No"},
    "Chabbriaa": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Sutton": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Radu": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Ghai": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Thapar": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Hassan": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Kaushik": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Smith": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Thrasher": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Khurana": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Morlet": {"dues": 299.27, "status": "Regular", "reqs": "No"},
    "Budhiraja": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Shah": {"dues": 299.27, "status": "Regular", "reqs": "No"},
    "Liu": {"dues": 299.27, "status": "Regular", "reqs": "Yes"},
    "Clayton": {"dues": 399.27, "status": "RIB", "reqs": "Yes"},
    "Wolf": {"dues": 399.27, "status": "RIB", "reqs": "Yes"},
    "Jar": {"dues": 205.59, "status": "Regular", "reqs": "Yes"},
    "Ruhil": {"dues": 205.59, "status": "Regular", "reqs": "Yes"},
    "Devine": {"dues": 205.59, "status": "Regular", "reqs": "Yes"},
    "Chandak": {"dues": 205.59, "status": "Regular", "reqs": "No"},
    "Vijhani": {"dues": 205.59, "status": "Regular", "reqs": "No"},
    "Rozario": {"dues": 205.59, "status": "Regular", "reqs": "No"},
    "Kumar": {"dues": 205.59, "status": "Regular", "reqs": "Yes"},
    "Suri": {"dues": 205.59, "status": "Regular", "reqs": "Yes"},
    "Richards": {"dues": 205.59, "status": "Regular", "reqs": "No"},
    "Bekal": {"dues": 205.59, "status": "Regular", "reqs": "No"},
    "Thakar": {"dues": 305.59, "status": "RIB", "reqs": "No"},
    "Wijeweera": {"dues": 305.59, "status": "NIB", "reqs": "Yes"},
}

def main():
    # Input last name
    last_name = input.input("Enter your last name:")

    # Look up the student data
    if last_name in student_data:
        dues = student_data[last_name]["dues"]
        status = student_data[last_name]["status"]
        reqs = student_data[last_name]["reqs"]
        
        # Output the results
        output.put_text(f"Last Name: {last_name}")
        output.put_text(f"Dues Owed: ${dues}")
        output.put_text(f"Chapter Status: {status}")
        output.put_text(f"Reqs: {reqs}")
    else:
        output.put_text("No data found for the entered last name.")

# Run the application
if __name__ == '__main__':
    start_server(main, port=8080)
