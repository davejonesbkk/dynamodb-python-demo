import argparse
import boto3

#Get the boto3 resource
dynamodb = boto3.resource('dynamodb')

#Instantiate the table
table = dynamodb.Table('users')

parser=argparse.ArgumentParser(description='Add new users first & lastname to the DB.')
parser.add_argument('firstname', type=str, help='users firstname')
parser.add_argument('lastname', type=str, help='users lastname')
parser.add_argument('age', type=int, help='users age')

args = parser.parse_args()


table.put_item(
	Item={
		'username': args.firstname+args.lastname,
		'first_name': args.firstname,
		'last_name': args.lastname,
		'age': args.age,
		'account_type': 'standard_user',
	}
)

print(args.firstname, args.lastname, args.age)





