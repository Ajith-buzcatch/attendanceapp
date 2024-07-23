from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.login_redirect, name='login_redirect'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_index/', views.admin_index, name='admin_index'),
    path('useradd/', views.user_add, name='useradd'),
    path('userlist/', views.user_list, name='userlist'),
    path('attendance_overview/', views.attendance_overview, name='attendance_overview'),
    # path('login/', auth_views.LoginView.as_view(template_name='adminlogin.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register, name='register'),
    path('worktime/', views.WorkTime, name='worktime'),
    path('user/<int:user_id>/edit/',views.user_edit, name='useredit'),
    path('user/<int:user_id>/',views.user_view, name='userview'),
    path('user/delete/<int:user_id>/',views.UserDelete, name='userdelete'),
    path('company_profile',views.CompanyProfile, name='company_profile'),
    path('edit_company_profile/',views.EditCompanyProfile, name='edit_company_profile'),
    path('add_leave_balance/',views.add_leave_balance, name='add_leave_balance'),
    path('get_leave_balances/<int:employee_id>/', views.get_leave_balances, name='get_leave_balances'),
    path('leave-request/',views.LeaveRequest, name='leave_request'),
    path('process-leave/<int:leave_enquiry_id>/<str:action>/', views.process_leave_request, name='process_leave_request'),
 

    path('get_countdown_state/', views.get_countdown_state, name='get_countdown_state'),
    path('update_countdown_state/', views.update_countdown_state, name='update_countdown_state'),
    path('',views.employee_login, name='employee_login'),
    path('employee_logout/',views.employee_logout, name='employee_logout'),
    path('employee_index/',views.employee_index, name='employee_index'),
    path('employee_profile/',views.employee_profile, name='employee_profile'),
    # path('forgot_checkin/',views.forgot_checkin, name='forgot_checkin'),
    path('approve-forgot-checkin/<int:forgot_checkin_id>/', views.approve_forgot_checkin, name='approve_forgot_checkin'),
    path('forgot-checkin-list/', views.admin_forgot_checkin_list, name='admin_forgot_checkin_list'),
    path('leave_form/', views.leave_form, name='leave_form'),
    path('leave/', views.Leave, name='leave'),
    path('leave_details/<int:leave_id>', views.LeaveDetails, name='leave_details'),
    path('reports', views.Report, name='reports'),
    path('testing/', views.testing, name='testing'),
    path('download_report/', views.DownloadReport, name='download_report'),
    path('employee_personal_info/', views.employee_personal_info, name='employee_personal_info'),
    path('employee_work_detail/', views.employee_work_detail, name='employee_work_detail'),
    path('employee_edit_profile/', views.employee_edit_profile, name='employee_edit_profile'),
    
    
    
    path('password-reset/', views.password_reset_request, name='password_reset_request'),
    path('password-reset/verify-otp/<str:email>/', views.password_reset_verify_otp, name='password_reset_verify_otp'),
    path('password-reset/set-new-password/<str:email>/', views.set_new_password, name='set_new_password'),
  
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)