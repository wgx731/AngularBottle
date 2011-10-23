/* App Controllers */

function NavCtrl(){
    this.activeTab = 'home';

    this.isActive = function(tabName) {
        return (this.activeTab == tabName) ? 'active' : '';
    };
}
NavCtrl.$inject = [];

function HomeCtrl($xhr){
  var self = this;
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
