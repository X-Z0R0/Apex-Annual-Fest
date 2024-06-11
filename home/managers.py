# managers.py
from django.contrib.auth.models import BaseUserManager

# class Users_INFOManager(BaseUserManager):
    
#     def create_user(self, phoneNO, password=None, **extra_fields):
#         user = self.model(phoneNO=phoneNO, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, phoneNO, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(phoneNO, password, **extra_fields)


class Users_INFOManager(BaseUserManager):
    # ... other methods ...
    use_in_migrations=True
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        

        return self.create_user(email, password, **extra_fields)
