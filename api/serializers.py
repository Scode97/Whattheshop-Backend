from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import serializers
from .models import  Plans, Profile, OrderPlan, Order

from django.dispatch import receiver


from rest_framework_jwt.settings import api_settings




from django.db.models.signals import post_save
# FOR Users

class UserCreateSerializer(serializers.ModelSerializer):

    token = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
      model = User
      fields = ['username', 'password','token', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        firstname = validated_data['first_name']
        lastname= validated_data['last_name']
        email = validated_data['email']



        new_user = User(username=username, first_name= firstname, last_name= lastname, email=email)
        new_user.set_password(password)
        

        new_user.save()

        # refer https://stackoverflow.com/questions/41623751/token-creation-with-rest-framework-jwt
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        handler =jwt_payload_handler(new_user)

      
        token = jwt_encode_handler(handler)

        validated_data["token"] = token

        print (validated_data)

        return validated_data

@receiver(post_save, sender=settings.AUTH_USER_MODEL)

def create_Profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user_name=instance)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email']





class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = [
          'name', 
          'image',
          'totalPrice',
          'description',

         
            ]


class OrderPlanListSerializer (serializers.ModelSerializer):
  class Meta:
    model = OrderPlan
    fields = '__all__'




class OrderSerializer(serializers.ModelSerializer):
    
    OrderPlans = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'

    def get_OrderPlans (self, obj):
      # OrderPlan = OrderPlan.objects.all(order = obj)
      request = self.context.get('request')
      OrderPlans = OrderPlan.objects.filter(order = obj)
      
      return OrderPlanListSerializer(OrderPlans, many= True, context = {"request": request}).data


# class ExpertListSerializer(serializers.ModelSerializer):
#    items = serializers.SerializerMethodField()

#    class Meta:
#        model = Expert
#        fields = '__all__'

#    def get_items(self, obj):
#        request = self.context.get('request')
#        items = Item.objects.filter(expert=obj)
#        return ItemListSerializer(items, many=True, context={"request": request}).data
#  