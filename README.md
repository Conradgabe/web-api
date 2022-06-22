# web-api
web API with CRUD functionality
# Intro
    this a task CRUD api

# Guide
go to overview to see the entire operation endpoints: 'overview': 'api/v1/',

1) To create a task: {'create': 'api/v1/create/'},
2) To update a task: {'update': 'api/v1/update/<int:id>/'},
3) To delete a task: {'delete': 'api/v1/delete/<int:id>/'},
4) To list out task: {'list view': 'api/v1/list/'},
5) To give details of a task: {'detail view': 'api/v1/detail/<int:id>/'}

# Authentication
    using this api require authorization(Tokenauthentication as API key):
        Register a new user with: {'register': 'api/v1/register/'}, to get your token for authentication
        Registration requires a username and password.
