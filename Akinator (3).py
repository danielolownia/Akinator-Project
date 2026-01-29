
name = input('What is your name?: ')
print('Hello ' + name + ', nice to meet you!')

print('Think of an Olympic sport, and I’ll guess it.')
print('For all questions, ' + name + ', please answer with True or False.')

team_sport = input('Is it a team sport? ')
while team_sport not in ['True', 'False']:
    team_sport = input('Please enter True or False and nothing else: ')

uses_ball = input('Does it use a ball? ')
while uses_ball not in ['True', 'False']:
    uses_ball = input('Please enter True or False and nothing else: ')

summer_sport = input('Is it in the Summer Olympics? ')
while summer_sport not in ['True', 'False']:
    summer_sport = input('Please enter True or False and nothing else: ')

water_sport = input('Is it played in water? ')
while water_sport not in ['True', 'False']:
    water_sport = input('Please enter True or False and nothing else: ')

requires_judges = input('Does it require judges to score? ')
while requires_judges not in ['True', 'False']:
    requires_judges = input('Please enter True or False and nothing else: ')

# Main guessing logic
if team_sport == 'True':
    if uses_ball == 'True':
        if water_sport == 'True':
            print('You are thinking of... WATER POLO!')
        elif summer_sport == 'True':
            print('You are thinking of... BASKETBALL!')
        else:
            print('You are thinking of... SOCCER!')
    else:
        if summer_sport == 'True':
            print('You are thinking of... VOLLEYBALL!')
        else:
            print('You are thinking of... ICE HOCKEY!')
else:
    if water_sport == 'True':
        print('You are thinking of... SWIMMING!')
    elif requires_judges == 'True':
        if summer_sport == 'True':
            print('You are thinking of... GYMNASTICS!')
        else:
            print('You are thinking of... FIGURE SKATING!')
    elif uses_ball == 'True':
        print('You are thinking of... TENNIS!')
    else:
        print('You are thinking of... TRACK AND FIELD!')

if name == 'Curling':
    print('Your name is the most boring sport to watch! (Sorry)')

print('Thank you for playing our Akinator game! We hope you had fun!')
