from handler.users import UserHandler
from handler.messages import MessageHandler
from handler.hashtags import HashtagHandler
from handler.chat import chatHandler
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"

@app.route('/login/')
def log():
    return "No logging!"


##### Routes for Users #####

@app.route('/ChatApp/users')
def getAllUsers():
    return UserHandler().getAllUsers()
        
@app.route('/ChatApp/user=<int:uid>')
def getUserByID(uid):
    return UserHandler().getUserByID(uid)

@app.route('/ChatApp/user=<int:uid>/contacts')
def getAllContactsByID(uid):
    return UserHandler().getAllContactsByID(uid)


##### Routes for Messages #####

@app.route('/ChatApp/messages')
def getAllMessages():
    return MessageHandler().getAllMessages()

@app.route('/ChatApp/message=<int:mid>')
def getMessageByID(mid):
    return MessageHandler().getMessageByID(mid)

@app.route('/ChatApp/messages/user=<int:uid>')
def getAllMessagesByUser(uid):
    return MessageHandler().getAllMessagesByUser(uid)


##### Routes for Hashtags #####

@app.route('/ChatApp/hashtags')
def getAllHashtags():
    return HashtagHandler().getAllHashtags()

@app.route('/ChatApp/hashtags/message=<int:hid>')
def getAllHashtagsByMessage(hid):
    return HashtagHandler().getAllHashtagsByMessage(hid)

@app.route('/ChatApp/hashtags/text=<text>')
def getAllHashtagsByText(text):
    return HashtagHandler().getAllHashtagsByText(text)

### Routes For Chats ####

@app.route('/ChatApp/Chats')
def getAllChats():
    return chatHandler().getAllChats()

@app.route('/ChatApp/Chats/cid=<int:cid>')
def getChatbyID(cid):
    return chatHandler().getChatByID(cid)

@app.route('/ChatApp/Chats/User/user=<int:uid>')
def getChatbyUser(uid):
    return chatHandler().getChatByUser(uid)

@app.route('/ChatApp/Chats/Names/name=<name>')
def getChatbyName(name):
    return chatHandler().getChatByName(name)



if __name__ == '__main__':
    app.run(debug=True)