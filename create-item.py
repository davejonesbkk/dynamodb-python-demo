import boto3

#Get the resource
dynamodb = boto3.resource('dynamodb')

#Instantiate a table object
table=dynamodb.Table('users')

table.put_item(
	Item={
		'username': 'jandoe',
		'first_name': 'Jane',
		'last_name': 'Doe',
		'age': 25,
		'account_type': 'standard_user',
	}
)


