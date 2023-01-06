from telethon.sync import TelegramClient
from data import api_id, api_hash, phone_number

client = TelegramClient(phone_number, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))


def get_channel_id(name):
    for dialog in client.iter_dialogs():
        if dialog.name == name:
            return dialog.id


def main():
    return [user.id for user in client.iter_participants(entity=get_channel_id('димончик'))]


if __name__ == '__main__':
    print(main())
