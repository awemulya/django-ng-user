'use strict';

angular.module('myApp.dashboard', ['ngRoute'])

.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = djcsrf();
}])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/dashboard', {
    templateUrl: djstatic('user/awe/dashboard/index.html'),
    controller: 'DashboardController'
  });
}])

.controller('DashboardController', ['$scope', 'Players', '$modal', '$timeout', function($scope, Players, $modal, $timeout) {
 var self = $scope;
 self.players = Players.query();
 self.profileImg = [{
        src: djstatic('user/vendor/dist/img/user2-160x160.jpg'),
    }];

    self.openPlayerDetails = function(player) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/player_detail_modal.html'),
            controller: 'PlayerDetailModalController',
            windowClass: 'app-modal-window',
            resolve: {
                player: function() {
                    return player;
                }
            }
        });
        modalInstance.result.then(function() {
        });
    };
}])

.controller('PlayerDetailModalController', function($scope, $modalInstance, player) {
    var playerModal = $scope;
    playerModal.player = player;

     self.profileImg = [{
        src: djstatic('user/vendor/dist/img/user2-160x160.jpg'),
    }];


    playerModal.ok = function() {
        $modalInstance.close();
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})


.controller('MainController', ['$scope', function($scope) {
 var self = $scope;
 self.name = "maincontroller";
}]);