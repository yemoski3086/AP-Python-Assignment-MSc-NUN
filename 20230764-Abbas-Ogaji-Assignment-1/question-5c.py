def shooting_aliens(color):
    alien_color = color
    if alien_color == 'green':
        print('Your player just earned 5 points for shooting the alien')
    elif alien_color == 'yellow':
        print('Your player just earned 10 points for shooting the alien')
    elif alien_color == 'red':
        print('Your player just earned 15 points for shooting the alien')
    
shooting_aliens('green')
shooting_aliens('yellow')
shooting_aliens('red')