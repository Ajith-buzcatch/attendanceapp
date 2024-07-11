from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class NationMaster(models.Model):
    nation = models.CharField(max_length=250, blank=True, null=True)
    
    class Meta:
      db_table  = 'nationmaster'
    
class StateMaster(models.Model):
    nation = models.ForeignKey(NationMaster, on_delete=models.CASCADE, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    
    class Meta:
      db_table  = 'statemaster'
    
class CityMaster(models.Model):
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    
    class Meta:
      db_table  = 'citymaster'
    
class DepartmentMaster(models.Model):
    department = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
      db_table  = 'departmentmaster'
    
class DesignationMaster(models.Model):
    designation = models.CharField(max_length=250, blank=True, null=True)
    
    class Meta:
      db_table  = 'designationmaster'
      
    

class CompanyDetails(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.ForeignKey(CityMaster, on_delete=models.CASCADE, blank=True, null=True)
    reg_no = models.CharField(max_length=100, blank=True, null=True)
    company_icon = models.ImageField(upload_to='company_images', blank=True, null=True)
    company_logo = models.ImageField(upload_to='company_images',blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
      db_table  = 'companydetails'

class EmployeeMaster(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='employees', blank=True, null=True)
    employee_code = models.CharField(max_length=50, blank=True, null=True)
    employee_name = models.CharField(max_length=250, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.ForeignKey(CityMaster,on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE, blank=True, null=True)
     
    class Meta:
      db_table  = 'employeemaster'
   
class EmployeeDepartment(models.Model):
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(DepartmentMaster,on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
      db_table  = 'employeedepartment'
    
class EmployeeDesignation(models.Model):
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE, blank=True, null=True)
    designation = models.ForeignKey(DesignationMaster,on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
      db_table  = 'employeedesignation'
    
class EmployeeImage(models.Model):
    employee = models.ForeignKey(EmployeeMaster,related_name='employee_images', on_delete=models.CASCADE, blank=True, null=True)
    employee_image = models.ImageField(blank=True,null=True,upload_to='employee_images')
    
    class Meta:
      db_table  = 'employeeimage'
      
class AttendanceMaster(models.Model):
    Slno = models.IntegerField(null=True, blank=True)
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE, blank=True, null=True)
    login_datetime = models.DateTimeField(blank=True, null=True)
    logout_datetime = models.DateTimeField(blank=True, null=True)
    login_ipaddress = models.CharField(max_length=1000, null=True, blank=True)
    logout_ipaddress = models.CharField(max_length=1000, null=True, blank=True)
    is_pending_approval = models.BooleanField(default=False)
    
    class Meta:
      db_table  = 'attendancemaster'
    
class RoleMaster(models.Model):
    role = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
      db_table  = 'rolemaster'
      
class EmployeeJoinMaster(models.Model):
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE, blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)
    role = models.ForeignKey(RoleMaster,on_delete=models.CASCADE, blank=True, null=True)
    
    
    class Meta:
      db_table  = 'employeejoinmaster'
      
class WorkingTime(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    class Meta:
      db_table  = 'workingtime'
      
class TimeBreakMaster(models.Model):
    tbreak = models.CharField(max_length=30)
      
    class Meta:
      db_table  = 'timebreakmaster'
      
class ForgotCheckIn(models.Model):
  company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True, blank=True)
  employee = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE, null=True,blank=True)
  current_time = models.DateTimeField(blank=True, null=True)
  normal_login_time = models.DateTimeField(blank=True,null=True)
  status = models.CharField(max_length=15,null=True,blank=True)
  reason = models.TextField(null=True,blank=True)
  location = models.CharField(max_length=500,null=True,blank=True)
  
  class Meta:
      db_table  = 'forgotcheckin'
      
class LeaveMaster(models.Model):
  leaves = models.CharField(max_length =30,null=True,blank=True)
  
  class Meta:
    db_table = 'leavemaster'
    
class LeaveEnquiry(models.Model):
  STATUS_CHOICES = (
      (0, 'Pending'),
      (1, 'Approved'),
      (2, 'Rejected'),
      (3, 'Cancelled'),
  )
  Slno = models.IntegerField(null=True,blank=True)
  company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True, blank=True)
  employee = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE, null=True,blank=True)
  submitted_to_user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
  leave = models.ForeignKey(LeaveMaster,on_delete=models.CASCADE, null=True,blank=True)
  from_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  enquery_date = models.DateTimeField(null=True, blank=True)
  status = models.IntegerField(choices=STATUS_CHOICES, default=0)
  reason = models.TextField(null=True,blank=True)
  half_day_option = models.TextField(null=True,blank=True)
  class Meta:
    db_table = 'leaveenquiry'
    
      
class ApprovedLeave(models.Model):
  Slno = models.IntegerField(null=True,blank=True)
  leave_enquiry = models.ForeignKey(LeaveEnquiry,on_delete=models.CASCADE,null=True, blank=True)
  from_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  approved_date = models.DateField(null=True, blank=True)
  approved_employee = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE, null=True,blank=True)
  
  class Meta:
    db_table = 'approvedleave'
    
class AddLeave(models.Model):
  company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True, blank=True)
  employee = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE, null=True,blank=True)
  leave = models.ForeignKey(LeaveMaster,on_delete=models.CASCADE, null=True,blank=True)
  leave_balance = models.IntegerField(default=0,null=True,blank=True)
  available_leave_balance = models.FloatField(null=True,blank=True)
  class Meta:
    db_table = 'addleave'
    
class EmployeeProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, null=True, blank=True)
    personal_mail = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES,null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)
    nationality = models.CharField(max_length=100,null=True, blank=True)
    identification_no = models.CharField(max_length=100, null=True, blank=True)
    field_of_study = models.CharField(max_length=100, null=True, blank=True)
    school = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_person = models.CharField(max_length=100, null=True, blank=True)
    emergency_phone = models.CharField(max_length=15, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    skill_1 = models.CharField(max_length=255, null=True, blank=True)
    skill_2 = models.CharField(max_length=255, null=True, blank=True)
    skill_3 = models.CharField(max_length=255, null=True, blank=True)
    skill_4 = models.CharField(max_length=255, null=True, blank=True)
    skill_5 = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
      db_table = 'employeeprofile'
      
      
class BankDetails(models.Model):
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    branch_address = models.CharField(max_length=255)
    
    class Meta:
      db_table = 'bankdetails'

    def __str__(self):
        return f"{self.employee.user.username}'s Bank Details"