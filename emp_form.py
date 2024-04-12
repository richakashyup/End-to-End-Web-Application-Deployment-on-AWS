from flask import Flask, render_template, request
import pymysql
import boto3
from config import custombucket, customregion, customhost, customuser, custompass, customdb

app = Flask(__name__, template_folder="templates")

db_conn = pymysql.connect(
    host=customhost,
    user=customuser,
    password=custompass,
    database=customdb
)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('emp_form.html')

@app.route("/about", methods=['POST'])
def about():
    return render_template('www.awsdb.com')

@app.route("/process_employee", methods=['POST'])
def AddEmp():
    emp_id = request.form['employee_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['primary_skill']
    location = request.form['location']
    emp_image_file = request.files['image']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    if emp_image_file.filename == "":
        return "Please select a file"

    try:
        cursor.execute(insert_sql, (emp_id, first_name, last_name, pri_skill, location))
        db_conn.commit()
        emp_name = f"{first_name} {last_name}"

        # Upload image file to S3
        emp_image_file_name_in_s3 = f"emp-id-{emp_id}_image_file"
        s3 = boto3.client('s3', region_name=customregion)
        try:
            print("Data inserted in MySQL RDS... uploading image to S3...")
            s3.upload_fileobj(emp_image_file, custombucket, emp_image_file_name_in_s3)
            object_url = f"https://{custombucket}.s3.{customregion}.amazonaws.com/{emp_image_file_name_in_s3}"
        except Exception as e:
            return str(e)

    finally:
        cursor.close()

    print("All modifications done...")
    return render_template('emp_form.html', name=emp_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
