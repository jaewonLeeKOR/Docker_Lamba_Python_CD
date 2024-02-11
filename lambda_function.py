def lambda_handler(event, context):
    message = 'Bye {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }
