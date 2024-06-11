# # # from django.contrib.auth.backends import ModelBackend
# # # from .models import Users_INFO

# # # class CustomBackend(ModelBackend):
# # #     def authenticate(self, request, email=None, password=None, **kwargs):
# # #         try:
# # #             user = Users_INFO.objects.get(email=email)
# # #         except Users_INFO.DoesNotExist:
# # #             return None

# # #         if user.check_password(password):
# # #             return user

# # #         return None
# # # In home/backends.py
# # from django.conf import settings
# # from django.contrib.auth.backends import ModelBackend
# # from .models import Users_INFO

# # class YourCustomBackend(ModelBackend):
# #     def authenticate(self, request, email=None, password=None, **kwargs):
# #         try:
# #             user = Users_INFO.objects.get(email=email)
# #         except Users_INFO.DoesNotExist:
# #             print(f"User with email {email} does not exist.")
# #             return None

# #         if user.check_password(password):
# #             print(f"User with email {email} authenticated successfully.")
# #             print(user)
# #             return user

# #         print(f"Password incorrect for user with email {email}.")
# #         return None
# from django.conf import settings
# from django.contrib.auth.backends import ModelBackend
# from .models import Users_INFO

# class YourCustomBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = Users_INFO.objects.get(email=email)
#         except Users_INFO.DoesNotExist:
#             print(f"User with email {email} does not exist.")
#             return None
#         print(user.password)
#         print(user.email)
#         print(password)
#         status=user.check_password(password)
#         print(status)
#         if status:
#             print(f"User with email {email} authenticated successfully.")
#             print(user)
#             return user

#         print(f"Password incorrect for user with email {email}.")
#         return None

#     def get_user(self, user_id):
#         try:
#             return Users_INFO.objects.get(pk=user_id)
#         except Users_INFO.DoesNotExist:
#             return None
