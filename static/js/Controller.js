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
	$scope.deleteItem=function(gid){
		var data={"gid":gid};
		$http.post('/register/delete',data).success(function(response) {
			if(response.success){
				$window.alert("已刪除");
				$window.location.href='/register/details';
			}else{
				$window.alert("刪除失敗，請檢查權限或聯絡管理員");
				$window.location.href='/register/details';
			}
		});
	};

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
	$scope.navigate=function(index){
		$scope.title=$scope.templates[index].name;
		$scope.subtitle=$scope.templates[index].subtitle;
		$scope.template = $scope.templates[index];
	};

	var init=function(){
		$scope.templates = {
			"story":{ name: '風弦故事',subtitle:"This's how everything started", url: 'static/story.html'},
			"reg":{ name: '參加風弦',subtitle:"Let's play together", url: 'static/reg.html'},
			"transportation":{ name: '交通資訊',subtitle:"Transfer Information", url: 'static/trans.html'},
			"contact":{ name: '聯絡我們',subtitle:"Contact us", url: 'static/contact.html'}
		};
		$scope.navigate('story');
	};

	init();
});
