from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.login_redirect, name='login_redirect'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_index/', views.AdminIndex, name='admin_index'),
    path('useradd/', views.UserAdd, name='useradd'),
    path('userlist/', views.UserList, name='userlist'),
    path('attendance_overview/', views.AttendanceOverview, name='attendance_overview'),
    # path('login/', auth_views.LoginView.as_view(template_name='adminlogin.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register, name='register'),
    path('worktime/', views.WorkTime, name='worktime'),
    path('user/<int:user_id>/edit/',views.UserEdit, name='useredit'),
    path('user/<int:user_id>/',views.UserView, name='userview'),
    path('user/delete/<int:user_id>/',views.UserDelete, name='userdelete'),
    path('company_profile',views.CompanyProfile, name='company_profile'),
    path('edit_company_profile/',views.EditCompanyProfile, name='edit_company_profile'),
    path('add_leave_balance/',views.AddLeaveBalance, name='add_leave_balance'),
    path('leave-request/',views.LeaveRequest, name='leave_request'),
    path('process-leave/<int:leave_enquiry_id>/<str:action>/', views.process_leave_request, name='process_leave_request'),
 

    path('',views.employee_login, name='employee_login'),
    path('employee_logout/',views.employee_logout, name='employee_logout'),
    path('employee_index/',views.employee_index, name='employee_index'),
    path('employee_profile/',views.EmployeeProfile, name='employee_profile'),
    # path('forgot_checkin/',views.forgot_checkin, name='forgot_checkin'),
    path('approve-forgot-checkin/<int:forgot_checkin_id>/', views.approve_forgot_checkin, name='approve_forgot_checkin'),
    path('forgot-checkin-list/', views.admin_forgot_checkin_list, name='admin_forgot_checkin_list'),
    path('leave_form/', views.LeaveForm, name='leave_form'),
    path('leave/', views.Leave, name='leave'),
    path('leave_details/<int:leave_id>', views.LeaveDetails, name='leave_details'),
    path('reports', views.Report, name='reports'),
    path('download_report/', views.DownloadReport, name='download_report'),
    path('employee_personal_info/', views.EmployeePersonalInfo, name='employee_personal_info'),
    path('employee_work_detail/', views.EmployeeWorkDetail, name='employee_work_detail'),
    
    
    
    path('password-reset/', views.password_reset_request, name='password_reset_request'),
    path('password-reset/verify-otp/<str:email>/', views.password_reset_verify_otp, name='password_reset_verify_otp'),
    path('password-reset/set-new-password/<str:email>/', views.set_new_password, name='set_new_password'),
  

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)