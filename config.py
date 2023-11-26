import os

#API ID & API Hash -----> my.telegram.org
api_id = 924859
api_hash = 'a4c9a18cf4d8cb24062ff6916597f832'

#Bot Token -----> @BotFather
token = '6898058070:AAERmk33JiLIdk1HCEI0-BUDJU2nY9EANx8'

#Session Name -----> optional
session_name = 'FTP_Uploader'


#The robot admin (the person who can give orders to the robot.) -----> @myidbot
admins = [6113077431]

# Chat id to send technical logs
dev = 6113077431

# When a file is sent to the bot, first that file is downloaded from the Telegram repository and stored in the bot's server.
# Here you need to specify its temporary storage path
# For example, I set the bot to save the downloaded file in the current path (the path where config.py file is located).
dl_path = os.path.abspath(os.getcwd()) + '/'


# The upload path where we give FTP access to the bot.
ftp_path = '/htdocs/hx/'

# The files are temporarily downloaded after they are on the bot server. They are uploaded to another host through FTP.
# Here we have to give FTP access to the bot.
ftp_ip = 'ftpupload.net'
ftp_username = 'rigrr_34653010'
ftp_password = 'nrq0pgqv'
ftp_domain = 'ks406989.ifast.in.eu.org/hx/'
