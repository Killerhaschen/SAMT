import asyncio

from marvin import Marvin, Answer, Context, Mode

marv = Marvin()

#Put here Your Own TelegramID
# It can be a string or an int
userID=22237162

@marv.answer("/start")
async def start():
    return Answer('greeting', Context.get('user'))

@marv.on_startup
async def testLoop():
    while True:
        #Define a message that we want to send
        a=Answer('greeting', "user", receiver=userID)
        # yield it to marvin
        yield a
        #wait 10 seconds
        await asyncio.sleep(10)

if __name__ == "__main__":
    marv.listen()