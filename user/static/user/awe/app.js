'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'ui.bootstrap',
  'ngResource',
  'dashboardServices',
  'myApp.dashboard',
])
.config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/dashboard'});
}])
.directive('jqdatepicker', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
                    scope.date = date;
                    scope.$apply();
                }
            });
        }
    };
});