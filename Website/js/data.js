function mySort(obj) {
    var result = [];
    angular.forEach(obj, function (val, key) {
        if (angular.isObject(val)) {
            result.push(val);
        }
    });
    return result;
}

angular.module('activeweather', ['firebase'])
    .filter("toArray", function () {
        return function (obj) {
            return mySort(obj);
        };
    })
    .controller('GeoidCtrl', ['$scope', '$firebase',
  function ($scope, $firebase) {
      var firebaseRef = firebaseSingleton.getInstance().getReference();
      var ref = firebaseRef.child("observations/meta");
      $scope.metadata = $firebase(ref);

      $scope.$watch('metadata', function () {
          console.log(JSON.stringify($scope.metadata) + " / " + ref);
      }, true);

  }])
    .controller('WeatherDataCtrl', ['$scope', '$firebase',
  function ($scope, $firebase) {
      var firebaseRef = firebaseSingleton.getInstance().getReference();
      var ref = firebaseRef.child("observations/meta");
      $scope.metadata = $firebase(ref);
  }]);
