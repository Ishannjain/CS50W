people=[
    {"name":"harry","house":"gryfindor"},
    {"name":"rom","house":"gryfindor"},
    {"name":"har","house":"gryfindor"}
]
# list of dictionaries

people.sort(key=lambda person :person['name'])
print(people)