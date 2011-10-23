/* App Controllers */

function NavCtrl($location){
   var self = this;
   self.hash = $location.hash.substring(1,$location.hash.length);

   if (self.hash == 'home' || self.hash == 'settings' || self.hash ==
           'info'){
          self.activeTab = self.hash;
      }
   else{
          self.activeTab = 'home';
      }
   self.isActive = function(tabName) {
          return (self.activeTab == tabName) ? 'active' : '';
      };
}

function HomeCtrl($xhr){
  var self = this;
  self.warning_conditions = ['Chance of Storm','Thunderstorm','Light rain','Rain','Chance of TStorm','Chance of Rain'];
  self.show_alert = true;
  $xhr('GET', 'weather', function(code, response) {
    self.current_conditions = response['current_conditions'];
    self.forecast_information = response['forecast_information'];
    self.forecasts = response['forecasts'];
  });
}
HomeCtrl.$inject = ['$xhr'];

function SettingsCtrl($xhr){
  var self = this;
  $xhr('GET', 'countries', function(code, response) {
      self.countries = response['countries'];
  });
}
SettingsCtrl.$inject = ['$xhr'];

function InfoCtrl(){
}
InfoCtrl.$inject = [];
