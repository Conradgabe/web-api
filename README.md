# web-api
web API with CRUD functionality

# Guide
go to overview to see the entire operation endpoints: 'overview': 'api/v1/',
To create a task: {'create': 'api/v1/create/'},
To update a task: {'update': 'api/v1/update/<int:id>/'},
To delete a task: {'delete': 'api/v1/delete/<int:id>/'},
To list out task: {'list view': 'api/v1/list/'},
To give details of a task: {'detail view': 'api/v1/detail/<int:id>/'}

using this api require authorization(Tokenauthentication):
    Register a new user with: {'register': 'api/v1/register/'}, to get your token for authentication
