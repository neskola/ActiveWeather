function CalendarDataCtrl($scope) {

  $scope.entries = [
    {text:'workshop', min:'-15', max:'15'},
    {text:'next event', min:'-10', max:'20'},
	{text:'further event', min:'-12', max:'13'}];

};

function WeatherDataCtrl($scope) {

	$scope.entries = [
	{text:"cloudy", temp:'5'},
	{text:"sunny", temp:'3'},
	{text:"rainy", temp:'4'}];
};