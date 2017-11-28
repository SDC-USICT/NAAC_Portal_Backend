# NAAC_Portal
Portal for GGSIPU Faculty Data Acquisition System Report

### Usage
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Start up the MySQL server and make sure it has:
- Database called 'naac_portal'. (Need to be created the first time)
- User ```root```, with no/empty password.

https://github.com/SDC-USICT/NAAC_Portal/blob/master/naac_portal/settings.py#L94-L103

You can also use your own config but make sure to not commit
it because then git merge conflicts may arise.

# API Examples

```
REQUEST:
OPTIONS /api/login HTTP/1.1" 200 0
{'empid': '01235', 'password': 'test'}

RESPONSE
{'success': 'true'}
```

```
REQUEST
GET /api/columns HTTP/1.1" 200 6895
{'empid': '01235'}

RESPONSE
{'Workshop': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'title', 'verbose': 'Name'}, {'name': 'role', 'verbose': 'Role'}, {'name': 'date', 'verbose': 'Date'}, {'name': 'duration', 'verbose': 'Duration(in days)'}, {'name': 'organization', 'verbose': 'Organization'}], 'Membership': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'title', 'verbose': 'Academic Body Name'}, {'name': 'membership_no', 'verbose': 'Membership Type'}, {'name': 'type', 'verbose': 'Membership Type'}, {'name': 'start_year', 'verbose': 'Start Year'}, {'name': 'end_year', 'verbose': 'End Year'}], 'Projects': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'title', 'verbose': 'Project Title'}, {'name': 'sponsors', 'verbose': 'Sponsoring Agency'}, {'name': 'date_of_award', 'verbose': 'Date of Award'}, {'name': 'date_completed', 'verbose': 'Date of Completed'}, {'name': 'amnt_sanctioned', 'verbose': 'Amount Sanctioned'}, {'name': 'status', 'verbose': 'Status'}, {'name': 'author', 'verbose': 'Principle Investigator'}, {'name': 'coauthor', 'verbose': 'Co Principle Investigators'}], 'Extra': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'title', 'verbose': 'Name'}, {'name': 'department', 'verbose': 'Department'}, {'name': 'level', 'verbose': 'Level'}, {'name': 'details', 'verbose': 'Details'}, {'name': 'year', 'verbose': 'Year'}, {'name': 'month', 'verbose': 'Month'}], 'Book': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'employee'}, {'name': 'title', 'verbose': 'Title of Book'}, {'name': 'isbn', 'verbose': 'ISBN'}, {'name': 'year', 'verbose': 'Year'}, {'name': 'coauthor', 'verbose': 'Co Authors'}, {'name': 'page_no_start', 'verbose': 'Page number starting'}, {'name': 'page_no_end', 'verbose': 'Page number ending'}], 'Conference': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'title', 'verbose': 'Title of Paper'}, {'name': 'name_and_publisher', 'verbose': 'Name & Publisher'}, {'name': 'issue_no', 'verbose': 'Issue no'}, {'name': 'issn_isbn', 'verbose': 'ISBN No.'}, {'name': 'indexing', 'verbose': 'Indexing'}, {'name': 'year', 'verbose': 'Year'}, {'name': 'international_national', 'verbose': 'International/National'}, {'name': 'coauthor', 'verbose': 'Co Authors'}, {'name': 'page_no_start', 'verbose': 'Page number starting'}, {'name': 'page_no_end', 'verbose': 'Page number ending'}], 'Awards': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'title', 'verbose': 'Title'}, {'name': 'awardType', 'verbose': 'awardType'}, {'name': 'organisation', 'verbose': 'Organization'}, {'name': 'month', 'verbose': 'Month'}, {'name': 'year', 'verbose': 'Year'}], 'GuestLecture': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'nature', 'verbose': 'Nature'}, {'name': 'institute', 'verbose': 'Institute Name'}, {'name': 'date', 'verbose': 'Date'}, {'name': 'title', 'verbose': 'Topic'}, {'name': 'year', 'verbose': 'Year'}], 'Professional': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'title', 'verbose': 'Highest Qualification'}, {'name': 'undergraduation_course', 'verbose': 'Undergraduation Course'}, {'name': 'undergraduation_stream', 'verbose': 'Undergraduation Stream'}, {'name': 'undergraduation_year', 'verbose': 'Undergraduation Year'}, {'name': 'undergraduation_college', 'verbose': 'Undergraduation College'}, {'name': 'postgraduation_course', 'verbose': 'Postgraduation Course'}, {'name': 'postgraduation_stream', 'verbose': 'Postgraduation Stream'}, {'name': 'postgraduation_year', 'verbose': 'Postgraduation Year'}, {'name': 'postgraduation_college', 'verbose': 'Postgraduation College'}, {'name': 'phd_title', 'verbose': 'PhD Title'}, {'name': 'phd_specialization', 'verbose': 'PhD Specialization'}, {'name': 'phd_college', 'verbose': 'PhD College'}, {'name': 'phd_year_application', 'verbose': 'PhD Year Application'}, {'name': 'phd_year_acquiring', 'verbose': 'PhD Year Acquiring'}, {'name': 'phd_no', 'verbose': 'No PhD'}, {'name': 'pdf_title', 'verbose': 'PDF Title'}, {'name': 'pdf_specialization', 'verbose': 'PDF Specialization'}, {'name': 'pdf_college', 'verbose': 'PDF College'}, {'name': 'pdf_year_application', 'verbose': 'PDF Year Application'}, {'name': 'pdf_year_acquiring', 'verbose': 'PDF Year Acquiring'}, {'name': 'pdf_no', 'verbose': 'No PdF'}, {'name': 'acedemic_exp', 'verbose': 'Acedemic Experience'}, {'name': 'industrial_exp', 'verbose': 'Industrial Experience'}, {'name': 'qualification_year_completion', 'verbose': 'Year Of Completion of Highest Qualification'}, {'name': 'pursuing', 'verbose': 'Phd Pursuing'}, {'name': 'submitted', 'verbose': 'Phd Submitted'}, {'name': 'awarded', 'verbose': 'Phd Awarded'}, {'name': 'phds', 'verbose': 'Total Student'}], 'Patents': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'title', 'verbose': 'Patent Name'}, {'name': 'patenting_agency', 'verbose': 'Patenting Agency'}, {'name': 'year_application', 'verbose': 'Year Of Application'}, {'name': 'year_grant', 'verbose': 'Year of Grant'}, {'name': 'type', 'verbose': 'Patent Type'}, {'name': 'status', 'verbose': 'Status'}], 'BookChapters': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'employee'}, {'name': 'title', 'verbose': 'Title of Book Chapter'}, {'name': 'book_title_and_publisher', 'verbose': 'Book Title with Publisher'}, {'name': 'page_no', 'verbose': 'Page No.'}, {'name': 'isbn', 'verbose': 'ISBN No.'}, {'name': 'indexing', 'verbose': 'Indexing'}, {'name': 'year', 'verbose': 'Year'}, {'name': 'month', 'verbose': 'Month'}, {'name': 'coauthor', 'verbose': 'Co Authors'}], 'SubjectsTaken': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'subjects', 'verbose': 'Subject Name'}, {'name': 'year', 'verbose': 'Year'}, {'name': 'school', 'verbose': 'School'}, {'name': 'sem', 'verbose': 'Semester'}, {'name': 'mode', 'verbose': 'Type'}, {'name': 'image', 'verbose': 'File Name'}, {'name': 'course', 'verbose': 'Course'}], 'JournalPapers': [{'name': 'id', 'verbose': 'ID'}, {'name': 'employee', 'verbose': 'Employee ID'}, {'name': 'title', 'verbose': 'Title of Paper'}, {'name': 'name', 'verbose': 'Journal Name with Publisher'}, {'name': 'publisher', 'verbose': 'Journal Name with Publisher'}, {'name': 'volume_no', 'verbose': 'Vol. No.'}, {'name': 'issn_isbn', 'verbose': 'ISSN No.'}, {'name': 'indexing', 'verbose': 'Indexing'}, {'name': 'month', 'verbose': 'Month'}, {'name': 'hindex', 'verbose': 'H-Index of Journal using Scimago (if Scopus, SCI-Ex or SCI)'}, {'name': 'impact_factor', 'verbose': 'Impact Factor if SCI-Ex or SCI'}, {'name': 'coauthor', 'verbose': 'Co Authors'}]}

```

