import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# This script generates a Telethon string session and sends it to the user's Telegram account.
def progress_bar():
    for i in range(0, 101, 10):
        print(f"🔄 Generating string session... {i}% complete", end="\r")
        time.sleep(0.1)
    print("✅ Generating string session... 100% complete")

api_id = int(input("Enter your API ID: "))
api_hash = input("Enter your API Hash: ")

# Show progress before launching client
progress_bar()

with TelegramClient(StringSession(), api_id, api_hash) as client:
    string_session = client.session.save()

    # Send to Telegram
    client.send_message("me", f"✅ **Your Telethon String Session:**\n\n`{string_session}`")

    # Save to file
    with open("telethon_string_session.txt", "w") as f:
        f.write(string_session)

    print("\n✅ String session generated successfully.")
    print("📩 Sent to your Telegram 'Saved Messages'.")
    print("💾 Saved to 'telethon_string_session.txt'.")
