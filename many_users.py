users = { 'erajesh':{'first':'rajesh','last':'esakki'},
		  'rvishrudh':{'first':'vishrudh','last':'rajesh'},
		  'rvelrani':{'first':'velrani','last':'rajaguru'}	
}

for username, user_info in users.items():
	print(f"username : {username}")
	print(f"Fullname : {user_info['first']} {user_info['last']}")