```
REQUEST
OPTIONS /api/get HTTP/1.1" 200 0
{'empid': '01235', 'kls': 'Professional'}

RESPONSE
[{"model": "employee.employee", "pk": "01235", "fields": {"name": "Test User 3", "email": "surender7790@gmail.com", "phone": 9718305549, "date_of_joining": "12-AUG-2014", "designation": "STUDENT", "room_no": "NA", "school": "usict"}}]
```

```
REQUEST
POST /api/employee HTTP/1.1" 200 254

RESPONSE
[{"model": "employee.employee", "pk": "01235", "fields": {"name": "Test User 3", "email": "surender7790@gmail.com", "phone": 9718305549, "date_of_joining": "12-AUG-2014", "designation": "STUDENT", "room_no": "NA", "school": "usict"}}]

```


Request-Response for Books Section; Other Sections Have Similar Responses.
```
REQUEST
"POST /api/post HTTP/1.1" 200 463
{'data': [{'year': '2013', 'page_no_end': 123, 'page_no_start': 213, 'employee': '01235', 'isbn': 12312312312, 'coauthor': '', 'title': 'Title'}], 'kls': 'Book'}

RESPONSE
{'data': [{'year': '2015', 'employee': '01235', 'page_no_start': 23, 'pk': 1, 'page_no_end': 12, 'isbn': 234567765432, 'coauthor': '', 'title': 'sdfgfsd'}, {'year': '2016', 'employee': '01235', 'page_no_start': 1, 'pk': 2, 'page_no_end': 12, 'isbn': 654345675564, 'coauthor': '', 'title': 'TOAST'}, {'year': '2013', 'employee': '01235', 'page_no_start': 213, 'pk': 4, 'page_no_end': 123, 'isbn': 12312312312, 'coauthor': '', 'title': 'Title'}], 'success': 'true'}

```
