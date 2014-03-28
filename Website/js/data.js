function WeatherDataCtrl($scope, $http) {

    
    $scope.entries = [];
    
    console.log($scope.data);    
};

function GeoidDataCtrl($scope, $http) {

    $scope.entries = [
    { place: 'Helsinki', geoid: '658225' },
    { place: 'Porvoo', geoid: '660561' },
    { place: 'Vantaa', geoid: '632453' },
    { place: 'Vaasa', geoid: '632978' },
    { place: 'Messila', geoid: '10000720' },
    { place: 'Ruka', geoid: '10000742' }
    ];

    $scope.place = $scope.entries[0];

}

function ProfileDataCtrl($scope, $http) {
    var profile = { name: 'Teemu Testaaja', email : 'teemu.testaaja@gmail.com', default_place : 'Helsinki' };    
    $scope.profile = profile;    
}

function AirportDataCtrl($scope, $http) {

    $scope.entries = [
        {code: '1', city: 'Istanbul', name: 'ist'},
        {code: '2', city: 'London', name: 'lon'},
        {code: '3', city: 'Paris', name: 'par'}
    ];

}

