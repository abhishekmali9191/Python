post_url = "https://jsonplaceholder.typicode.com/posts"

weather_data={
    "city":"Newyork",
    "temperature":28,
    "humidity":60,
    "condition":"sunny"
}

def post_data(url,data):
     response = requests.post(url,json=data)
     print(response.json())

#Deleting data using id
try:
    post_data(post_url,weather_data)
    id = 111
    delete_url = f"https://reqres.in/api/users/{id}"
    def delete_data(url):
        response = requests.delete(delete_url)
        if response.status_code == 204:
            print("User deleted successfully")
        else:
            print("Failed to delete user")
    delete_data(delete_url)
except Exception as e:
    print(e)
    
    
# #########################################################
# OUTPUT
# {'city': 'Newyork', 'temperature': 28, 'humidity': 60, 'condition': 'sunny', 'id': 101}
# User deleted successfully