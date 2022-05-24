from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import *
from core.permissions import ResturentUser, OfficeUser
from .models import *



# Create your views here.


class AddResturentView(LoginRequiredMixin, TemplateView):
	login_url = 'core:user-login'
	redirect_field_name = 'core:user-login'
	#permission_classes = [ResturentUser]
	template_name = 'resturent/add_resturent.html'

	def get(self, request, *args, **kwargs):
		if request.user.acc_type == "Resturent":
			return render(request, self.template_name)
		else:
			return redirect('core:user-login')

	def post(self, request):
		name = request.POST['resturent_name']
		email = request.POST['email']
		phone = request.POST['phone']

		address = request.POST['address']
		city = request.POST['city']
		country = request.POST['country']

		booking_type = request.POST['booking_type']
		booking_price = request.POST['booking_price']
		booking_status = request.POST['booking_status']
		timing_days_available = request.POST['timing_days_available']

		cafeteria = request.POST['cafeteria']
		wifi = request.POST['wifi']
		cafeteria_details = request.POST['cafeteria_details']
		sitting_details = request.POST['sitting_details']
		resturent_other_details = request.POST['resturent_other_details']
		image = request.POST['image']

		if request.user.acc_type == "Resturent":
			data = Resturent.objects.create(user=request.user, name=name, email=email, phone=phone,
				address=address, city=city, country=country,
				booking_type=booking_type, booking_price=booking_price, booking_status=booking_status,
				cafeteria=cafeteria, wifi=wifi, cafeteria_details=cafeteria_details, 
				sitting_details=sitting_details, resturent_other_details=resturent_other_details,
				image=image
				)
			messages.success(request, 'Add Successfully')
			return redirect('resturent:add-resturent')
		else:
			messages.success(request, 'Permission Required!')
			return redirect('resturent:add-resturent')
