async def spam():
    global answer
    user = str(input("\nUser_id:"))
    msg = str(input("\nMessage:"))
    msgnumber = int(input("\nHow many messages?"))
    for i in range(msgnumber):
        await dlient.send_message(discord.User(id=user), msg)
    print("Successful spam. Your target is now aching in pain and anger. Good job keyboard warrior.\n")
    answer = str(input("\n You want sum more?*yes*, *no*:\n"))

