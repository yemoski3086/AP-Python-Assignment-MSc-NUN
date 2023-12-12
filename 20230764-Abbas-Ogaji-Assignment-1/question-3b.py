def show_magicians(magicians):
    [print(magician) for magician in magicians]

def make_great(magicians):
    return map(lambda x: 'Great '+x, magicians)


list_of_magicians = ['Sango', 'babanla', 'odumodu']
show_magicians(list_of_magicians)

new_list_magicians = make_great(list_of_magicians[:])
show_magicians(new_list_magicians)