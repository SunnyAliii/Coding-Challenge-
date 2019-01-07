# Coding-Challenge-
Illumio Coding Assignment 2018, Back-end QA team 

Introduction:
I have followed the test driven development approach and wrote unit test cases for individual functions. Then to check the application as a whole, I ran it on terminal with some valid and invalid urls. 
Ex: https://www.facebook.com, https://www.example.com, 192.168.1.1 etc.

Interesting coding, design, or algorithmic choices I’d like to point out:
a) Followed PEP-8 standards.
b) Followed OOPS design approach by creating QueryApi class which made my code much more readable & modular.
c) My code is loosely coupled, which is a pre-requisite for a code to be scalable.
d) Scalability, we can add more regular expressions for checking if a url has a valid syntax.
e) Scalability, we can neglect urls by giving more invalid status codes.
f) I use a dictionary, a hashable python data structure; so that the user does not need to enter the old url again & can simply access the same one by providing the index associated with each url which 
is shown on the UI/command line.
g) Modularity, I can easily import my functions into other modules.

Refinements or optimizations that I would’ve implemented if I had more time:
The run function that holds the retry loop could have been done better, as there are some lines of code repeated inside the nested while loop.

Additional Information:
Instead of fetching data directly from the user with a GET request,
We first ensure
1. The url has got a valid syntax by checking it with all regular expressions available.
2. The url is checked if available online by fetching & validating its STATUS CODE.
If the STATUS CODE is valid, then only do we make a GET request to fetch the data.
This ensures our code is fast and optimized. Moreover, it does not break, if the url is syntactically valid but unavailable online.
