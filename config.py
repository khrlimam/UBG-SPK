import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", 'sqlite:///test.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

THREADS_PER_PAGE = 2

APP_NAME = 'BestApp'

SECRET_KEY = "cBWegL8d367vPzTp9Y2pJudLLtaKi5Jtw8//WsRjZrc="

#twitter
ACCESS_TOKEN_SECRET = "7Wz1rwrLncyqiHJLaTkBYfIdNFUK55UpVGLJdYJSGIGui"
ACCESS_TOKEN = "1140536422610264064-0f3EpuyoZnFwo3UgsdHDFhcm5axHGv"
API_SECRET = "RbW4L7CPazk4c3OLhs8vdZDacoAEbAA8n4w7HhI1Rr8tZTJcti"
API_KEY = "u95VwtIDBhYKDL7mU969vZCDK"