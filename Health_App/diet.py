def htmlDiet(dietData):
	template = '<div class="col-md-4 col-sm-4  col-lg-3">'+'<div class="profile-widget">' +'<div class="doctor-img">' +'<a class="avatar" href="#"><img alt="" src="{{ url_for('+ "'static'"+ ', filename='+"'assets/img/doctor-thumb-12.jpg') }}"'></a>'+'</div>' +'<h4 class="doctor-name text-ellipsis"><a href="#">%s</a></h4>'+'<div class="doc-prof">%s</div>'+'<div class="user-country">'+'<i class="fa fa-map-marker"></i> United States, San Francisco'+'</div>'+'</div>'+'</div>'
	htmlTemplate = ''
	for i in dietData:
		temp = template
		temp

htmlDiet()