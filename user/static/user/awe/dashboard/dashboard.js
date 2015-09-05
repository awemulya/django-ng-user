'use strict';

angular.module('myApp.dashboard', ['ngRoute'])

.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = djcsrf();
}])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/dashboard', {
    templateUrl: djstatic('user/awe/dashboard/index.html'),
    controller: 'DashboardController'
  })
  $routeProvider.when('/clubs', {
    templateUrl: djstatic('user/awe/dashboard/club/club.html'),
    controller: 'ClubController'
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
    self.openPlayerFixtures = function(player) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/fixtures_modal.html'),
            controller: 'FixtureModalController',
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

.controller('FixtureModalController', function($scope, $modalInstance, player) {
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

.controller('ClubPlayerModalController', function($scope, $modalInstance, players) {
    var playerModal = $scope;
    playerModal.players = players;

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


.controller('ClubController', ['$scope', 'Clubs', '$modal', '$timeout', function($scope, Clubs, $modal, $timeout) {
 var self = $scope;
 self.clubs = Clubs.query();
 self.profileImg = [{
        src: djstatic('user/vendor/dist/img/user2-160x160.jpg'),
    }];

    self.openPlayers = function(players) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/club/players_modal.html'),
            controller: 'ClubPlayerModalController',
            windowClass: 'app-modal-window',
            resolve: {
                players: function() {
                    return players;
                }
            }
        });
        modalInstance.result.then(function() {
        });
    };
    self.openPlayerFixtures = function(player) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/fixtures_modal.html'),
            controller: 'FixtureModalController',
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