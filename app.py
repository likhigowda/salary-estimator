from flask import Flask, render_template, request
import joblib
import warnings

# Filter all warnings
warnings.filterwarnings("ignore")

model = joblib.load('salary_estimator.joblib')


def get_gender(gender):
    lst = [0,0]
    data = ['Female','Male']
    for index,i in enumerate(data):
        if(i == gender):
            lst[index] = 1
            return lst
    return lst


def get_education(education):
    lst = [0,0,0]
    data = ["Bachelor's","Master's","phD"]
    for index,i in enumerate(data):
        if(i == education):
            lst[index] = 1
            return lst
    return lst
        

def get_job(job):
    lst = [0,0,0,0,0,0,0,0,0]
    data = ["Creative and Design","Customer Service and Support","Finance and Accounting","Human Resources and Recruitment","Management and Leadership","Operations and Project Management","Research and Analysis","Sales and Marketing","Software and Technology"]
    for index,i in enumerate(data):
        if(i == job):
            lst[index] = 1
            return lst
    return lst


app = Flask(__name__)

# Route for the homepage
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/estimate', methods = ['POST'])
def estimate():

    result = None

    age = int(request.form['Age'])
    experience = int(request.form['Years of Experience'])
    gender = request.form['Gender']
    education = request.form['Education Level']
    job = request.form['Education Level']

    gender_list = get_gender(gender)
    education_list = get_education(education)
    job_list = get_job(job)

    print(age, experience, gender_list[0], gender_list[1], education_list[0], education_list[1], education_list[2], job_list[0], job_list[1], job_list[2], job_list[3], job_list[4], job_list[5], job_list[6], job_list[7], job_list[8])

    prediction = list(model.predict([[age, experience, gender_list[0], gender_list[1], education_list[0], education_list[1], education_list[2], job_list[0], job_list[1], job_list[2], job_list[3], job_list[4], job_list[5], job_list[6], job_list[7], job_list[8]]]))
    
    result = round(prediction[0])

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(debug=True)
