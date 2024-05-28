<h1>Task Round - Assign Task Application</h1>
<h3>I. File Hierarchy: </h3>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>1. Project Name:</strong> assignment,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>2. Application name :</strong> task1, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>3. Environment Setup:</strong> cd env/Scripts then .\activate, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>4. Templates:</strong> Inside the django app i.e. task1 
<h3>II. Application/Task Implementation</h3>
&nbsp;&nbsp;&nbsp;&nbsp;<strong>1. Models in models.py</strong>:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>1.1. RegisterUser model</strong> (extended Default User Model) using onetoonefield : for registaration;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>1.2. DepartmentUser model:</strong> All other department and related user;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>1.3. TaskAssign model:</strong> Add task model and records all assigned tasks to users from another department users<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<strong>2. Forms.py</strong>:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>2.1. RegisterUser Form</strong>for registaration form with save method overriding in whcih user object being created in USer models as well as in RegisterUser model;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>2.2. LoginForm: </strong> for Login form created from scratch and not by modleform<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>2.3. TaskAssign Form</strong> Add Task Form<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<strong>3. urls for web pages: </strong>:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>3.1. Register Page Link: </strong> (http://127.0.0.1:8000/register<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>3.2. Login Page Link: </strong> (http://127.0.0.1:8000/login, redirecting after register<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>3.3. Dashboard Page Link: </strong> (http://127.0.0.1:8000/dashboard, redirecting to this page after successful login and with login this page cant be accessed<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>3.4. Add Task Page Link: </strong> http:\\](http://127.0.0.1:8000/assign_task/<name><br>, after clicking add to ask button in dashboard, can access the task assign form and this also accessed by after successful login<br>
&nbsp;&nbsp;&nbsp;&nbsp;<strong>4. API Endpoints: </strong>:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>4.1. Register API: </strong> (http://127.0.0.1:8000/api/register [POST, GET, GET by Id, PUT, PUT by Id, Delete by ID]<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>4.2. Task Assign API: </strong> (http://127.0.0.1:8000/api/task-assign [POST, GET, GET by Id, PUT, PUT by Id, Delete by ID]<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>4.2. Department related user API: </strong> (http://127.0.0.1:8000/api/department-user [POST, GET, GET by Id, PUT, PUT by Id, Delete by ID]<br>
