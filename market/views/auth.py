from django.contrib.auth import models as auth_models
from django.contrib.auth import views as auth_views
from django import http

from market.forms import auth as auth_forms


@auth_views.deprecate_current_app
@auth_views.sensitive_post_parameters()
@auth_views.csrf_protect
@auth_views.never_cache
def register(request, template_name='registration/register.html',
             register_form=auth_forms.RegisterForm,
             extra_context=None, redirect_authenticated_user=True):
    """
    Displays the register form and handles the login action.
    """
    if redirect_authenticated_user and request.user.is_authenticated:
        return http.HttpResponseRedirect('/')
    elif request.method == "POST":
        form = register_form(data=request.POST)
        if form.is_valid():
            user = auth_models.User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1'])
            user.save()
            auth_views.auth_login(request, user)
            return http.HttpResponseRedirect('/')
    else:
        form = register_form()

    current_site = auth_views.get_current_site(request)

    context = {
        'form': form,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    return auth_views.TemplateResponse(request, template_name, context)
