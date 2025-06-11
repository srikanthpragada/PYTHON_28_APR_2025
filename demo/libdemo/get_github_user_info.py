import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")
#print(resp)
if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit(1)  # exit with error

details = resp.json()
print(f'Name     :   {details['name']}')
print(f'Location :   {details['location']}')
print(f'Company  :   {details['company']}')
print(f'Joined On:   {details['created_at']}')

