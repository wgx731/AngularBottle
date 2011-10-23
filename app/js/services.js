/* http://docs.angularjs.org/#!angular.service */

/**
 * App service which is responsible for the main configuration of the app.
 */
angular.service('AngularBottleApp', function($route, $window) {

  $route.when('/home', {template: 'partials/home.html', controller: HomeCtrl });
  $route.when('/settings', {template: 'partials/settings.html', controller: SettingsCtrl });
  $route.when('/info', {template: 'partials/info.html', controller: InfoCtrl });
  $route.otherwise({redirectTo: '/home'});

  var self = this;

  self.$on('$afterRouteChange', function(){
    $window.scrollTo(0,0);
  });

}, {$inject:['$route', '$window'], $eager: true});
