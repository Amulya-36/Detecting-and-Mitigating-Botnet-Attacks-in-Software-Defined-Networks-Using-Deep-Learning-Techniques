# """detecting_and_mitigating_botnet_attacks URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.urls import path, re_path
# from django.contrib import admin
# from Remote_User import views as remoteuser
# from detecting_and_mitigating_botnet_attacks import settings
# from Service_Provider import views as serviceprovider
# from django.conf.urls.static import static


# urlpatterns = [
#     url('admin/', admin.site.urls),
#     url(r'^$', remoteuser.login, name="login"),
#     url(r'^Register1/$', remoteuser.Register1, name="Register1"),
#     url(r'^Predict_Attack_Type/$', remoteuser.Predict_Attack_Type, name="Predict_Attack_Type"),
#     url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
#     url(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
#     url(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
#     url(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
#     url(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),
#     url(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
#     url(r'^View_Attack_Type_Prediction_Details_Ratio/$', serviceprovider.View_Attack_Type_Prediction_Details_Ratio, name="View_Attack_Type_Prediction_Details_Ratio"),
#     url(r'^View_Attack_Type_Prediction_Details/$', serviceprovider.View_Attack_Type_Prediction_Details, name="View_Attack_Type_Prediction_Details"),
#     url(r'^Train_Test_View_Results_Details/$', serviceprovider.Train_Test_View_Results_Details, name="Train_Test_View_Results_Details"),
#     url(r'^Download_Trained_DataSets/$', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),

# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



"""
detecting_and_mitigating_botnet_attacks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""

from django.urls import path, re_path
from django.contrib import admin
from Remote_User import views as remoteuser
from detecting_and_mitigating_botnet_attacks import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', remoteuser.login, name="login"),
    path('Register1/', remoteuser.Register1, name="Register1"),
    path('Predict_Attack_Type/', remoteuser.Predict_Attack_Type, name="Predict_Attack_Type"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path('serviceproviderlogin/', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    
    re_path(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts, name="charts"),
    re_path(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),
    re_path(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    path('View_Attack_Type_Prediction_Details_Ratio/', serviceprovider.View_Attack_Type_Prediction_Details_Ratio, name="View_Attack_Type_Prediction_Details_Ratio"),
    path('View_Attack_Type_Prediction_Details/', serviceprovider.View_Attack_Type_Prediction_Details, name="View_Attack_Type_Prediction_Details"),
    path('Train_Test_View_Results_Details/', serviceprovider.Train_Test_View_Results_Details, name="Train_Test_View_Results_Details"),
    path('Download_Trained_DataSets/', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

