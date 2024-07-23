from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import UserType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.cache import cache
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model() 
AUTH_USER_MODEL = 'attendance_app.User'
from master.models import *
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.timezone import localtime, timedelta, now
import requests
from datetime import datetime
from django.http import JsonResponse
import json
from django.utils.formats import get_format
from django.http import HttpResponse,HttpResponseRedirect
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.core.exceptions import ObjectDoesNotExist
from twilio.rest import Client
import random
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.utils.dateparse import parse_date, parse_datetime
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from django.db.models import Prefetch
import pytz
from django.views.decorators.csrf import csrf_exempt
# def login_redirect(request):
#     if request.user.is_authenticated:
#         return redirect('admin_index')
#     return redirect('employee_login')

def admin_logout(request):
    logout(request)
    return redirect('employee_login')

@login_required
def admin_index(request):
    try:
        # Fetch the company details of the logged-in user
        company = CompanyDetails.objects.get(user=request.user)
        # Fetch all employees linked to this company
        employees = EmployeeJoinMaster.objects.filter(company=company).select_related('employee')
        
        leaves = LeaveEnquiry.objects.filter(company=company, status=0)
         
        for employee in employees:
            employee.images = EmployeeImage.objects.filter(employee=employee.employee)
        employee_count = employees.count() #count the number of employees
        leave_count = leaves.count()
        
    except CompanyDetails.DoesNotExist:
        employees = []  # Handle case where company details are not found
        employee_count = 0 # No employees if company details are not found
        leave_count = 0
        
    context = {
        'leave_count': leave_count,
        'employees': employees,
        'employee_count': employee_count
    }
    
    return render(request, 'company_admin/index.html', context)

@login_required
def CompanyProfile(request):
    try:
        company_profile = CompanyDetails.objects.get(user=request.user)
    except CompanyDetails.DoesNotExist:
        company_profile = None
        
    context = {
        'company_profile': company_profile
    }
        
    return render(request,'company_admin/company_profile.html',context)

@login_required
def EditCompanyProfile(request):
    company = get_object_or_404(CompanyDetails, user=request.user)
    if request.method == 'POST':
        company.company_name = request.POST.get('company_name')
        company.address = request.POST.get('address')
        company.city_id = request.POST.get('city')
        company.reg_no = request.POST.get('reg_no')
        if 'company_icon' in request.FILES:
            company.company_icon = request.FILES['company_icon']
        if 'company_logo' in request.FILES:
            company.company_logo = request.FILES['company_logo']
        company.save()
        return redirect('company_profile')
    
    cities = CityMaster.objects.all()
    return render(request, 'company_admin/edit_company_profile.html', {'company': company, 'cities': cities})



