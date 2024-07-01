from master.models import CompanyDetails
from master.models import *
from attendance_app.models import *
from django.contrib.auth.decorators import login_required

def company_logo(request):
    if request.user.is_authenticated:
        try:
            company = CompanyDetails.objects.get(user=request.user)
            return {
                'company_name': company.company_name,
                'company_logo': company.company_logo.url if company.company_logo else None
            }
        except CompanyDetails.DoesNotExist:
            return {
                'company_name': None,
                'company_logo': None
            }
    return {
        'company_name': None,
        'company_logo': None
    }




def employee_base(request):
    if request.user.is_authenticated:
        try:
            employee = EmployeeMaster.objects.select_related('user').prefetch_related('employeedesignation_set__designation').get(user=request.user)
            employee_image = EmployeeImage.objects.filter(employee=employee).first()
            
            return {
                'employee': {
                    'first_name': employee.user.first_name,
                    'last_name': employee.user.last_name,
                    'designations': employee.employeedesignation_set.all(),
                    'image_url': employee_image.employee_image.url if employee_image else None
                }
            }
        except EmployeeMaster.DoesNotExist:
            return {
                'employee': None
            }
    return {
        'employee': None
    }