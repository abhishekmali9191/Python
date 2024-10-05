#Hands on POST request
#API endpoint for creating a new user
post_url = "https://regres.in/api/users"
#Data to be sent in the post request
post_data ={
    "name":"Abhishek",
    "job" : "Software Dev"
}
response = requests.post(post_url,json=post_data)


