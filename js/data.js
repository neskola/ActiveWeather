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
			// get data from xml file
		}
	});
	
	$scope.entries = [
	{text:"cloudy", temp:'5'},
	{text:"sunny", temp:'3'},
	{text:"rainy", temp:'4'}];
};

