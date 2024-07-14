import os

#API ID & API Hash -----> my.telegram.org
api_id = 2532603
api_hash = 'f565b00bbe3ad9c6748e39a3a71d16e7'

#Bot Token -----> @BotFather
token = '7132343147:AAGHv_wmRd_7PRXeLsa9r42Zl28EbyR5V0E'

#Session Name -----> optional
session_name = 'FTP_Uploader'


#The robot admin (the person who can give orders to the robot.) -----> @myidbot
admins = [754495556]

# Chat id to send technical logs
dev = 754495556

# When a file is sent to the bot, first that file is downloaded from the Telegram repository and stored in the bot's server.
# Here you need to specify its temporary storage path
# For example, I set the bot to save the downloaded file in the current path (the path where config.py file is located).
dl_path = os.path.abspath(os.getcwd()) + '/'


# The upload path where we give FTP access to the bot.
ftp_path = '/earn.22web.org/htdocs/FTPXBot/'

# The files are temporarily downloaded after they are on the bot server. They are uploaded to another host through FTP.
# Here we have to give FTP access to the bot.
ftp_ip = 'ftpupload.net'
ftp_username = 'rigrr_34652687'
ftp_password = 'nrq0pgqv'
ftp_domain = 'http://earn.22web.org/FTPXBot/'
