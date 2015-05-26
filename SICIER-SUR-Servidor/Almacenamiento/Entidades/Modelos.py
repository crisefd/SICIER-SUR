from peewee import *

database = PostgresqlDatabase('cier_sur', **{})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Leaderteacher(BaseModel):
    area = CharField()
    birth_date = DateField()
    city = CharField()
    department = CharField()
    email = CharField(unique=True)
    first_name = CharField()
    grade = CharField()
    id = CharField(primary_key=True)
    institution = CharField()
    is_active = BooleanField()
    last_name = CharField()
    marital_status = CharField()
    pass_ = CharField(db_column='pass', null=True)
    secretariat = CharField()
    sex = CharField()
    tel_num = CharField()

    class Meta:
        db_table = 'leaderteacher'

class Course(BaseModel):
    description = CharField()
    end_date = DateField()
    id = CharField(primary_key=True)
    start_date = DateField()

    class Meta:
        db_table = 'course'

class CourseActivity(BaseModel):
    activity = CharField(primary_key=True)
    end_date = DateField()
    id_course_fk = ForeignKeyField(db_column='id_course_fk', rel_model=Course, to_field='id')
    start_date = DateField()
    weight = FloatField()

    class Meta:
        db_table = 'course_activity'

class ActivityGradeLt(BaseModel):
    activity_fk = ForeignKeyField(db_column='activity_fk', rel_model=CourseActivity, to_field='activity')
    id_lt_fk = ForeignKeyField(db_column='id_lt_fk', rel_model=Leaderteacher, to_field='id')
    score = FloatField(null=True)

    class Meta:
        db_table = 'activity_grade_lt'
        primary_key = CompositeKey('activity_fk', 'id_lt_fk')

class Administrator(BaseModel):
    city = CharField()
    email = CharField(unique=True)
    first_name = CharField()
    id = CharField(primary_key=True)
    is_active = BooleanField()
    last_name = CharField()
    pass_ = CharField(db_column='pass', null=True)
    tel_num = CharField()

    class Meta:
        db_table = 'administrator'

class Coordinator(BaseModel):
    city = CharField()
    email = CharField(unique=True)
    first_name = CharField()
    id = CharField(primary_key=True)
    is_active = BooleanField()
    last_name = CharField()
    pass_ = CharField(db_column='pass', null=True)
    tel_num = CharField()

    class Meta:
        db_table = 'coordinator'

class CourseCohort(BaseModel):
    cohort = CharField()
    id_course_fk = ForeignKeyField(db_column='id_course_fk', rel_model=Course, to_field='id')

    class Meta:
        db_table = 'course_cohort'
        primary_key = CompositeKey('cohort', 'id_course_fk')

class Masterteacher(BaseModel):
    area = CharField()
    birth_date = DateField()
    city = CharField()
    email = CharField(unique=True)
    first_name = CharField()
    grade = CharField()
    id = CharField(primary_key=True)
    institution = CharField()
    is_active = BooleanField()
    last_name = CharField()
    marital_status = CharField()
    pass_ = CharField(db_column='pass', null=True)
    secretariat = CharField()
    sex = CharField()
    tel_num = CharField()

    class Meta:
        db_table = 'masterteacher'

class Enrollment(BaseModel):
    def_grade = FloatField(null=True)
    id_course_fk = ForeignKeyField(db_column='id_course_fk', rel_model=Course, to_field='id')
    id_lt_fk = ForeignKeyField(db_column='id_lt_fk', rel_model=Leaderteacher, to_field='id')
    id_mt_fk = ForeignKeyField(db_column='id_mt_fk', rel_model=Masterteacher, to_field='id')

    class Meta:
        db_table = 'enrollment'
        primary_key = CompositeKey('id_course_fk', 'id_mt_fk')

class LtAcademicBackg(BaseModel):
    id_lt_fk = ForeignKeyField(db_column='id_lt_fk', rel_model=Leaderteacher, to_field='id')
    item = CharField()

    class Meta:
        db_table = 'lt_academic_backg'
        primary_key = CompositeKey('id_lt_fk', 'item')

class LtCohort(BaseModel):
    cohort_fk = ForeignKeyField(db_column='cohort_fk', rel_model=CourseCohort, related_name='course_cohort_cohort_fk_set', to_field='cohort')
    id_course_fk = ForeignKeyField(db_column='id_course_fk', rel_model=CourseCohort, related_name='course_cohort_id_course_fk_set', to_field='cohort')
    id_lt_fk = ForeignKeyField(db_column='id_lt_fk', rel_model=Leaderteacher, to_field='id')

    class Meta:
        db_table = 'lt_cohort'
        primary_key = CompositeKey('cohort_fk', 'id_course_fk', 'id_lt_fk')

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

