"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from planillas.resources.city import CityViewSet
from planillas.resources.people import PeopleViewSet
from planillas.resources.academicUnit import AcademicUnitViewSet
from planillas.resources.account import AccountViewSet
from planillas.resources.academicMethod import AcademicMethodViewSet
from planillas.resources.semester import SemesterViewSet
from planillas.resources.specialty import SpecialtyViewSet
from planillas.resources.student import StudentViewSet
from planillas.resources.account import LoginView, LogoutView
from emiForms.resources.form import FormViewSet
from emiForms.resources.question import QuestionViewSet, QuestionFormApiView
# from emiForms.resources.question import QuestionFormApiView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'AcademicMethod', AcademicMethodViewSet)
router.register(r'AcademicUnit', AcademicUnitViewSet)
router.register(r'Account', AccountViewSet)
router.register(r'City', CityViewSet)
router.register(r'People', PeopleViewSet)
router.register(r'Semester', SemesterViewSet)
router.register(r'Specialty', SpecialtyViewSet)
router.register(r'Student', StudentViewSet)

routerForms = routers.DefaultRouter()
routerForms.register(r'Form', FormViewSet)
routerForms.register(r'Question', QuestionViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^Forms/', include(routerForms.urls)),
    url(r'^Forms/Form/(?P<pk>[0-9]+)/question/$', QuestionFormApiView.as_view(), name='Forms'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^Login/', LoginView.as_view(), name="login"),
    url(r'^Logout/', LogoutView.as_view(), name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
