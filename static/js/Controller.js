'use strict';
var ctrl = angular.module('ws', []).config(function($interpolateProvider,$httpProvider){
  $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

ctrl.controller('wsLogin',function($scope, $window,$http,$sce,$compile,$timeout) {
  $scope.login=function(){
    $http.post('/register/auth',$scope.form).success(function(response) {
      $scope.msg=response.msg

      if(response.success){
        $scope.col="green";
        $timeout(function(){
          $window.location.href=response.rdr;
        }, 1000);

      }else{
        $scope.col="red";
      }
    });
  }

})

