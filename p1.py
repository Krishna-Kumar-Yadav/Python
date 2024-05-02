#Dictionary Program 

informationOfPeople ={};
n = int(input("Enter number of person :"));
for detail in range(n+1):
  A={'name':{},'address' :{}};
  A['name']['first'] = input("Enter your first name:");
  A['name']['middle'] = input("Enter your  middle name:");
  A['name']['last'] = input("Enter your last name:");
  A['address']['building'] = input('Enter your building name:');
  A['address']['pincode'] = input('Enter your pincode:');
  A['address']['city'] = input('Enter your city name:');
  A['E-Mail'] = input("Enter your E-mail:");
  A['Phone_No'] = int(input("Enter your phone no."));
  A['aadhar_No'] = int(input('Enter your aadhar number:'));
  
  informationOfPeople[f'person{detail+1}'] =A;
  
print(informationOfPeople);