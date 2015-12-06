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
					}, 500);

				}else{
					$scope.col="red";
				}
		});
	}

});

ctrl.controller('wsPay',function($scope,$http,$window,$compile) {
	$scope.notify=function(gid){
		var data={"gid":gid};
		$http.post('/register/notify',data).success(function(response) {
			if(response.success){
				$window.alert("已通知付款");
				$window.location.href='/register/details';
			}
		});
	};

	$scope.confirmPay=function(gid){
		var data={"gid":gid};
		$http.post('/register/confirm',data).success(function(response) {
			if(response.success){
				$window.alert("已確認付款");
				$window.location.href='/register/view';
			}
		});
	};
});

ctrl.controller('wsIndex',function($scope, $window,$http,$sce,$compile,$timeout) {
	var init=function(){
		$http.get('static/content.json').then(function(res){
			$scope.data=res.data;
			//init value
			var init_data="story";
			$scope.title=$scope.data[init_data].title;
			$scope.subtitle=$scope.data[init_data].subtitle;
			$scope.desc=$scope.data[init_data].desc;
		});

	}
	$scope.navigate=function(index){
		$scope.title=$scope.data[index].title;
		$scope.subtitle=$scope.data[index].subtitle;
		$scope.desc=$scope.data[index].desc;
	}
	init();
});
