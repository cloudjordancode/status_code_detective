

# GET    /posts/1
# GET    /posts/99999
# POST   /posts
# DELETE /posts/1
# GET    /invalidendpoint
# GET    /users/1/todos

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# 1. 
response = requests.get(f"{BASE_URL}/posts/1")


if 200 <= response.status_code < 300:
    category = "Success"
elif 300 <= response.status_code < 400:
    category = "Redirection"
elif 400 <= response.status_code < 500:
    category = "Client Error"
elif 500 <= response.status_code < 600:
    category = "Server Error"

if response.status_code == 200:
    description = "Request succeeded - resource returned."

print()
print("GET /posts/1: ") 
print(f"    Status: {response.status_code} ({category})")
print(f"    Description: {description}")
print()


# 2. 
response = requests.get(f"{BASE_URL}/posts/99999")

if 200 <= response.status_code < 300:
    category = "Success"
elif 300 <= response.status_code < 400:
    category = "Redirection"
elif 400 <= response.status_code < 500:
    category = "Client Error"
elif 500 <= response.status_code < 600:
    category = "Server Error"
else: 
    print(f"    Error {response.status_code}{response.reason}")

if response.status_code == 404:
    error_description = "Error - nonexistent resource."

print()
print("GET /posts/99999: ") 
print(f"    Status: {response.status_code} ({category})")
print(f"    Description: {error_description}")
print()


# 3. 
new_post = {"title": "Test", "body": "Test body", "userId": 1}
response = requests.post(f"{BASE_URL}/posts", json=new_post)

post_description = "Data Successfully Created."

if 200 <= response.status_code < 300:
    category = "Success"
elif 300 <= response.status_code < 400:
    category = "Redirection"
elif 400 <= response.status_code < 500:
    category = "Client Error"
elif 500 <= response.status_code < 600:
    category = "Server Error"
else: 
    print(f"    Error {response.status_code}{response.reason}")

print()
print("POST new post: ") 
print(f"    Status: {response.status_code} ({category})")
print(f"    Description: {post_description}")
print()


# 4. 
response = requests.delete(f"{BASE_URL}/posts/1")
delete_description = "Post Successfully Deleted."

if 200 <= response.status_code < 300:
    category = "Success"
elif 300 <= response.status_code < 400:
    category = "Redirection"
elif 400 <= response.status_code < 500:
    category = "Client Error"
elif 500 <= response.status_code < 600:
    category = "Server Error"
else: 
    print(f"    Error {response.status_code}{response.reason}")

print()
print(f"DELETE /posts/1: ")
print(f"    Status: {response.status_code} ({category})")
print(f"    Description: {delete_description}")
print()


# 5. 
response = requests.get(f"{BASE_URL}/invalidendpoint")

if 200 <= response.status_code < 300:
    category = "Success"
elif 300 <= response.status_code < 400:
    category = "Redirection"
elif 400 <= response.status_code < 500:
    category = "Client Error"
elif 500 <= response.status_code < 600:
    category = "Server Error"
else: 
    print(f"    Error {response.status_code}{response.reason}")

if response.status_code == 404:
    bad_uri_description = "Error - Bad URI."


print()
print("GET /invalidendpoint: ") 
print(f"    Status: {response.status_code} ({category})")
print(f"    Description: {bad_uri_description}")
print()



# 6.
response = requests.get(f"{BASE_URL}/users/1/todos")

if 200 <= response.status_code < 300:
    category = "Success"
elif 300 <= response.status_code < 400:
    category = "Redirection"
elif 400 <= response.status_code < 500:
    category = "Client Error"
elif 500 <= response.status_code < 600:
    category = "Server Error"
else: 
    print(f"    Error {response.status_code}{response.reason}")

if response.status_code == 200:
    nested_description = "Nested Resource."


print()
print("GET /users/1/todos: ") 
print(f"    Status: {response.status_code} ({category})")
print(f"    Description: {nested_description}")
print()


# BONUS
def status_report(url, method, data=None):
    if method == "GET":
        response = requests.get(url)
    elif method == "DELETE":
        response = requests.delete(url)
    elif method == "POST":
        response = requests.post(url, json=data)

    if 200 <= response.status_code < 300:
        category = "Success"
    elif 300 <= response.status_code < 400:
        category = "Redirection"
    elif 400 <= response.status_code < 500:
        category = "Client Error"
    elif 500 <= response.status_code < 600:
        category = "Server Error"

    return (
        f"{method} {url}\n"
        f"Status: {response.status_code} ({category})"
    )

print(status_report(f"{BASE_URL}/posts/1", "GET"))