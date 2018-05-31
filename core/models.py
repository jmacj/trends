from peewee import *
from core import config
import datetime

db = MySQLDatabase(
	config.DB_NAME,
	user=config.DB_USER,
	password=config.DB_PASSWORD,
	host=config.DB_HOST
)

class BaseModel(Model):
	class Meta:
		database = db

class Delegates(BaseModel):
	id = PrimaryKeyField(index=True)
	first_name = CharField(max_length=100)
	last_name = CharField(max_length=100)
	email_address = CharField()
	contact_number = CharField()
	is_student = BooleanField()
	school_or_company = CharField(max_length=255)
	course_or_position = CharField(max_length=255)
	created_at = DateTimeField(default=datetime.datetime.now)

def initialize_db():
	db.connect()
	db.create_tables([Delegates], safe=True)

def close_db():
	db.close()