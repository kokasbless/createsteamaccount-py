import smtplib
import steam

# Set the SMTP server and port for Outlook
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()

# Set your login credentials
username = 'murilocriarconta@outlook.com'
password = '4000221877CL'

# Login to the email account
server.login(username, password)

# Set the base details of the new email accounts
base_email = 'mumudede9@outlook.com'
password = '4000221877CL'

# Set the number of accounts to create
num_accounts = 10

# Set the starting number for the new email accounts
start_num = 1

# Create a new Steam client
client = steam.WebAPI()

# Set your Steam API key
api_key = '79954BD04D1BAFC33DC152EAE109C079'

# Create the specified number of accounts
for i in range(num_accounts):
    # Increment the number for the new email account
    num = start_num + i
    email = base_email + str(num)

    # Create a new Steam account using the email and password from the new email account
    result = client.ISteamUser.CreateAccount(api_key=api_key,
                                             username=email,
                                             password=password,
                                             email=email,
                                             question='Qual é o nome do seu animal de estimação?',
                                             answer='Fred')

    # Check the result of the account creation
    if result['response']['success'] == 1:
        print(f'Account {email} created successfully!')
    else:
        print(f'Error creating account {email}:', result['response']['message'])

# Disconnect from the server
server.quit()
