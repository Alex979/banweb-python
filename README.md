# banweb-python
Interface with the banner website to access academic information in your programs.

## Examples
Getting a list of registered courses
```python
import banweb
import json

banweb.login("https://rooturl.edu", "ABC123456", "12345", "Answer")
courses = banweb.get_courses("2018", "fall")

print(json.dumps(courses, indent=4))
```