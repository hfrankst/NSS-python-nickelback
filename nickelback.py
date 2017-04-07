songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

for song in songs: 
	if song[0] != 'Nickelback':
		no_nickelback_here = song
		print(no_nickelback_here)

