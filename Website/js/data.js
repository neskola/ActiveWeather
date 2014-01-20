function CalendarDataCtrl($scope) {

  $scope.entries = [
    {text:'workshop', min:'-15', max:'15'},
    {text:'next event', min:'-10', max:'20'},
	{text:'further event', min:'-12', max:'13'}];

};

function WeatherDataCtrl($scope, $http) {

    var place = 'Helsinki';    

    $scope.entries = [];

    $.ajax({
        type: "GET",
        url: './python/' + place + '.json',
        async: false,
        success: function (data) {
            $("<div class='alert alert-success alert-dismissable'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>Ok!</strong> Weather data refresh was succesfull</div>").appendTo("#status");
            $scope.entries.push(data);
        },
        error: function (data) {
            $("<div class='alert alert-warning alert-dismissable'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>Warning!</strong> Weather data refresh was NOT succesfull</div>").appendTo("#status");                        
        }
    });
    
    console.log($scope.data);    
};

function AirportDataCtrl($scope, $http) {

    $scope.entries = [
        {code: '1', city: 'Istanbul', name: 'ist'},
        {code: '2', city: 'London', name: 'lon'},
        {code: '3', city: 'Paris', name: 'par'}
    ];

}

