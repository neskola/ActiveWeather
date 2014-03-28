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

      $scope.region = null;
      $scope.observations = [];

      $scope.$watch('metadata', function () {
          console.log(JSON.stringify($scope.metadata) + " / " + ref);
      }, true);

      $scope.selectedGeoid = function () {
          console.log($scope.region.geoid);
          var dataRef = firebaseRef.child("observations/data/" + $scope.region.geoid);
          $scope.observations = $firebase(dataRef);
          $scope.$watch('observations', function () {
              console.log(JSON.stringify($scope.observations) + " / " + ref);
          }, true);          
      }
  }]);
