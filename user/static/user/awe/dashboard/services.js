angular.module('dashboardServices', ['ngResource'])

.factory('Players', ['$resource', function($resource){
	return $resource('/app/players/', {}, {
	  query: {method:'GET', params:{}, isArray:true}
	});
}])

.factory('Clubs', ['$resource', function($resource){
	return $resource('/app/clubs/:clubId', {}, {
	  query: {method:'GET', params:{clubId: ''}, isArray:true},
	  update: {method:'PUT', params: {clubId: '@clubId'}},
	  save: {method:'POST', params: {clubId: ''}},
	});
}])

.factory('Player', ['$resource', function($resource){
	return $resource('/app/players/:pId', {}, {
	  query: {method:'GET', params:{pId: ''}, isArray:true},
	  update: {method:'PUT', params: {pId: '@pId'}},
	  save: {method:'POST', params: {pId: ''}},
	});
}])

.factory('Fixture', ['$resource', function($resource){
	return $resource('/app/fixtures/:pId', {}, {
	  query: {method:'GET', params:{pId: ''}, isArray:true},
	  update: {method:'PUT', params: {pId: '@pId'}},
	  save: {method:'POST', params: {pId: ''}},
	});
}])

.factory('Video', ['$resource', function($resource){
	return $resource('app/create/videos/:videoId', {}, {
//	  query: {method:'GET', params:{}, isArray:true},
	  post: {method:'POST',  params: {}},
        update: {method:'PUT', params: {videoId: '@videoId'}},
	});
}]);


