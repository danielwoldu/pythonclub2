#Tesing Models
from django.test import TestCase
from .models import Meeting, MeetingMinute, Resource

class MeetingTest(TestCase):
   def test_string(self):
       meeting=Meeting(meetingtitle="SeattleCentral")
       self.assertEqual(str(meeting), meeting.meetingtitle)

   def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')
#Testing the view

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
# class MeeTest(TestCase):
#    def test_view_url_accessible_by_name(self):
#        response = self.client.get(reverse('products'))
#        self.assertEqual(response.status_code, 200)


#Creating context elements in view
# def setUp(self):
#         self.u=User.objects.create(username='myuser')
#         self.type=ProductType.objects.create(typename='laptop')
#         self.prod = Product.objects.create(productname='product1', producttype=self.type, user=self.u, productprice=500, productentrydate='2019-04-02', productdescription="a product")
#         self.rev1=Review.objects.create(reviewtitle='prodreview', reviewdate='2019-04-03', product=self.prod, reviewrating=4, reviewtext='some review')
#         self.rev1.user.add(self.u)
#         self.rev2=Review.objects.create(reviewtitle='prodreview', reviewdate='2019-04-03', product=self.prod,  reviewrating=4, reviewtext='some review')
#         self.rev2.user.add(self.u)
# #testing a view that takes an id for paramenter
# def test_product_detail_success(self):
#         response = self.client.get(reverse('productdetails', args=(self.prod.id,)))
#         # Assert that self.post is actually returned by the post_detail view
#         self.assertEqual(response.status_code, 200)
# #Testing context elements in view.

# def test_discount(self):
#         discount=self.prod.memberdiscount()
#         self.assertEqual(discount, 25.00)

#     def test_number_of_reviews(self):
#         reviews=Review.objects.filter(product=self.prod).count()
#         self.assertEqual(reviews, 2)




# #class Meeting(models.Model):
#     meetingtitle=models.CharField(max_length=255)
#     meetingdate=models.DateField()
#     meetingtime=models.TimeField()
#     meetingagenda=models.TextField()

#     def __str__(self):
#         return self.meetingtitle
    
#     class Meta:
#         db_table='meeting'

# class MeetingMinute(models.Model):
#     meeting=models.ForeignKey(Meeting,on_delete=models.DO_NOTHING)
#     meetingattend=models.ManyToManyField(User)
#     meetingtext=models.TextField()








# # Create your tests here.