@login_required
def user_add(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']
        repeat_password = request.POST['rpass']
        email = request.POST['email']
        contact_no = request.POST['mobno']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address1 = request.POST['address1']
        city_id = request.POST['city']
        state_id = request.POST['state']
        nation_id = request.POST['country']
        department_id = request.POST['department']
        designation_id = request.POST['designation']
        employee_image = request.FILES['profile_pic']
        employee_code = request.POST['employee_card_id']
        joining_date = request.POST['joining_date']
        role_id = request.POST['role']

        if password != repeat_password:
            messages.error(request, "Passwords do not match")
            return redirect('useradd')

        try:
            usertype = UserType.objects.get(usertype='Employee')
            city = CityMaster.objects.get(id=city_id)
            state = StateMaster.objects.get(id=state_id)
            nation = NationMaster.objects.get(id=nation_id)
            department = DepartmentMaster.objects.get(id=department_id)
            designation = DesignationMaster.objects.get(id=designation_id)
            role = RoleMaster.objects.get(id=role_id)
            
            # Get the company associated with the logged-in admin user
            company = CompanyDetails.objects.get(user=request.user)
            
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                contact_no=contact_no,
                usertype=usertype,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            employee = EmployeeMaster.objects.create(
                employee_code=employee_code,
                user=user,
                employee_name=f"{first_name} {last_name}",
                address=address1,
                city=city,
                company=company
            )

            EmployeeDepartment.objects.create(
                employee=employee,
                department=department,
                company=company
            )
            EmployeeDesignation.objects.create(
                employee=employee,
                designation=designation,
                company=company
            )
            EmployeeImage.objects.create(
                employee=employee,
                employee_image=employee_image
            )
            EmployeeJoinMaster.objects.create(
                join_date=joining_date,
                employee=employee,
                company=company,  # Store the company in EmployeeJoinMaster
                role=role
            )

            messages.success(request, "User created successfully")
            return redirect('useradd')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('useradd')

    usertypes = UserType.objects.all()
    nations = NationMaster.objects.all()
    states = StateMaster.objects.all()
    cities = CityMaster.objects.all()
    departments = DepartmentMaster.objects.all()
    designations = DesignationMaster.objects.all()
    roles = RoleMaster.objects.all()
    
    return render(request, 'company_admin/user-add.html', {
        'usertypes': usertypes,
        'nations': nations,
        'states': states,
        'cities': cities,
        'departments': departments,
        'designations': designations,
        'roles': roles
    })
    

@login_required
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    employee = get_object_or_404(EmployeeMaster, user=user)

    if request.method == 'POST':
        user.username = request.POST['uname']
        if 'pass' in request.POST and request.POST['pass']:
            if request.POST['pass'] == request.POST['rpass']:
                user.password = make_password(request.POST['pass'])
            else:
                messages.error(request, "Passwords do not match")
                return redirect('useredit', user_id=user_id)
        user.email = request.POST['email']
        user.contact_no = request.POST['mobno']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']

        employee.address = request.POST['address1']
        employee.city = CityMaster.objects.get(id=request.POST['city'])
        #employee.role = RoleMaster.objects.get(id=request.POST['role'])
        employee.employee_code = request.POST['employee_card_id']
        employee.employee_name = f"{user.first_name} {user.last_name}"
        if 'profile_pic' in request.FILES:
            employee_image = EmployeeImage.objects.get(employee=employee)
            employee_image.employee_image = request.FILES['profile_pic']
            employee_image.save()
            
        # Update role
        

        user.save()
        employee.save()

        # messages.success(request, "User updated successfully")
        return redirect('userlist')

    usertypes = UserType.objects.all()
    nations = NationMaster.objects.all()
    states = StateMaster.objects.all()
    cities = CityMaster.objects.all()
    departments = DepartmentMaster.objects.all()
    designations = DesignationMaster.objects.all()
    roles = RoleMaster.objects.all()
    employee_image = EmployeeImage.objects.filter(employee=employee).first()
    
    context = {
        'user': user,
        'employee_image': employee_image,
        'employee': employee,
        'usertypes': usertypes,
        'nations': nations,
        'states': states,
        'cities': cities,
        'departments': departments,
        'designations': designations,
        'roles': roles,
    }
    return render(request, 'company_admin/user-edit.html', context)

@login_required
def user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    employee = get_object_or_404(EmployeeMaster, user=user)
    employee_department = EmployeeDepartment.objects.filter(employee=employee).first()
    employee_designation = EmployeeDesignation.objects.filter(employee=employee).first()
    employee_image = EmployeeImage.objects.filter(employee=employee).first()
    employee_join = EmployeeJoinMaster.objects.filter(employee=employee).first()
    work_time = WorkingTime.objects.filter(user=user).first()
    personal_info = EmployeeProfile.objects.filter(employee=employee).first()
    bank_details = BankDetails.objects.filter(employee=employee).first()
    context = {
        'user': user,
        'employee': employee,
        'employee_department': employee_department,
        'employee_designation': employee_designation,
        'employee_image': employee_image,
        'employee_join': employee_join,
        'work_time': work_time,
        'personal_info': personal_info,
        'bank_details' : bank_details
    }
    return render(request, 'company_admin/user-view.html', context)
    
@login_required
def user_list(request):
    try:
        # Get the company associated with the logged-in admin
        admin_company = CompanyDetails.objects.get(user=request.user)
        
        # Filter users who are employees under the admin's company
        users = User.objects.filter(
            employees__employeejoinmaster__company=admin_company
        ).prefetch_related(
            'employees__city__state__nation',
            'employees__employeejoinmaster_set__company',
            'employees__employee_images'
        ).exclude(is_superuser=True).distinct()

        return render(request, 'company_admin/user-list.html', {'users': users})

    except CompanyDetails.DoesNotExist:
        # Handle the case where the logged-in user is not associated with any company
        messages.error(request, "You are not associated with any company.")
        return redirect('admin_index')


@login_required
def UserDelete(request, user_id):
    try:
        # Retrieve the user and their associated records
        user = User.objects.get(id=user_id)
        employee = EmployeeMaster.objects.get(user=user)
        
        # Deleting related records
        EmployeeDepartment.objects.filter(employee=employee).delete()
        EmployeeDesignation.objects.filter(employee=employee).delete()
        EmployeeImage.objects.filter(employee=employee).delete()
        EmployeeJoinMaster.objects.filter(employee=employee).delete()
        
        # Finally, delete the employee and user records
        employee.delete()
        user.delete()
        
        messages.success(request, "User deleted successfully")
    except User.DoesNotExist:
        messages.error(request, "User does not exist")
    except EmployeeMaster.DoesNotExist:
        messages.error(request, "Employee does not exist")
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
    
    return redirect('userlist')

@login_required
def WorkTime(request):
    company = CompanyDetails.objects.get(user=request.user)
    employee_joins = EmployeeJoinMaster.objects.filter(company=company)
    employees = [join.employee for join in employee_joins]

    if request.method == 'POST':
        user_id = request.POST.get('user')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        user = User.objects.get(id=user_id)
        
        work_time = WorkingTime(
            user=user,
            company=company,
            start_time=start_time,
            end_time=end_time
        )
        work_time.save()
        return redirect('worktime')  # Redirect to the same page or another page

    context = {
        'employees': employees,
    }
    return render(request, 'company_admin/work-time.html', context)

@login_required
def attendance_overview(request):
    # Assuming you have a way to identify the logged-in user (company admin)
    logged_in_user = request.user
    
    # Fetch the company associated with the logged-in user
    company = logged_in_user.companydetails_set.first()
    
    # Fetch attendance records for employees belonging to the company
    attendance_records = AttendanceMaster.objects.filter(company=company).order_by('-login_datetime')
    print ('attendance_records')
    for record in attendance_records:
        print(f'Employee: {record.employee.employee_name}, Login: {record.login_datetime}, Logout: {record.logout_datetime}')
        
        # Calculate working hours if both check-in and check-out times are available
        if record.login_datetime and record.logout_datetime:
            working_hours = record.logout_datetime - record.login_datetime
            hours, remainder = divmod(working_hours.total_seconds(), 3600)
            minutes, _ = divmod(remainder, 60)
            record.working_hours = "{:02}:{:02}".format(int(hours), int(minutes))

    context = {
        'attendance_records': attendance_records,
    }
    
    return render(request, 'company_admin/attendance1.html', context)

@login_required(login_url='employee_login')
def add_leave_balance(request):
    company = CompanyDetails.objects.get(user=request.user)
    employees = EmployeeMaster.objects.filter(company=company)
    leave_types = LeaveMaster.objects.all()

    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        leave_balances = {leave.id: request.POST.get(f'leave_{leave.id}') for leave in leave_types}

        employee = EmployeeMaster.objects.get(id=employee_id)

        for leave_id, balance in leave_balances.items():
            
            if balance is None or balance =='':
                balance = 0
            else:
                balance = float(balance)
                
            leave_record, created = AddLeave.objects.get_or_create(
                employee=employee,
                leave_id=leave_id,
                company=company,
                defaults={'leave_balance': balance, 'available_leave_balance': balance}
            )
            
            if not created:
                leave_record.leave_balance += balance
                leave_record.available_leave_balance += balance
                leave_record.save()

        return redirect('add_leave_balance')

    context = {
        'employees': employees,
        'leave_types': leave_types
    }
    return render(request, 'company_admin/add_leave.html', context)


@login_required(login_url='employee_login')
def get_leave_balances(request, employee_id):
    employee = EmployeeMaster.objects.get(id=employee_id)
    leave_types = LeaveMaster.objects.all()
    leave_balances = AddLeave.objects.filter(employee=employee)
    
    leave_balance_dict = {leave.leave.id: leave.available_leave_balance for leave in leave_balances}
    data = {
        'leave_balances': [
            {
                'leave_id': leave.id,
                'leave_name': leave.leaves,
                'available_balance': leave_balance_dict.get(leave.id, 0),
            } for leave in leave_types
        ]
    }
    return JsonResponse(data)


@login_required
def LeaveRequest(request):
    
    company = CompanyDetails.objects.get(user=request.user)
    leave_requests = LeaveEnquiry.objects.filter(company=company).order_by('-enquery_date')
   
    
    for leave_request in leave_requests:
        if leave_request.from_date and leave_request.end_date:
            days = (leave_request.end_date - leave_request.from_date).days + 1
            if leave_request.half_day_option:
                if leave_request.from_date == leave_request.end_date:
                    days = 0.5 #half day leave
                else:
                    days -= 0.5 #deduct half day if any day is half-day leave
           
        else:
            days = 0
        
        leave_request.total_days = days
    return render(request, 'company_admin/leave_req.html', {'leave_requests': leave_requests})
    
@login_required
def process_leave_request(request, leave_enquiry_id, action):
    leave_enquiry = get_object_or_404(LeaveEnquiry, id=leave_enquiry_id)
    
    if action == 'approve':
        if leave_enquiry.status != 1:
            # Calculate the duration of the leave request
            leave_duration = (leave_enquiry.end_date - leave_enquiry.from_date).days + 1
            if leave_enquiry.half_day_option:
                if leave_enquiry.from_date == leave_enquiry.end_date:
                    leave_duration = 0.5  # Half day leave
                else:
                    leave_duration -= 0.5  # Deduct half day if any day is half-day leave
            
            # Retrieve or create the AddLeave record to update available leave balance
            try:
                add_leave_record = AddLeave.objects.get(employee=leave_enquiry.employee, leave=leave_enquiry.leave)
            except AddLeave.DoesNotExist:
                add_leave_record = AddLeave.objects.create(
                    employee=leave_enquiry.employee,
                    leave=leave_enquiry.leave,
                    company=leave_enquiry.company,
                    leave_balance=0,
                    available_leave_balance=0
                )
            
            # Update available leave balance
            add_leave_record.available_leave_balance -= leave_duration
            add_leave_record.save()
            
            # Create an ApprovedLeave record
            ApprovedLeave.objects.create(
                leave_enquiry=leave_enquiry,
                from_date=leave_enquiry.from_date,
                end_date=leave_enquiry.end_date,
                approved_date=timezone.now().date(),
                approved_employee=leave_enquiry.employee
            )
            
            leave_enquiry.status = 1  # Set status to Approved
            leave_enquiry.save()
            messages.success(request, 'Leave request approved successfully.')
            
    elif action == 'reject':
        if leave_enquiry.status != 2:
            leave_enquiry.status = 2  # Set status to Rejected
            leave_enquiry.save()
            messages.success(request, 'Leave request rejected successfully.')
    
    return redirect('leave_request')

# EMPLOYEE VIEW SECTION

@cache_control(no_cache=True, must_revalidate=True)
def employee_login(request):
    error_message = None
    
    if request.user.is_authenticated:
        # Redirect based on user type
        if request.user.usertype.id == 1:
            return redirect('admin_index')
        elif request.user.usertype.id == 2:
            return redirect('employee_index')
        
    if request.method == 'POST':
        mailid = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=mailid, password=password)
        if user is not None:
            login(request, user)
            if user.usertype.id == 1:
                return redirect('admin_index')
            elif user.usertype.id == 2:
                return redirect('employee_index')
        else:
            error_message = 'Invalid email or password.'
    
    return render(request, 'employee/login.html', {'error_message': error_message})

