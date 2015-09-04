angular.module('dashboardServices', ['ngResource'])

.factory('Players', ['$resource', function($resource){
	return $resource('/app/players/', {}, {
	  query: {method:'GET', params:{}, isArray:true}
	});
}])

.factory('LibraryMusic', ['$resource', function($resource){
	return $resource('app/create/libraryMusic/', {}, {
	  query: {method:'GET', params:{}, isArray:true}
	});
}])

.factory('HistoryMusic', ['$resource', function($resource){
	return $resource('app/create/historyMusic/', {}, {
	  query: {method:'GET', params:{}, isArray:true}
	});
}])

.factory('HistoryImages', ['$resource', function($resource){
	return $resource('app/create/historyImages/', {}, {
	  query: {method:'GET', params:{}, isArray:true}
	});
}])

.factory('Images', ['$resource', function($resource){
	return $resource('pv/style/images.json', {}, {
	  query: {method:'GET', params:{}, isArray:true}
	});
}])

.factory('Create', ['$resource', function($resource){
	return $resource('app/create/initial/', {}, {
	  query: {method:'GET', params:{}, isArray:false}
	});
}])

.factory('VideoPreview', ['$resource', function($resource){
	return $resource('app/create/preview/', {}, {
	  query: {method:'GET', params:{}, isArray:false}
	});
}])

.factory('VideoCreate', ['$resource', function($resource){
	return $resource('app/create/render/', {}, {
	  query: {method:'GET', params:{}, isArray:false}
	});
}])

.factory('Video', ['$resource', function($resource){
	return $resource('app/create/videos/:videoId', {}, {
//	  query: {method:'GET', params:{}, isArray:true},
	  post: {method:'POST',  params: {}},
        update: {method:'PUT', params: {videoId: '@videoId'}},
	});
}])

.factory('VideoMusic', ['$resource', function($resource){
	return $resource('app/create/:route/:musicId/', {}, {
//	  query: {method:'GET', params:{}, isArray:true},
	  post: {method:'POST',  params: {route:'music-detail'}},
        update: {method:'PUT', params: {route:'music-detail', musicId: '@musicId'}},
	});
}])

.factory('UrlMusic', ['$resource', function($resource){
	return $resource('app/create/uploadMusic/', {}, {
	  post: {method:'POST',  params: {}},
        update: {method:'PUT', params: {}},
	});
}])

.factory('UrlSlide', ['$resource', function($resource){
	return $resource('app/create/uploadSlide/', {}, {
	  post: {method:'POST',  params: {}},
        update: {method:'PUT', params: {}},
	});
}])

.factory('Credits', ['$resource', function($resource){
	return $resource('app/create/creditsSave/', {}, {
	  post: {method:'POST',  params: {}},
        update: {method:'PUT', params: {}},
	});
}])

.factory('VideoStyle', ['$resource', function($resource){
	return $resource('app/create/:route/:styleId/', {}, {
//	  query: {method:'GET', params:{route:'style',styleId: ''}, isArray:true},
	  post: {method:'POST',  params: {route:'style-detail'}},
        update: {method:'PUT', params: {route:'style-detail',styleId: '@styleId'}},
	});
}])

