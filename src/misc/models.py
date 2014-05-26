from django.db import models

GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Transgender','Transgender'),    
    ('Unknown','Unknown'),        
    )

QUALIFICATION =(
    ('SSLC','SSLC'),
    ('Unknown','Unknown'),
)

ATTENDANCE =(
    ('Present','Present'),
    ('Absent','Absent'),
    ('N.A','N.A'),
)

class Representative(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.name, self.key)
    name            = models.CharField(max_length=200,blank=False,null=False)
    name_l          = models.CharField(max_length=200,blank=True,null=True)
    key             = models.CharField(max_length=200,blank=False,null=False,unique=True)
    gender          = models.CharField(max_length=15,choices=GENDER,default='Unknown')
    birth_year      = models.IntegerField(default=0,null=True,blank=True)
    has_picture     = models.BooleanField(default=False)
    qualification   = models.CharField(max_length=100,choices=QUALIFICATION,default='Unknown')
    all_time_attendance_percentage    = models.DecimalField(max_digits=4, decimal_places=2,blank=True,null=True)
    all_time_no_questions_asked       = models.DecimalField(max_digits=4, decimal_places=2,blank=True,null=True)

class Constituency(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.name, self.key)
    name            = models.CharField(max_length=200,blank=False,null=False)
    name_l          = models.CharField(max_length=200,blank=True,null=True)
    key             = models.CharField(max_length=200,blank=False,null=False,unique=True)
    number          = models.IntegerField(default=0,null=True,blank=True)

class Assembly(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.name, self.key)
    name            = models.CharField(max_length=200,blank=False,null=False)
    name_l          = models.CharField(max_length=200,blank=True,null=True)
    key             = models.CharField(max_length=200,blank=False,null=False,unique=True)
    start           = models.DateField(blank=True,null=True,default = None) 
    end             = models.DateField(blank=True,null=True,default = None) 


class Role(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.name, self.key)
    name            = models.CharField(max_length=100,blank=False,null=False)
    name_l          = models.CharField(max_length=100,blank=True,null=True)
    key             = models.CharField(max_length=200,blank=False,null=False,unique=True)
    weightage       = models.IntegerField(default=0,null=True,blank=True)

class Party(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.name, self.key)
    name            = models.CharField(max_length=200,blank=False,null=False)
    name_l          = models.CharField(max_length=200,blank=True,null=True)
    short_name      = models.CharField(max_length=50,blank=False,null=False)
    short_name_l    = models.CharField(max_length=50,blank=False,null=True)
    key             = models.CharField(max_length=200,blank=False,null=False,unique=True)


class RepRole(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.representative.name, self.role.name)
    representative             =  models.ForeignKey(Representative) 
    constituency               =  models.ForeignKey(Constituency) 
    party                      =  models.ForeignKey(Party) 
    assembly                   =  models.ForeignKey(Assembly) 
    role                       =  models.ForeignKey(Role) 
    start                      =  models.DateField(blank=True,null=True,default = None) 
    end                        =  models.DateField(blank=True,null=True,default = None) 
    has_ec_affidavit           = models.BooleanField(default=False)

class Session(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.name, self.key)
    name                    = models.CharField(max_length=200,blank=False,null=False)
    name_l                  = models.CharField(max_length=200,blank=True,null=True)
    key                     = models.CharField(max_length=200,blank=False,null=False,unique=True)
    start                   = models.DateField(blank=True,null=True,default = None) 
    end                     = models.DateField(blank=True,null=True,default = None) 
    assembly                =  models.ForeignKey(Assembly) 
    total_working_days      = models.IntegerField(default=0,null=True,blank=True)
    average_member_attendance = models.DecimalField(max_digits=4, decimal_places=2,blank=True,null=True)


class Attendance(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.representative.name, self.role.name)
    representative              =  models.ForeignKey(Representative) 
    session                     =  models.ForeignKey(Session) 
    repRole                     =  models.ForeignKey(RepRole) 
    date                        =  models.DateField(blank=True,null=True,default = None) 
    attendance                  =  models.CharField(max_length=100,choices=ATTENDANCE,default='Unknown')


class Department(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.name, self.key)
    name            = models.CharField(max_length=100,blank=False,null=False)
    name_l          = models.CharField(max_length=100,blank=True,null=True)
    key             = models.CharField(max_length=200,blank=False,null=False,unique=True)

class Question(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.question)
    session                     =  models.ForeignKey(Session) 
    representative              =  models.ForeignKey(Representative) 
    department                  =  models.ForeignKey(Department) 
    date                        =  models.DateField(blank=True,null=True,default = None) 
    question                    =  models.CharField(max_length=2000)         