@cache_control(no_cache=True, must_revalidate=True)
def employee_logout(request):
    logout(request)
    cache.clear()
    
    #messages.success(request,'You Have Successfully Logged Out.')
    return redirect('employee_login')



def get_location_from_coordinates(latitude, longitude):
    geolocator = Nominatim(user_agent="employee_app", timeout=10)  # Increased timeout to 10 seconds
    try:
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        if location:
            address_parts = location.address.split(',')
            if len(address_parts) > 3:
                # Remove state, district, and country
                formatted_address = ', '.join(address_parts[:-4])
            else:
                formatted_address = location.address
            return formatted_address
        else:
            return "Unknown location"
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Geocoding error: {e}")
        return "Geocoding service unavailable"
    
    
@login_required(login_url='employee_login')
def employee_index(request):
    user = request.user
    employee, employee_image, company, work_time, leave_requests = get_employee_details(user)
    is_new_user = not AttendanceMaster.objects.filter(employee=employee).exists()
    
    if request.method == 'POST':
        process_form_submission(request, employee, company)
    
    latest_attendance = AttendanceMaster.objects.filter(employee=employee).order_by('-login_datetime').first()
    forgot_checkin_attendance = ForgotCheckIn.objects.filter(employee=employee, status='Pending').exists()
    checkin_time, checkout_time, total_working_hours = calculate_working_hours(latest_attendance)
    monthly_days, monthly_hours, weekly_hours = calculate_attendance_statistics(employee)
    leave_stats = calculate_leave_statistics(leave_requests,employee)
    attendance_counts = get_attendance_counts(employee)
    
    remaining_time = calculate_remaining_time(request, latest_attendance, work_time)
        
    context = {
        'forgot_checkin_attendance' : forgot_checkin_attendance,
        'weekly_attendance': attendance_counts['weekly'],
        'monthly_attendance': attendance_counts['monthly'],
        'yearly_attendance': attendance_counts['yearly'],
        'monthly_days': monthly_days,
        'monthly_hours': monthly_hours,
        'weekly_hours': weekly_hours,
        'latest_attendance': latest_attendance,
        'checkin_time': checkin_time,
        'checkout_time': checkout_time,
        'total_working_hours': total_working_hours,
        'work_time': work_time,
        'available_leave_balance': leave_stats['available_leave_balance'],
        'approved_leave_count': leave_stats['approved'],
        'pending_leave_count': leave_stats['pending'],
        'applied_leave_count': leave_stats['applied'],
        'rejected_leave_count': leave_stats['rejected'],
        'leave_balance': leave_stats['leave_balance'],
        'is_new_user': is_new_user,
        'remaining_time': remaining_time,
    }

    return render(request, 'employee/landing.html', context)

def calculate_remaining_time(request, latest_attendance, work_time):
    if latest_attendance and not latest_attendance.logout_datetime:
        checkin_time = latest_attendance.login_datetime
        elapsed_time = timezone.now() - checkin_time
        work_duration = (datetime.combine(datetime.min, work_time.end_time) - datetime.combine(datetime.min, work_time.start_time)).total_seconds()
        remaining_seconds = work_duration - elapsed_time.total_seconds()
        
        if remaining_seconds > 0:
            request.session['remaining_time'] = remaining_seconds
        else:
            request.session['remaining_time'] = 0
        
        return request.session['remaining_time']
    else:
        if work_time:
            work_duration = (datetime.combine(datetime.min, work_time.end_time) - datetime.combine(datetime.min, work_time.start_time)).total_seconds()
            return work_duration
        return 0

def get_employee_details(user):
    employee = EmployeeMaster.objects.select_related('user', 'company').prefetch_related('employeedesignation_set__designation').get(user=user)
    employee_image = EmployeeImage.objects.filter(employee=employee).first()
    company = employee.company
    work_time = WorkingTime.objects.filter(user=user).first()
    leave_requests = LeaveEnquiry.objects.filter(employee=employee).order_by('enquery_date')
    return employee, employee_image, company, work_time, leave_requests

def process_form_submission(request, employee, company):
    action = request.POST.get('action')
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    #datetime_str = request.POST.get('datetime')
    location_name = get_location_from_coordinates(latitude, longitude)
    #current_datetime = datetime.strptime(datetime_str, '%m/%d/%Y, %I:%M:%S %p')
    
    if action == 'checkin':
        checkin_employee(request, employee, company, location_name)
    elif action == 'checkout':
        checkout_employee(request, employee, location_name)
    elif action == 'forgot_checkin':
        handle_forgot_checkin(request, employee, company, location_name)

def checkin_employee(request, employee, company, location_name):
    working_time = WorkingTime.objects.get(user=employee.user, company=company)
    
     # Calculate the total working seconds based on start and end times
    start_time = working_time.start_time
    end_time = working_time.end_time
    remaining_time  = (datetime.combine(datetime.min, end_time) - datetime.combine(datetime.min, start_time)).total_seconds()
    
    AttendanceMaster.objects.create(
        employee=employee,
        company=company,
        login_datetime=timezone.now(),
        login_ipaddress=location_name
    )
    # Update remaining time in CountdownState
    state, created = CountdownState.objects.get_or_create(user=employee.user)
    state.total_seconds = remaining_time
    state.save()
    
    

