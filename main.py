import asyncio
from telethon import TelegramClient, events

async def main():
    event = asyncio.Event()
    bot_token = '6505849033:AAErhVKQ_3aoXPt5V_PYBvMMXnUiqI7ZNc0'
    print("work")
    # Initialize Telegram Client
    client = TelegramClient('yuh' + bot_token, "28905453", "21073abfe2bf0652881caf8ec8f104e4")
    await client.start(bot_token=bot_token)
    print("launched")
    bot_chat_id = 6505849033  # If this is a bot, ensure it's the correct chat_id format

    @client.on(events.NewMessage(chats=bot_chat_id))
    async def my_event_handler(event):
        # Make sure 'from_id' is available and valid
        if event.message.from_id and event.message.from_id.user_id == bot_chat_id:
            # Check for advertisement keywords (case insensitive)
            message_text = event.message.message.lower()
            if '#ad' in message_text or '#paidad' in message_text or 'sponsored' in message_text:
                print(event)
                
                # Delete the message if conditions are met
                await client.delete_messages(event.message.peer_id.user_id, event.message.id)
                print('Message deleted successfully')
            else:
                print('No matching advertisement keywords')
        else:
            print('Message not from the bot')
    
    client.add_event_handler(my_event_handler)
    
    while True:
        await event.wait()
        event.clear()

# Entry point of the script
if __name__ ==
 '__main__':
    asyncio.run(main())
