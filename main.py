# So we are going to see the code on how we can send bulk message in telegram to any group or friends. #PS: creating this file only for educational purpose. Use this code carefully, dont harrass others.


# Import essentials
from telethon.sync import TelegramClient

# Your API details and credentials
# You can visit this site to gain access to your API credentials -> https://my.telegram.org/auth

api_id = 'Your api id'
api_hash = 'Your hash value' # you will find this on the above mentioned site.

# Provide your friend's username # remove @ from username

f_username = 'Your friend username'

# Now create a telegram client

client = TelegramClient('my_session',api_id,api_hash)

async def main_function():
    await client.start()

    for _ in range(20):
        await client.send_message(f_username, 'Hellloo from Nayan! This message is send by from python')

        await client.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main_function())