def checkout_employee(request,employee, location_name):
    latest_attendance = AttendanceMaster.objects.filter(employee=employee).order_by('-login_datetime').first()
    if latest_attendance and not latest_attendance.logout_datetime:
        latest_attendance.logout_datetime = timezone.now()
        latest_attendance.logout_ipaddress = location_name
        latest_attendance.save()
        
         # Clear remaining time in CountdownState
        state = CountdownState.objects.filter(user=employee.user).first()
        if state:
            state.total_seconds = 0
            state.save()
            
        # Clear remaining time in session or local storage
        if 'remaining_time' in request.session:
            del request.session['remaining_time']

@login_required
def get_countdown_state(request):
    state = CountdownState.objects.filter(user=request.user).first()
    data = {
        'total_seconds': state.total_seconds if state else 0,
    }
    return JsonResponse(data)

@csrf_exempt
@login_required
def update_countdown_state(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total_seconds = data.get('total_seconds', 0)
        state, created = CountdownState.objects.get_or_create(user=request.user)
        state.total_seconds = total_seconds
        state.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
    
    
def handle_forgot_checkin(request, employee, company, location_name):
    start_time = request.POST.get('start_time')
    reason = request.POST.get('reason')
    
    if not ForgotCheckIn.objects.filter(employee=employee, status='Pending').exists():
        ForgotCheckIn.objects.create(
            employee=employee,
            company=company,
            current_time=timezone.now(),
            normal_login_time=start_time,
            reason=reason,
            location=location_name,
            status='Pending'
        )
        if not AttendanceMaster.objects.filter(employee=employee, is_pending_approval=True).exists():
            AttendanceMaster.objects.create(
                employee=employee,
                company=company,
                login_datetime=timezone.now(),
                login_ipaddress=location_name,
                is_pending_approval=True
            )

def calculate_working_hours(latest_attendance):
    checkin_time = localtime(latest_attendance.login_datetime) if latest_attendance and latest_attendance.login_datetime else None
    checkout_time = localtime(latest_attendance.logout_datetime) if latest_attendance and latest_attendance.logout_datetime else None

    formatted_checkin_time = checkin_time.strftime('%I:%M %p<br>%b %d, %Y') if checkin_time else ''
    formatted_checkout_time = checkout_time.strftime('%I:%M %p<br>%b %d, %Y') if checkout_time else ''

    if checkin_time and checkout_time:
        total_working_seconds = (checkout_time - checkin_time).total_seconds()
        hours, remainder = divmod(total_working_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        total_working_hours = f"{int(hours)}:{int(minutes):02d}"
    else:
        total_working_hours = ''

    return formatted_checkin_time, formatted_checkout_time, total_working_hours

def calculate_attendance_statistics(employee):
    today = timezone.now()
    start_of_month = today.replace(day=1)
    start_of_week = today - timedelta(days=today.weekday())
    
    monthly_attendances = AttendanceMaster.objects.filter(
        employee=employee,
        login_datetime__date__gte=start_of_month,
        logout_datetime__date__lte=today
    )
    monthly_days = monthly_attendances.values('login_datetime__date').distinct().count()
    monthly_hours = sum([(attendance.logout_datetime - attendance.login_datetime).seconds for attendance in monthly_attendances if attendance.logout_datetime and attendance.login_datetime]) / 3600
    monthly_hours = round(monthly_hours, 2)

    weekly_attendances = AttendanceMaster.objects.filter(
        employee=employee,
        login_datetime__date__gte=start_of_week,
        logout_datetime__date__lte=today
    )
    weekly_hours = sum([(attendance.logout_datetime - attendance.login_datetime).seconds for attendance in weekly_attendances if attendance.logout_datetime and attendance.login_datetime]) / 3600
    weekly_hours = round(weekly_hours, 2)

    return monthly_days, monthly_hours, weekly_hours

def calculate_leave_statistics(leave_requests,employee):
    try:
        add_leave_instances = AddLeave.objects.filter(employee=employee)
        available_leave_balance = sum([instance.available_leave_balance for instance in add_leave_instances])
        leave_balance = sum([instance.leave_balance for instance in add_leave_instances])
    except AddLeave.DoesNotExist:
        available_leave_balance = 0
        leave_balance = 0
    
    approved_leave_count = leave_requests.filter(status=1).count()
    pending_leave_count = leave_requests.filter(status=0).count()
    applied_leave_count = leave_requests.count()
    rejected_leave_count = leave_requests.filter(status=2).count()

    return {
        'available_leave_balance': available_leave_balance,
        'leave_balance': leave_balance,
        'approved': approved_leave_count,
        'pending': pending_leave_count,
        'applied': applied_leave_count,
        'rejected': rejected_leave_count
    }

def get_attendance_counts(employee):
    today = now().date()
    start_of_month = today.replace(day=1)
    start_of_week = today - timedelta(days=today.weekday())
    start_of_year = today.replace(month=1, day=1)

    weekly_attendance = AttendanceMaster.objects.filter(employee=employee, login_datetime__gte=start_of_week).count()
    monthly_attendance = AttendanceMaster.objects.filter(employee=employee, login_datetime__gte=start_of_month).count()
    yearly_attendance = AttendanceMaster.objects.filter(employee=employee, login_datetime__gte=start_of_year).count()

    return {
        'weekly': weekly_attendance,
        'monthly': monthly_attendance,
        'yearly': yearly_attendance
    }


# @login_required(login_url='employee_login')
# def employee_index(request):
#     user = request.user
    
#     employee = EmployeeMaster.objects.select_related('user', 'company').prefetch_related('employeedesignation_set__designation').get(user=user)
#     employee_image = EmployeeImage.objects.filter(employee=employee).first()
#     company = employee.company
#     work_time = WorkingTime.objects.filter(user=user).first()
#     leave_requests = LeaveEnquiry.objects.filter(employee=employee).order_by('enquery_date')
    
#     # Determine if the user is new
#     is_new_user = not AttendanceMaster.objects.filter(employee=employee).exists()

#     if request.method == 'POST':
#         action = request.POST.get('action')
#         latitude = request.POST.get('latitude')
#         longitude = request.POST.get('longitude')
#         datetime_str = request.POST.get('datetime')
#         location_name = get_location_from_coordinates(latitude, longitude)

#         current_datetime = datetime.strptime(datetime_str, '%m/%d/%Y, %I:%M:%S %p')
        
        
#         if action == 'checkin':
#             AttendanceMaster.objects.create(
#                 employee=employee,
#                 company=company,
#                 login_datetime=current_datetime,
#                 login_ipaddress=location_name
#             )
#         elif action == 'checkout':
#             latest_attendance = AttendanceMaster.objects.filter(employee=employee).order_by('-login_datetime').first()
#             if latest_attendance and not latest_attendance.logout_datetime:
#                 latest_attendance.logout_datetime = current_datetime
#                 latest_attendance.logout_ipaddress = location_name
#                 latest_attendance.save()
                
#         elif action == 'forgot_checkin':
#             start_time = request.POST.get('start_time')
#             reason = request.POST.get('reason')

#             if not ForgotCheckIn.objects.filter(employee=employee, status='Pending').exists():
#                 ForgotCheckIn.objects.create(
#                     employee=employee,
#                     company=company,
#                     current_time=current_datetime,
#                     normal_login_time=start_time,
#                     reason=reason,
#                     location=location_name,
#                     status='Pending'
#                 )
#                 if not AttendanceMaster.objects.filter(employee=employee, is_pending_approval=True).exists():
#                     AttendanceMaster.objects.create(
#                         employee=employee,
#                         company=company,
#                         login_datetime=current_datetime,
#                         login_ipaddress=location_name,
#                         is_pending_approval=True
#                     )

#     latest_attendance = AttendanceMaster.objects.filter(employee=employee).order_by('-login_datetime').first()

#     checkin_time = localtime(latest_attendance.login_datetime) if latest_attendance and latest_attendance.login_datetime else None
#     checkout_time = localtime(latest_attendance.logout_datetime) if latest_attendance and latest_attendance.logout_datetime else None

#     formatted_checkin_time = checkin_time.strftime('%I:%M %p<br>%b %d, %Y') if checkin_time else ''
#     formatted_checkout_time = checkout_time.strftime('%I:%M %p<br>%b %d, %Y') if checkout_time else ''

#     if checkin_time and checkout_time:
#         total_working_seconds = (checkout_time - checkin_time).total_seconds()
#         hours, remainder = divmod(total_working_seconds, 3600)
#         minutes, _ = divmod(remainder, 60)
#         total_working_hours = f"{int(hours)}:{int(minutes):02d}"
#     else:
#         total_working_hours = ''
    
#     employee = EmployeeMaster.objects.get(user=request.user)
#     today = now().date()
#     start_of_month = today.replace(day=1)
#     start_of_week = today - timedelta(days=today.weekday())
#     start_of_year = today.replace(month=1, day=1)

#     # Monthly attendance
#     monthly_attendances = AttendanceMaster.objects.filter(
#         employee=employee,
#         login_datetime__date__gte=start_of_month,
#         logout_datetime__date__lte=today
#     )
#     monthly_days = monthly_attendances.values('login_datetime__date').distinct().count()

#     # Monthly hours
#     monthly_hours = sum([(attendance.logout_datetime - attendance.login_datetime).seconds for attendance in monthly_attendances if attendance.logout_datetime and attendance.login_datetime]) / 3600
#     monthly_hours = round(monthly_hours, 2)  # Round to 2 decimal places

#     # Weekly hours
#     weekly_attendances = AttendanceMaster.objects.filter(
#         employee=employee,
#         login_datetime__date__gte=start_of_week,
#         logout_datetime__date__lte=today
#     )
#     weekly_hours = sum([(attendance.logout_datetime - attendance.login_datetime).seconds for attendance in weekly_attendances if attendance.logout_datetime and attendance.login_datetime]) / 3600
#     weekly_hours = round(weekly_hours, 2)  # Round to 2 decimal places
    
#     # Retrieve available leave balance
#     try:
#         add_leave_instances = AddLeave.objects.filter(employee=employee)
#         available_leave_balance = 0
#         leave_balance = 0
#         total_leave_count = {}
#         total_leave_balance = {}
    
#         for add_leave_instance in add_leave_instances:
#             available_leave_balance += add_leave_instance.available_leave_balance
#             leave_balance += add_leave_instance.leave_balance
            
#     except AddLeave.DoesNotExist:
#         available_leave_balance = {}
#         leave_balance = {}# Handle case where no AddLeave object exists
#     except AddLeave.MultipleObjectsReturned:
#         # Handle case where multiple AddLeave objects exist
#         add_leave_objects = AddLeave.objects.filter(employee=employee)
#         available_leave_balance = add_leave_objects.first().available_leave_balance if add_leave_objects.exists() else 0
#         available_leave_balance = {}
        
#     # Calculate leave statistics
#     approved_leave_count = leave_requests.filter(status=1).count()
#     pending_leave_count = leave_requests.filter(status=0).count()
#     applied_leave_count = leave_requests.count()
#     rejected_leave_count = leave_requests.filter(status=2).count()

    
#     #Graph chart
#     # Fetch attendance data based on these date ranges
    
#     weekly_attendance = AttendanceMaster.objects.filter(employee=employee,login_datetime__gte=start_of_week).count()
#     monthly_attendance = AttendanceMaster.objects.filter(employee=employee,login_datetime__gte=start_of_month).count()
#     yearly_attendance = AttendanceMaster.objects.filter(employee=employee,login_datetime__gte=start_of_year).count()
    
  
    
#     context = {
#         'weekly_attendance': weekly_attendance,
#         'monthly_attendance': monthly_attendance,
#         'yearly_attendance': yearly_attendance,
#         'monthly_days': monthly_days,
#         'monthly_hours': monthly_hours,
#         'weekly_hours': weekly_hours,
#         'latest_attendance': latest_attendance,
#         'checkin_time': formatted_checkin_time,
#         'checkout_time': formatted_checkout_time,
#         'total_working_hours': total_working_hours,
#         'work_time': work_time,
#         'available_leave_balance': available_leave_balance,
#         'approved_leave_count': approved_leave_count,
#         'pending_leave_count': pending_leave_count,
#         'applied_leave_count': applied_leave_count,
#         'rejected_leave_count': rejected_leave_count,
#         'leave_balance': leave_balance,
#         'is_new_user': is_new_user,  # Add this to the context
#     }

#     return render(request, 'employee/landing.html', context)

@login_required(login_url='employee_login')
def approve_forgot_checkin(request, forgot_checkin_id):
    forgot_checkin = get_object_or_404(ForgotCheckIn, id=forgot_checkin_id)
    
    # Get the company details for the logged-in user
    company = get_object_or_404(CompanyDetails, user=request.user)

    # Ensure the forgot check-in belongs to the employee in the logged-in user's company
    if forgot_checkin.employee.company != company:
        return redirect('admin_forgot_checkin_list')
    
    if request.method == 'POST':
        approval = request.POST.get('approval', '')
        if approval == 'approve':
            attendance = AttendanceMaster.objects.filter(
                employee=forgot_checkin.employee,
                is_pending_approval=True
            ).order_by('-login_datetime').first()
            if attendance:
                attendance.login_datetime = forgot_checkin.normal_login_time
                attendance.is_pending_approval = False
                attendance.save()
            forgot_checkin.status = 'Approved'
        else:
            forgot_checkin.status = 'Rejected'
        forgot_checkin.save()
        return redirect('admin_forgot_checkin_list')

    return render(request, 'company_admin/approve_forgot_checkin.html', {
        'forgot_checkin': forgot_checkin
    })

@login_required(login_url='employee_login')
def admin_forgot_checkin_list(request):
    # Get the company details for the logged-in user
    company = get_object_or_404(CompanyDetails, user=request.user)

    # Filter the forgot check-ins for the specific company
    forgot_checkins = ForgotCheckIn.objects.filter(employee__company=company,status='Pending').select_related('employee')

    return render(request, 'company_admin/forgot_checkin_list.html', {
        'forgot_checkins': forgot_checkins
    })
 
from django.db.models import Q

@login_required(login_url='employee_login')
def leave_form(request):
    employee = EmployeeMaster.objects.get(user=request.user)
    leave_requests = LeaveEnquiry.objects.filter(employee=employee, status=0).order_by('-enquery_date')
    
    if request.method == "POST":
        if 'delete_request' in request.POST:
            leave_request_id = request.POST.get('delete_request')
            reason = request.POST.get('modal-reason')

            # Validate leave_request_id
            if not leave_request_id or not leave_request_id.isdigit():
                messages.error(request, "Invalid leave request ID.")
                return redirect('leave_form')

            try:
                leave_request = LeaveEnquiry.objects.get(id=leave_request_id, employee=employee)
                leave_request.status = 3  # Set status to Cancelled
                leave_request.reason = reason
                leave_request.save()
                messages.success(request, "Leave request cancelled successfully.")
                return redirect('leave_form')
            except LeaveEnquiry.DoesNotExist:
                messages.error(request, "Leave request not found.")
                return redirect('leave_form')

        leave_type_id = request.POST.get('leavetype')
        reason = request.POST.get('reason')
        from_date = request.POST.get('from_date')
        end_date = request.POST.get('end_date')
        half_day_option = request.POST.get('half_day_option', None)

        # Validate dates
        try:
            from_date_parsed = datetime.strptime(from_date, '%Y-%m-%d')
            end_date_parsed = datetime.strptime(end_date, '%Y-%m-%d')
            if from_date_parsed > end_date_parsed:
                messages.error(request, "From date cannot be later than end date.")
                return redirect('leave_form')
        except ValueError:
            messages.error(request, "Invalid date format. Please enter valid dates.")
            return redirect('leave_form')
                
        
        # Check for overlapping leave requests
        overlapping_requests = LeaveEnquiry.objects.filter(
            Q(employee=employee),
            Q(status__in=[0, 1, 2]),  # Pending, Approved, Rejected
            Q(from_date__lte=end_date_parsed, end_date__gte=from_date_parsed) |
            Q(from_date__gte=from_date_parsed, end_date__lte=end_date_parsed) |
            Q(from_date__lte=from_date_parsed, end_date__gte=end_date_parsed)
        )

        if overlapping_requests.exists():
            messages.error(request, "Leave request already exists with the selected dates.")
            return redirect('leave_form')

        user = request.user
        employee = user.employees.first()
        company = employee.company

        try:
            leave_type = LeaveMaster.objects.get(id=leave_type_id)
        except LeaveMaster.DoesNotExist:
            messages.error(request, "Selected leave type does not exist.")
            return redirect('leave_form')

        # Calculate the requested leave duration
        if from_date == end_date and half_day_option:
            leave_duration = 0.5  # Half day leave
        else:
            leave_duration = (end_date_parsed - from_date_parsed).days + 1

        # Retrieve the available leave balance for the employee and leave type
        try:
            leave_balance_record = AddLeave.objects.get(employee=employee, leave=leave_type)
            available_leave_balance = leave_balance_record.available_leave_balance
        except AddLeave.DoesNotExist:
            available_leave_balance = 0

        if leave_duration > available_leave_balance:
            messages.error(request, "Insufficient leave balance.")
            return redirect('leave_form')

    

        # Create the leave enquiry
        LeaveEnquiry.objects.create(
            company=company,
            employee=employee,
            leave=leave_type,
            from_date=from_date,
            end_date=end_date,
            enquery_date= timezone.now(),
            status=0,
            reason=reason,
            half_day_option=half_day_option
        )
        messages.success(request, "Leave request submitted successfully.")
        return redirect('leave_form')

    leave_name = LeaveMaster.objects.all()

    for leave_request in leave_requests:
        leave_request.duration = (leave_request.end_date - leave_request.from_date).days + 1
        
        

    return render(request, 'employee/leave_form.html', {'leave_name': leave_name, 'leave_requests': leave_requests})

@login_required(login_url='employee_login')
def employee_profile(request):
    if request.user.is_authenticated:
        try:
            employee = EmployeeMaster.objects.select_related('user').prefetch_related('employeedesignation_set__designation').get(user=request.user)
            employee_image = EmployeeImage.objects.filter(employee=employee).first()
            
            if request.method == 'POST' and request.FILES.get('profile_image'):
                image_file = request.FILES['profile_image']
                # Update or create the EmployeeImage
                if employee_image:
                    employee_image.employee_image = image_file
                    employee_image.save()
                else:
                    EmployeeImage.objects.create(employee=employee, employee_image=image_file)
                return redirect('employee_profile')
            
            try:
                employee_profile = EmployeeProfile.objects.filter(employee=employee).first()
            except EmployeeProfile.DoesNotExist:
                employee_profile = None
            # Pass employee data along with the context
            context = {
                'employee': {
                    'first_name': employee.user.first_name,
                    'last_name': employee.user.last_name,
                    'designations': employee.employeedesignation_set.all(),
                    'image_url': employee_image.employee_image.url if employee_image else None
                },
                
                'employee_info':employee,
                'employee_profile' : employee_profile
            }
            return render(request, 'employee/profile.html', context)
        except EmployeeMaster.DoesNotExist:
            pass 
    return render(request, 'employee/profile.html', {'employee': None})

@login_required(login_url='employee_login')
def employee_personal_info(request):
    if request.user.is_authenticated:
        try:
            employee = EmployeeMaster.objects.select_related('user').prefetch_related('employeedesignation_set__designation').get(user=request.user)
            employee_image = EmployeeImage.objects.filter(employee=employee).first()
            try:
                employee_profile = EmployeeProfile.objects.get(employee=employee)
            except EmployeeProfile.DoesNotExist:
                employee_profile = None
            
            # Pass employee data along with the context
            context = {
                'employee': {
                    'first_name': employee.user.first_name,
                    'last_name': employee.user.last_name,
                    'designations': employee.employeedesignation_set.all(),
                    'image_url': employee_image.employee_image.url if employee_image else None
                },
                
                'employee_info':employee,
                'employee_profile': employee_profile
            }
            return render(request, 'employee/personalinfo.html', context)
        except EmployeeMaster.DoesNotExist:
            pass 
    return render(request, 'employee/personalinfo.html', {'employee': None})

@login_required(login_url='employee_login')
def employee_work_detail(request):
    if request.user.is_authenticated:
        try:
            employee = EmployeeMaster.objects.get(user=request.user)
            company = get_object_or_404(CompanyDetails, id=employee.company_id)
        except:
            pass
        
        bank_details = BankDetails.objects.filter(employee=employee).first() or {}
        
        
        if request.method == 'POST':
            bank_name = request.POST.get('bank_name')
            account_number = request.POST.get('account_number')
            branch_address = request.POST.get('branch_address')
            ifsc_code = request.POST.get('ifsc_code')
            BankDetails.objects.update_or_create(
                employee__user_id  = request.user,
                defaults = {
                    'employee' : employee,
                    'company' : company,
                    'bank_name' : bank_name,
                    'account_number' : account_number,
                    'branch_address' :branch_address,
                    'ifsc_code': ifsc_code
                }
            )
                    
            return redirect('employee_work_detail')
            
        try:
            employee = EmployeeMaster.objects.select_related('user', 'city', 'company').prefetch_related(
                Prefetch('employeedesignation_set', queryset=EmployeeDesignation.objects.select_related('designation')),
                Prefetch('employeedepartment_set', queryset=EmployeeDepartment.objects.select_related('department')),
                Prefetch('employeejoinmaster_set', queryset=EmployeeJoinMaster.objects.select_related('role'))
            ).get(user=request.user)

            employee_image = EmployeeImage.objects.filter(employee=employee).first()
            latest_department = employee.employeedepartment_set.order_by('-id').first()
            latest_join = employee.employeejoinmaster_set.order_by('-id').first()

            context = {
                'employee': {
                    'first_name': employee.user.first_name,
                    'last_name': employee.user.last_name,
                    'designations': employee.employeedesignation_set.all(),
                    'department': latest_department.department if latest_department else None,
                    'join_date': latest_join.join_date if latest_join else None,
                    'role': latest_join.role if latest_join else None,
                    'email': employee.user.email,
                    'location': employee.city,
                    'image_url': employee_image.employee_image.url if employee_image else None,
                    'bank_details': bank_details
                },
                'employee_info': employee,
                'bank_details': bank_details
            }
            return render(request, 'employee/work.html', context)
        except EmployeeMaster.DoesNotExist:
            return render(request, 'employee/work.html', {'employee': None})

    return render(request, 'employee/work.html', {'employee': None, 'bank_details': bank_details})


def Register(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']
        repeat_password = request.POST['rpass']
        email = request.POST['email']
        contact_no = request.POST['mobno']
        # usertype_id = request.POST['usertype']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address1 = request.POST['address1']
        city_id = request.POST['city']
        company_icon = request.FILES['company_icon']
        company_logo = request.FILES['company_logo']
        reg_no = request.POST['regno']
        company_name = request.POST['company_name']

        if password != repeat_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
        usertype = UserType.objects.get(usertype='Admin')
        city = CityMaster.objects.get(id=city_id)
        
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            contact_no=contact_no,
            usertype=usertype,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        
        CompanyDetails.objects.create(
            company_name=company_name,
            company_icon=company_icon,
            company_logo=company_logo,
            reg_no=reg_no,
            city=city,
            user=user,
            address=address1
        )
        
        messages.success(request, "Company Details Registered Successfully")
        return redirect('register')
    
    cities = CityMaster.objects.all()
    context = {
        'cities':cities
    }
    return render(request,'buzcatch/register.html',context)

# Forgor Password view

def generate_otp():
    return random.randint(100000, 999999)


from django.conf import settings

def send_otp(contact_no, otp):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Your OTP is {otp}",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=contact_no
    )
    return message.sid

def password_reset_request(request):
    error_message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp = random.randint(100000, 999999)
            user.otp = otp
            user.save()
            
            country_code = '+91'
            full_mobile_number = f'{country_code}{user.contact_no}'
            
            send_otp(full_mobile_number, otp)
            return redirect('password_reset_verify_otp', email=email)
        except ObjectDoesNotExist:
            # messages.error(request,"User with this email does not exist")
            # return redirect('password_reset_request')
            error_message = "User with this email does not exist"
    return render(request, 'employee/password_reset_request.html',{'error_message': error_message})

def password_reset_verify_otp(request, email):
    error_message = request.GET.get('error_message',"")
    user = get_object_or_404(User, email=email)
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if str(user.otp) == otp:
            request.session['otp_verified'] = True
            return redirect('set_new_password', email=email)
        else:
            error_message = "Invalid OTP"
            return HttpResponseRedirect(f"{reverse('password_reset_verify_otp', kwargs={'email':email})}?error_message={error_message}")
    return render(request, 'employee/password_reset_verify_otp.html', {'error_message': error_message})


def set_new_password(request, email):
    user = get_object_or_404(User, email=email)
    if not request.session.get('otp_verified'):
        messages.error(request,'OTP verfication required')
        return redirect('password_reset_request')
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            del request.session['otp_verified']
            messages.success(request,'Password has been reset Successfully')
            return redirect('employee_login')
        else:
            messages.error(request,'Passwords do not match')
            return redirect('set_new_password',email=email)
    return render(request, 'employee/set_new_password.html')


# def verify_otp(request):
#     if request.method == 'POST':
        
#         otp = request.POST['otp']

#         try:
#             user = User.objects.get(contact_no=mobile_number)
#             device = TOTPDevice.objects.get(user=user)

#             if device.verify_token(otp):
#                 # OTP is correct, redirect to password reset form
#                 request.session['user_id'] = user.id
#                 return redirect('reset_password')
#             else:
#                 return render(request, 'employee/verify_otp.html', {'error': 'Invalid OTP'})
#         except (User.DoesNotExist, TOTPDevice.DoesNotExist):
#             return render(request, 'employee/verify_otp.html', {'error': 'Invalid mobile number or OTP'})

#     return render(request, 'employee/verify_otp.html')
from django.db.models import Sum, Count
@login_required(login_url='employee_login')
def Leave(request):
    employee = EmployeeMaster.objects.select_related('user').get(user=request.user)
    leave_requests = LeaveEnquiry.objects.filter(employee=employee).order_by('enquery_date')
    monthly_days, monthly_hours, weekly_hours = calculate_attendance_statistics(employee)
    
    for leave in leave_requests:
        if leave.from_date and leave.end_date:
            days = (leave.end_date - leave.from_date).days + 1
            if leave.half_day_option:
                if leave.from_date == leave.end_date:
                    days = 0.5 # half day leave
                else:
                    days -= 0.5 # deduct half day if any day is half-day leave
        else:
            days = 0
        leave.total_days = days
    
    
    # Retrieve available leave balance
    add_leave_instances = AddLeave.objects.filter(employee=employee)
    leave_balance_agg = add_leave_instances.aggregate(
        available_leave_balance=Sum('available_leave_balance'),
        leave_balance=Sum('leave_balance')
    )

    available_leave_balance = leave_balance_agg['available_leave_balance'] or 0
    leave_balance = leave_balance_agg['leave_balance'] or 0

    # Calculate leave statistics
    leave_counts = leave_requests.aggregate(
        approved_leave_count=Count('id', filter=Q(status=1)),
        pending_leave_count=Count('id', filter=Q(status=0)),
        applied_leave_count=Count('id'),
        rejected_leave_count=Count('id', filter=Q(status=2)),
    )

    context = {
        'monthly_days': monthly_days,
        'monthly_hours': monthly_hours,
        'weekly_hours': weekly_hours,
        'leave_requests': leave_requests,
        'available_leave_balance': available_leave_balance,
        'approved_leave_count': leave_counts['approved_leave_count'],
        'pending_leave_count': leave_counts['pending_leave_count'],
        'applied_leave_count': leave_counts['applied_leave_count'],
        'rejected_leave_count': leave_counts['rejected_leave_count'],
        'leave_balance': leave_balance,
    }

    return render(request, 'employee/leave.html', context)

@login_required(login_url='employee_login')
def LeaveDetails(request, leave_id):
    leave_request = LeaveEnquiry.objects.get(id=leave_id, employee__user=request.user)  
    
    # Calculate the total days of leave
    if leave_request.from_date and leave_request.end_date:
        days = (leave_request.end_date - leave_request.from_date).days + 1
    else:
        days = 0

    leave_request.total_days = days
    
    return render(request, 'employee/leave_details.html', {'leave_request': leave_request})

@login_required(login_url='employee_login')
def Report(request):
    attendance_records = None
    
    if request.method == 'POST':
        
        storage = messages.get_messages(request) #clear previous error messages
        storage.used = True
        
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        
        # Check if both dates are provided
        if not from_date or not to_date:
            messages.error(request, "Both from date and to date are required.")
            return redirect('reports')
        
        # Convert dates to proper format
        try:
            from_date = parse_date(from_date)
            to_date = parse_date(to_date)
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect('reports')

        # Validate date range
        if from_date > to_date:
            messages.error(request, "From date cannot be later than end date.")
            return redirect('reports')
        
        # Query attendance records within the date range
        attendance_records = AttendanceMaster.objects.filter(
            employee__user=request.user, 
            login_datetime__date__range=(from_date, to_date)
        )

        # Debugging: Print the query and number of records found
        print(f"Query: {attendance_records.query}")
        print(f"Number of records found: {attendance_records.count()}")
        
    return render(request, 'employee/report.html', {'attendance_records': attendance_records})


@login_required(login_url='employee_login')
def testing(request):
    attendance_records = None
    
    if request.method == 'POST':
        
        storage = messages.get_messages(request) #clear previous error messages
        storage.used = True
        
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        
        # Check if both dates are provided
        if not from_date or not to_date:
            messages.error(request, "Both from date and to date are required.")
            return redirect('testing')
        
        # Convert dates to proper format
        try:
            from_date = parse_date(from_date)
            to_date = parse_date(to_date)
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect('testing')

        # Validate date range
        if from_date > to_date:
            messages.error(request, "From date cannot be later than end date.")
            return redirect('testing')
        
        # Query attendance records within the date range
        attendance_records = AttendanceMaster.objects.filter(
            employee__user=request.user, 
            login_datetime__date__range=(from_date, to_date)
        )

        # Debugging: Print the query and number of records found
        print(f"Query: {attendance_records.query}")
        print(f"Number of records found: {attendance_records.count()}")
        
    return render(request, 'employee/testing.html', {'attendance_records': attendance_records})



@login_required(login_url='employee_login')
def DownloadReport(request):
    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        if from_date and to_date:
            from_date = parse_date(from_date)
            to_date = parse_date(to_date)

            attendance_records = AttendanceMaster.objects.filter(
                employee__user=request.user,
                login_datetime__date__range=(from_date, to_date)
            )

            data = []
            for record in attendance_records:
                data.append([
                    record.login_datetime.strftime("%d-%m-%Y"),
                    record.login_datetime.strftime("%H:%M %p"),
                    record.login_ipaddress,
                    record.logout_datetime.strftime("%H:%M %p") if record.logout_datetime else '',
                    record.logout_ipaddress,
                    'Present' if record.logout_datetime else 'Present'
                ])

            df = pd.DataFrame(data, columns=['Date', 'CheckIn', 'CheckIn Location', 'Checkout', 'Checkout Location', 'Status'])

            # Create a response object and set the content type and disposition
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=attendance_report.xlsx'

            # Use pandas to write the DataFrame to a BytesIO object
            with pd.ExcelWriter(response, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                
                # Define the fill for the header
                header_fill = PatternFill(start_color='0073f7', end_color='0073f7', fill_type='solid')

                # Apply the fill to the header cells
                for cell in worksheet[1]:
                    cell.fill = header_fill

            return response
    return HttpResponse("Invalid request")

@login_required
def employee_edit_profile(request):
    try:
        employee_master = EmployeeMaster.objects.get(user=request.user)
        company =  get_object_or_404(CompanyDetails, id=employee_master.company_id)
    except EmployeeMaster.DoesNotExist:
        # Handle case where EmployeeMaster record does not exist
        return redirect('employee_profile')
    # try:
    profile = EmployeeProfile.objects.filter(employee=employee_master).first() or {}
    # if profile:
    #     pass
    # profile = profile.first() if profile.exists() else {}
    # except EmployeeProfile.DoesNotExist:
    #     profile = {}
    
    if request.method == 'POST':
        # Extract data from the form
        personal_mail = request.POST.get('personal_mail')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        blood_group = request.POST.get('blood_group')
        nationality = request.POST.get('nationality')
        identification_no = request.POST.get('identification_no')
        field_of_study = request.POST.get('field_of_study')
        school = request.POST.get('school')
        guardian_name = request.POST.get('guardian_name')
        guardian_phone = request.POST.get('guardian_phone')
        guardian_email = request.POST.get('guardian_email')
        guardian_address = request.POST.get('guardian_address')
        linkedin = request.POST.get('linkedin')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')
        skill1 = request.POST.get('skill1')
        skill2 = request.POST.get('skill2')
        skill3 = request.POST.get('skill3')
        skill4 = request.POST.get('skill4')
        skill5 = request.POST.get('skill5')
        
        EmployeeProfile.objects.update_or_create(
            employee__user_id = request.user.id,
            defaults = {
            'linkedin': linkedin,
            'twitter' :twitter,
            'instagram' : instagram,
            'employee':employee_master,
            'company':company,
            'personal_mail':personal_mail,
            'date_of_birth':date_of_birth,
            'gender':gender,
            'marital_status':marital_status,
            'blood_group':blood_group,
            'nationality':nationality,
            'identification_no': identification_no,
            'field_of_study': field_of_study,
            'school':school,
            'guardian_name':guardian_name,
            'guardian_phone': guardian_phone,
            'guardian_email': guardian_email,
            'guardian_address': guardian_address,
            'skill_1': skill1,
            'skill_2': skill2,
            'skill_3': skill3,
            'skill_4': skill4,
            'skill_5': skill5,
            }
        )
        
        return redirect('employee_profile')  # Redirect to wherever you list your profiles
    
    # Render the form with existing data if editing
    return render(request, 'employee/editprofile.html', {'profile': profile})