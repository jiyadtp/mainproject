from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('',views.index,name='index'),
        path('login-check',views.login_check,name='login-check'),
        path('register',views.register,name='register'),
        path('register-data',views.register_data,name='register-data'),

        path('student-dashboard',views.student_dashboard,name='student-dashboard'),
        path('buy-course',views.buy_course,name='buy-course'),
        path('pay-course/<int:id>',views.pay_course,name='pay-course'),
        path('paymenthandler',views.paymenthandler,name='paymenthandler'),

        path('instructor-dashboard',views.instructor_dashboard,name='instructor-dashboard'),
        path('create-course',views.create_course,name='create-course'),
        path('edit-course',views.edit_course,name='edit-course'),
        path('edit-course-action',views.edit_course_action,name='edit-course-action'),
        path('view-users',views.view_users,name='view-users'),
        path('delete-course/<int:id>', views.delete_course, name='delete-course'),

        path('logout', auth_views.LogoutView.as_view(), name="logout"),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)