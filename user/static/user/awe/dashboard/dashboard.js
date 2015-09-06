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
    self.openResults = function(game, played) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/club/results_modal.html'),
            controller: 'ClubResultsModalController',
            windowClass: 'app-modal-window',
            resolve: {
                game: function() {
                    return game;
                },
                played: function() {
                    return played;
                }
            }
        });
        modalInstance.result.then(function() {
        });
    };

    self.openEditClub = function(club) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/club/club_modify_modal.html'),
            controller: 'ClubModalController',
            windowClass: 'app-modal-window',
            resolve: {
                club: function() {
                    return club;
                }
            }
        });
        modalInstance.result.then(function() {
        });
    };
}])

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

.controller('ClubResultsModalController', function($scope, $modalInstance, game, played) {
    var playerModal = $scope;
    playerModal.game = game;
    playerModal.played = played;
    playerModal.ok = function() {
        $modalInstance.close();
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('ClubModalController', function($scope, $modalInstance, club) {
    var playerModal = $scope;
    playerModal.club = angular.copy(club);

    playerModal.ok = function() {
        $modalInstance.close(playerModal.club);
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})
