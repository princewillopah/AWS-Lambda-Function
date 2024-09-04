import boto3

# Specify the AWS region
region_name = 'eu-north-1'  # Replace with your AWS region

# Create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb', region_name=region_name)
# Use the DynamoDB object to select our table
table = dynamodb.Table('studentData')


# List of student data to be added
students = [
    {'studentid': '1', 'student_id': '1-1', 'name': 'John Doe', 'class': '10', 'age': 15},
    {'studentid': '2', 'student_id': '2-1', 'name': 'Jane Smith', 'class': '11', 'age': 16},
    {'studentid': '3', 'student_id': '3-1', 'name': 'Alice Johnson', 'class': '12', 'age': 17},
    {'studentid': '4', 'student_id': '4-1', 'name': 'Michael Brown', 'class': '10', 'age': 15},
    {'studentid': '5', 'student_id': '5-1', 'name': 'Emily Davis', 'class': '11', 'age': 16},
    {'studentid': '6', 'student_id': '6-1', 'name': 'Daniel Wilson', 'class': '12', 'age': 17},
    {'studentid': '7', 'student_id': '7-1', 'name': 'Sophia Miller', 'class': '10', 'age': 15},
    {'studentid': '8', 'student_id': '8-1', 'name': 'Matthew Moore', 'class': '11', 'age': 16},
    {'studentid': '9', 'student_id': '9-1', 'name': 'Olivia Taylor', 'class': '12', 'age': 17},
    {'studentid': '10', 'student_id': '10-1', 'name': 'James Anderson', 'class': '10', 'age': 15},
    {'studentid': '11', 'student_id': '11-1', 'name': 'Ava Thomas', 'class': '11', 'age': 16},
    {'studentid': '12', 'student_id': '12-1', 'name': 'Christopher Jackson', 'class': '12', 'age': 17},
    {'studentid': '13', 'student_id': '13-1', 'name': 'Isabella White', 'class': '10', 'age': 15},
    {'studentid': '14', 'student_id': '14-1', 'name': 'Joshua Harris', 'class': '11', 'age': 16},
    {'studentid': '15', 'student_id': '15-1', 'name': 'Mia Martin', 'class': '12', 'age': 17},
    {'studentid': '16', 'student_id': '16-1', 'name': 'David Thompson', 'class': '10', 'age': 15},
    {'studentid': '17', 'student_id': '17-1', 'name': 'Amelia Garcia', 'class': '11', 'age': 16},
    {'studentid': '18', 'student_id': '18-1', 'name': 'Alexander Martinez', 'class': '12', 'age': 17},
    {'studentid': '19', 'student_id': '19-1', 'name': 'Charlotte Robinson', 'class': '10', 'age': 15},
    {'studentid': '20', 'student_id': '20-1', 'name': 'Joseph Clark', 'class': '11', 'age': 16},
    {'studentid': '21', 'student_id': '21-1', 'name': 'Grace Lewis', 'class': '12', 'age': 17},
    {'studentid': '22', 'student_id': '22-1', 'name': 'Elijah Lee', 'class': '10', 'age': 15},
    {'studentid': '23', 'student_id': '23-1', 'name': 'Chloe Walker', 'class': '11', 'age': 16},
    {'studentid': '24', 'student_id': '24-1', 'name': 'Samuel Hall', 'class': '12', 'age': 17},
    {'studentid': '25', 'student_id': '25-1', 'name': 'Sofia Allen', 'class': '10', 'age': 15},
    {'studentid': '26', 'student_id': '26-1', 'name': 'Benjamin Young', 'class': '11', 'age': 16},
    {'studentid': '27', 'student_id': '27-1', 'name': 'Harper King', 'class': '12', 'age': 17},
    {'studentid': '28', 'student_id': '28-1', 'name': 'Henry Wright', 'class': '10', 'age': 15},
    {'studentid': '29', 'student_id': '29-1', 'name': 'Avery Scott', 'class': '11', 'age': 16},
    {'studentid': '30', 'student_id': '30-1', 'name': 'Sebastian Green', 'class': '12', 'age': 17},
    {'studentid': '31', 'student_id': '31-1', 'name': 'Evelyn Adams', 'class': '10', 'age': 15},
    {'studentid': '32', 'student_id': '32-1', 'name': 'Owen Baker', 'class': '11', 'age': 16},
    {'studentid': '33', 'student_id': '33-1', 'name': 'Aria Gonzalez', 'class': '12', 'age': 17},
    {'studentid': '34', 'student_id': '34-1', 'name': 'Jack Nelson', 'class': '10', 'age': 15},
    {'studentid': '35', 'student_id': '35-1', 'name': 'Ellie Carter', 'class': '11', 'age': 16},
    {'studentid': '36', 'student_id': '36-1', 'name': 'Lucas Perez', 'class': '12', 'age': 17},
    {'studentid': '37', 'student_id': '37-1', 'name': 'Lily Mitchell', 'class': '10', 'age': 15},
    {'studentid': '38', 'student_id': '38-1', 'name': 'Mason Roberts', 'class': '11', 'age': 16},
    {'studentid': '39', 'student_id': '39-1', 'name': 'Zoe Turner', 'class': '12', 'age': 17},
    {'studentid': '40', 'student_id': '40-1', 'name': 'Logan Phillips', 'class': '10', 'age': 15},
    {'studentid': '41', 'student_id': '41-1', 'name': 'Aubrey Campbell', 'class': '11', 'age': 16},
    {'studentid': '42', 'student_id': '42-1', 'name': 'Ethan Parker', 'class': '12', 'age': 17},
    {'studentid': '43', 'student_id': '43-1', 'name': 'Hannah Evans', 'class': '10', 'age': 15},
    {'studentid': '44', 'student_id': '44-1', 'name': 'Jayden Edwards', 'class': '11', 'age': 16},
    {'studentid': '45', 'student_id': '45-1', 'name': 'Addison Collins', 'class': '12', 'age': 17},
    {'studentid': '46', 'student_id': '46-1', 'name': 'Aiden Stewart', 'class': '10', 'age': 15},
    {'studentid': '47', 'student_id': '47-1', 'name': 'Layla Sanchez', 'class': '11', 'age': 16},
    {'studentid': '48', 'student_id': '48-1', 'name': 'Gabriel Morris', 'class': '12', 'age': 17},
    {'studentid': '49', 'student_id': '49-1', 'name': 'Scarlett Rogers', 'class': '10', 'age': 15},
    {'studentid': '50', 'student_id': '50-1', 'name': 'Caleb Reed', 'class': '11', 'age': 16},
    {'studentid': '51', 'student_id': '51-1', 'name': 'Victoria Cook', 'class': '12', 'age': 17},
    {'studentid': '52', 'student_id': '52-1', 'name': 'Dylan Morgan', 'class': '10', 'age': 15},
    {'studentid': '53', 'student_id': '53-1', 'name': 'Penelope Bell', 'class': '11', 'age': 16},
    {'studentid': '54', 'student_id': '54-1', 'name': 'Luke Bailey', 'class': '12', 'age': 17},
    {'studentid': '55', 'student_id': '55-1', 'name': 'Camila Cooper', 'class': '10', 'age': 15},
    {'studentid': '56', 'student_id': '56-1', 'name': 'Isaac Rivera', 'class': '11', 'age': 16},
    {'studentid': '57', 'student_id': '57-1', 'name': 'Riley Richardson', 'class': '12', 'age': 17},
    {'studentid': '58', 'student_id': '58-1', 'name': 'Nathan Cox', 'class': '10', 'age': 15},
    {'studentid': '59', 'student_id': '59-1', 'name': 'Nora Howard', 'class': '11', 'age': 16},
    {'studentid': '60', 'student_id': '60-1', 'name': 'Isaiah Ward', 'class': '12', 'age': 17},
    {'studentid': '61', 'student_id': '61-1', 'name': 'Elizabeth Brooks', 'class': '10', 'age': 15},
    {'studentid': '62', 'student_id': '62-1', 'name': 'Thomas Bennett', 'class': '11', 'age': 16},
    {'studentid': '63', 'student_id': '63-1', 'name': 'Eliana Barnes', 'class': '12', 'age': 17},
    {'studentid': '64', 'student_id': '64-1', 'name': 'Aaron Jenkins', 'class': '10', 'age': 15},
    {'studentid': '65', 'student_id': '65-1', 'name': 'Madison Perry', 'class': '11', 'age': 16},
    {'studentid': '66', 'student_id': '66-1', 'name': 'Ryan Powell', 'class': '12', 'age': 17},
    {'studentid': '67', 'student_id': '67-1', 'name': 'Nina Long', 'class': '10', 'age': 15},
    {'studentid': '68', 'student_id': '68-1', 'name': 'Aaron James', 'class': '11', 'age': 16},
    {'studentid': '69', 'student_id': '69-1', 'name': 'Brody Stone', 'class': '12', 'age': 17},
    {'studentid': '70', 'student_id': '70-1', 'name': 'Grace Dunn', 'class': '10', 'age': 15}
]


# Add each student to the DynamoDB table
for student in students:
    response = table.put_item(
        Item=student
    )
    print(f"Added student: {student['name']}")

print("All students added successfully!")
