#to create a makrsheet defining division
while True:
  name=input("what is your name:")
  science=input( "Enter your obtained marks in science:")
  Math=input("Enter your obtained marks in Math:")
  Social=input("Enter your obtained marks in Social:")
  Nepali=input("Enter your obtained marks in Nepali:")
  gk =input("Enter your obtained marks in gk:")

  total_score=float(float(science)+float(Math)+float(Social)+float(Nepali)+float(gk))/5
  print("Your total_score is", total_score)

  if total_score>90:
    print('Congratulation! You got an A+')
  elif total_score<90 and total_score>80:
    print('You got a A')
  elif total_score<80 and total_score>70:
    print('You got a B+')
  elif total_score<70 and total_score>60:
    print('You got a B')
  elif total_score<60 and total_score>50:
    print('You got a C+')
  elif total_score<50 and total_score>40:
    print('You got a C')
  elif total_score<50 and total_score>40:
    print('You got a D+')
  elif total_score<40:
    print('You got a D')

 