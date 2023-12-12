def shooting_aliens(color):
    alien_color = color
    if alien_color == 'green':
        print('Your player just earned 5 points for shooting the alien')
    else:
        print('Your player just earned 10 points for shooting the alien')

    
shooting_aliens('green')
shooting_aliens('red')
