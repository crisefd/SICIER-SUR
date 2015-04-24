from peewee import *

database = PostgresqlDatabase('CIER-SUR', **{})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Course(BaseModel):
    description = CharField()
    end_date = DateField()
    id = CharField(primary_key=True)
    start_date = DateField()

    class Meta:
        db_table = 'course'

class CourseActivity(BaseModel):
    activity = IntegerField()
    id_course_fk = ForeignKeyField(db_column='id_course_fk', rel_model=Course, to_field='id')

    class Meta:
        db_table = 'course_activity'
        primary_key = CompositeKey('activity', 'id_course_fk')

class ActivityGrade(BaseModel):
    activity_fk = ForeignKeyField(db_column='activity_fk', rel_model=CourseActivity, related_name='course_activity_activity_fk_set', to_field='activity')
    id_course_fk = ForeignKeyField(db_column='id_course_fk', rel_model=CourseActivity, related_name='course_activity_id_course_fk_set', to_field='activity')

    class Meta:
        db_table = 'activity_grade'
        primary_key = CompositeKey('activity_fk', 'id_course_fk')

class Administrator(BaseModel):
    city = CharField()
    email = CharField()
    first_name = CharField()
    id = CharField(primary_key=True)
    last_name = CharField()
    tel_num = CharField()

    class Meta:
        db_table = 'administrator'

class Coordinator(BaseModel):
    city = CharField()
    email = CharField()
    first_name = CharField()
    id = CharField(primary_key=True)
    last_name = CharField()
    tel_num = CharField()

    class Meta:
        db_table = 'coordinator'

class CourseCohort(BaseModel):
    cohort = IntegerField()
    id_course_fk = ForeignKeyField(db_column='id_course_fk', rel_model=Course, to_field='id')

    class Meta:
        db_table = 'course_cohort'
        primary_key = CompositeKey('cohort', 'id_course_fk')

class Masterteacher(BaseModel):
    city = CharField()
    email = CharField()
    first_name = CharField()
    id = CharField(primary_key=True)
    last_name = CharField()
    tel_num = CharField()

    class Meta:
        db_table = 'masterteacher'

class Enrollment(BaseModel):
    def_grade = FloatField(null=True)
    id_course_fk = ForeignKeyField(db_column='id_course_fk', rel_model=Course, to_field='id')
    id_mt_fk = ForeignKeyField(db_column='id_mt_fk', rel_model=Masterteacher, to_field='id')

    class Meta:
        db_table = 'enrollment'
        primary_key = CompositeKey('id_course_fk', 'id_mt_fk')

class Leaderteacher(BaseModel):
    city = CharField()
    email = CharField()
    first_name = CharField()
    id = CharField(primary_key=True)
    last_name = CharField()
    tel_num = CharField()

    class Meta:
        db_table = 'leaderteacher'

class LtAcademicBackg(BaseModel):
    id_lt_fk = ForeignKeyField(db_column='id_lt_fk', rel_model=Leaderteacher, to_field='id')
    item = CharField()

    class Meta:
        db_table = 'lt_academic_backg'
        primary_key = CompositeKey('id_lt_fk', 'item')

class LtLaborExp(BaseModel):
    id_lt_fk = ForeignKeyField(db_column='id_lt_fk', rel_model=Leaderteacher, to_field='id')
    item = CharField()

    class Meta:
        db_table = 'lt_labor_exp'
        primary_key = CompositeKey('id_lt_fk', 'item')

class MtAcademicBackg(BaseModel):
    id_mt_fk = ForeignKeyField(db_column='id_mt_fk', rel_model=Masterteacher, to_field='id')
    item = CharField()

    class Meta:
        db_table = 'mt_academic_backg'
        primary_key = CompositeKey('id_mt_fk', 'item')

class MtLaborExp(BaseModel):
    id_mt_fk = ForeignKeyField(db_column='id_mt_fk', rel_model=Masterteacher, to_field='id')
    item = CharField()

    class Meta:
        db_table = 'mt_labor_exp'
        primary_key = CompositeKey('id_mt_fk', 'item')

