# banweb-python
Interface with the banner website to access academic information in your programs.

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