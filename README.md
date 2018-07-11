# banweb-python
Interface with the banner website to access academic information in your programs.
### Table of contents
  * [Examples](#examples)
  * [Documentation](#documentation)
    * [login](#loginroot-sid-pin-security_answer)
## Examples
### Getting a list of registered courses
```python
import banweb
import json

banweb.login("https://rooturl.edu", "ABC123456", "12345", "Answer")
courses = banweb.get_courses("2018", "fall")

print(json.dumps(courses, indent=4))
```
This code would output:
```
{
    "total_credits": 16,
    "courses": [
        {
            "title": "Example Course - EX 3000 - 10",
            "associated_term": "Fall 2018",
            "crn": 24567,
            "status": "**Web Registered** on 04/19/18",
            "assigned_instructor": "Jim A. Bob",
            "grade_mode": "Letter Grade",
            "credits": 3,
            "level": "Undergraduate",
            "campus": "Main Campus"
        },
        {
            "title": "Example Discussion - EX 3000 - 30",
            "associated_term": "Fall 2018",
            "crn": 24568,
            "status": "**Web Registered** on 04/19/18",
            "assigned_instructor": "Jim A. Bob",
            "grade_mode": "Letter Grade",
            "credits": 0,
            "level": "Undergraduate",
            "campus": "Main Campus"
        },
        ...
    ]
}
```
### Getting a list of financial awards
```python
import banweb
import json

banweb.login("https://rooturl.edu", "ABC123456", "12345", "Answer")
awards = banweb.get_awards("1718")

print(json.dumps(awards, indent=4))
```
This code would output:
```
{
    "awards": [
        {
            "fund": "Honors Scholarship",
            "fall": {
                "status": "Accepted",
                "amount": "$7,500.00"
            },
            "spring": {
                "status": "Accepted",
                "amount": "$7,500.00"
            },
            "total": "$15,000.00"
        },
        {
            "fund": "Federal Work-Study",
            "fall": {
                "status": "Web Accept",
                "amount": "$1,250.00"
            },
            "spring": {
                "status": "Web Accept",
                "amount": "$1,250.00"
            },
            "total": "$2,500.00"
        },
        ...
    ]
}
```
## Documentation
### login(root, sid, pin, security_answer)

Starts a banner session with the given credentials. Required in order to use any methods that access the banner site.
  * **root:** The root url for user's banner site
  * **sid:** The user's sid used to log into banner
  * **pin:** The user's pin used to log into banner
  * **security_answer:** The answer to the user's security question

Example usage:
```python
banweb.login("https://rooturl.edu", "ABC123456", "12345", "Answer")
```

### navigate_to(url, headers=None, data=None, cookies=None, method="GET")
Loads the given url using the banner session and returns a response object
  * **url:** The url to load
  * **headers:** Optional HTTP headers
  * **cookies:** Optional Session cookies
  * **method:** Optional HTTP method (defaults to GET)

Example usage:
```python
banweb.login("https://rooturl.edu", "ABC123456", "12345", "Answer")
```