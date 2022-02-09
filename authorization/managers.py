from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self,email,password):

		if email is None:
			raise TypeError('Users must have a username.')



		user = self.model(email=email)
		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, email,password):
		if password is None:
			raise TypeError('Superusers must have a password.')
		user = self.create_user(email,password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user
