import motor

client = motor.motor_tornado.MotorClient(
   "mongodb+srv://admin:admin@ffcluster.8zf8y.mongodb.net/db?retryWrites=true&w=majority")
db = client.db
crslt = db.crslt
users = db.users

