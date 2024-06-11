from django.db import models
from datetime import datetime
from django.core.validators import validate_email,RegexValidator
from home.models import Users_INFO
# Create your models here.
class CustomAutoField(models.AutoField):
    def __init__(self, *args, **kwargs):
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

class TechnoagaazTeam(models.Model):
    teamID = CustomAutoField(primary_key=True)
    teamName = models.CharField(max_length=100)
    leaderName = models.CharField(max_length=100)
    emailID = models.EmailField(validators=[validate_email])
    phoneNO = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\d{10,15}$', message='Phone number must be between 10 and 15 digits.')
    ])
    event = models.CharField(max_length=100,blank=True, null=True)
    game = models.CharField(max_length=100,blank=True, null=True)
    user = models.ForeignKey(Users_INFO, on_delete=models.CASCADE, related_name='created_TechnoagaazTeams',  default=None, blank=True, null=True)   #for user association with team
    amount=models.CharField(max_length=100,null=True,blank=True)
    payment_ID=models.CharField(max_length=100,null=True,blank=True)
    order_ID=models.CharField(max_length=100,null=True,blank=True)
    payment_signature=models.CharField(max_length=100,null=True,blank=True)
    paid=models.BooleanField(default=False)
    
    
    
    def save(self, *args, **kwargs):   #this is save overide funcion which is called when we save the model 
        if not self.teamID:
            # Auto-generate teamID with a combination of current date and time
            current_datetime = datetime.now()
            date_part = current_datetime.strftime('%Y%m%d')         #for current date,year,month,time as a teamID
            time_part = current_datetime.strftime('%H%M%S')

            self.teamID = int(f'{date_part}{time_part}')

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.teamName} ({self.teamID})"
    

class TechnoagaazTeamMember(models.Model):
    team = models.ForeignKey(TechnoagaazTeam, on_delete=models.CASCADE, null=True, related_name='team_members')
    name = models.CharField(max_length=100)
  
    class Meta:
        unique_together = ['team','name']  # Ensure uniqueness based on teamID

    def __str__(self):
        if self.team:
            return f"{self.name} ({self.team.teamName}) - {self.team.teamID}"
        else:
            return f"{self.name} - No Team Assigned"
