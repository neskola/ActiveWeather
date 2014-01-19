function CalendarDataCtrl($scope) {

  $scope.entries = [
    {text:'workshop', min:'-15', max:'15'},
    {text:'next event', min:'-10', max:'20'},
	{text:'further event', min:'-12', max:'13'}];

};

function WeatherDataCtrl($scope, $http) {

    var place = 'Helsinki';
    var result = getWeatherData(place, $http).then(function () {
        $scope.entries = result;
    });
    
    alert(JSON.stringify($scope.entries));
};

function getWeatherData($place, $http) {
    var promise = $http({
        method : 'GET',
        url : './python/' + $place + '.json'
    }).success(function (data, status, headers, config) {
        $("<div class='alert alert-success alert-dismissable'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>Ok!</strong> Weather data refresh was succesfull</div>").appendTo("#status");
        console.log('Done');
        alert(JSON.stringify(data));
        entries = data;
        return entries;
    }).error(function (data, status, headers, config) {
        $("<div class='alert alert-warning alert-dismissable'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>Warning!</strong> Weather data refresh was NOT succesfull</div>").appendTo("#status");                
        entries = data;
        return entries;
    });

    return promise; 
}; 
