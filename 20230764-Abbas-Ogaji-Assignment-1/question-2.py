def _print_invitation(invidation_list, message = 'You are hereby invited to graduation ceremony'):
   for invitee in invidation_list:
        print("Hello {}, {}".format(invitee, message))

grad_invitees = ['Yusuf', 'Maryam', 'Fatima']
_print_invitation(grad_invitees)

grad_invitees[0] = 'Sage'
_print_invitation(grad_invitees)

print('More invitations allowed')
grad_invitees.insert(0, 'Rukky')
grad_invitees.insert(int(len(grad_invitees)/2), 'Ahmad')
grad_invitees.append('John Sinner')
_print_invitation(grad_invitees)

print('Only two people can be invited for graduation')
total_invitee = len(grad_invitees)
no_of_invitees_to_remove = total_invitee-2

for _ in range(no_of_invitees_to_remove):
    removed_invitee = grad_invitees.pop()
    print('Dear {}, we sincerely apologies because we have to decline ur invitation to graduation'.format(removed_invitee))
_print_invitation(grad_invitees, "You are still invited to the graduation")

grad_invitees.sort()
_print_invitation(grad_invitees)

grad_invitees.reverse()
_print_invitation(grad_invitees)

del grad_invitees[:]
print(grad_invitees)