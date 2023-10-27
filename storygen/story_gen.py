import random
when = ['A few years ago', 'Yesterday', 'Late night', 'week later','On 11th Jan']
who = ['a ghost', 'an boy', 'a phasmophobia', 'a gamer','a murderer']
name = ['Mayank', 'Priyanshu','Nagpal', 'Rawat', 'Praveen']
residence = ['India','Russia', 'Gujarat', 'Vivek vihar', 'Sri lanka']
went = ['Huanted place', 'School','Haunted Show', 'Forest', 'Shop']
happened = ['made a lot of friends','Eats a burger', 'found a secret key from that Huanted Place', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))