import os
import mailbox

# Path to your mbox file
mbox_path = "/home/mcode/Downloads/takeout-20250928T075616Z-1-001/Takeout/Mail/Inbox.mbox"

# Directory to save attachments
output_dir = "/home/mcode/Downloads/takeout-20250928T075616Z-1-001/Takeout/attachments"
os.makedirs(output_dir, exist_ok=True)

# Open the mbox
mbox = mailbox.mbox(mbox_path)

for i, message in enumerate(mbox):
    if message.is_multipart():
        for part in message.walk():
            # Look for attachments
            if part.get_content_disposition() == "attachment":
                filename = part.get_filename()
                if not filename:
                    filename = f"attachment_{i}.bin"

                filepath = os.path.join(output_dir, filename)

                # Save the attachment
                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))

                print(f"Saved: {filepath}")

