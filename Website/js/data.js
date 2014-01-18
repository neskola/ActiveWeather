function CalendarDataCtrl($scope) {

  $scope.entries = [
    {text:'workshop', min:'-15', max:'15'},
    {text:'next event', min:'-10', max:'20'},
	{text:'further event', min:'-12', max:'13'}];

};

function WeatherDataCtrl($scope) {

	var place = 'Helsinki';

	$.ajax({
		type: "GET",
		url: "http://data.fmi.fi/fmi-apikey/8a861995-5bad-4fea-85e8-7cccd6860bb2/wfs?request=getFeature&storedquery_id=fmi::forecast::hirlam::surface::point::multipointcoverage&place=helsinki",
		dataType: "xml",
		success: function(xml) {
			$("<div class='alert alert-success alert-dismissable'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>Ok!</strong> Weather data refresh was succesfull</div>").appendTo("#status");
			// get data from xml file
		},
		error: function(xml) {
			$("<div class='alert alert-warning alert-dismissable'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>Warning!</strong> Weather data refresh was NOT succesfull</div>").appendTo("#status");
			// failed
		}
	});
	
	$scope.entries = [
	{text:"cloudy", temp:'5'},
	{text:"sunny", temp:'3'},
	{text:"rainy", temp:'4'}];
	
	

};

