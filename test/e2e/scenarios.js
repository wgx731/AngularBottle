describe('angular bottle example test', function() {

  beforeEach(function() {
    browser().navigateTo('/index.html');
  });


  it('should automatically redirect to /home when location hash/fragment is empty', function() {
    expect(browser().location().hash()).toBe("/home");
  });


  describe('home', function() {

    beforeEach(function() {
      browser().navigateTo('#/home');
    });


    it('should render home when user navigates to /home', function() {
      expect(element('ng\\:view h2').text()).
        toMatch(/Weather Information:/);
    });

  });

  describe('settings', function() {

    beforeEach(function() {
      browser().navigateTo('#/settings');
    });

    it('should render settings when user navigates to /settings', function() {
      expect(element('ng\\:view h2').text()).
        toMatch(/Choose country to see report:/);
    });

    it('should display Singapore weather report when I choose Singapore as preference', function(){
        select('location').option('Singapore');
        element('input:submit').click();
        sleep(2);
        expect(element('ng\\:view h2').text()).
        toMatch(/Weather Information:/);
        expect(element('ng\\:view p:nth-child(2)').text()).
        toMatch(/City: Singapore/);
    });
  });


});
