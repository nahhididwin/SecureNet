# SNet (SecureNet)
Multi-device data transmission network, connecting devices together, highly secure, fully customizable.

# Index
x

# How to use? (if used with ngrok)

Suppose there is computer A and computer B.

**On computer A:**

Open CMD first, move to the folder containing the file "chat_server.py" (using "cd").

then type "python chat_server.py" in CMD.

Open second CMD,type "ngrok http 5000" in CMD.

Look for the Forwarding line with the address https://...ngrok-free.app. This is the public web address of computer A.

Copy the ngrok address of Computer A.

**On computer B:**

Do exactly the same as Computer A. Computer B will also have its own ngrok address.

Copy the ngrok address of Computer B.


**On computer A:**

Open the chat_client.py file, Find the line PARTNER_NGROK_URL and paste the ngrok address of computer B into it. Save the file.

**On computer B:**

Open the chat_client.py file, Find the line PARTNER_NGROK_URL and paste the ngrok address of computer A into it. Save the file.

**Open a third CMD on both computers:**

Move to the folder containing the code.

Run the client program: "python chat_client.py"

#


