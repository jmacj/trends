from peewee import *
from core import config

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
	first_name = CharField(max_length=50)
	last_name = CharField(max_length=50)
	email = CharField()
	contact_number = CharField()
	is_student = BooleanField()
	school_or_company = CharField(max_length=255)
	course_or_position = CharField(max_length=255)
	created_at = DateTimeField(constraints=[SQL('NOT NULL DEFAULT CURRENT_TIMESTAMP')])
	updated_at = DateTimeField(constraints=[SQL('NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')])

def initialize_db():
	db.connect()
	db.create_tables([Delegates], safe=True)

def close_db():
	db.close()