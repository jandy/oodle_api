import urllib
import simplejson

class oodle_listings:
    def __init__(self):
        self.base_url = "http://api.oodle.com/api/v2/listings"
    
    def retrieve(self):
        self.req_url = self.base_url +'?key=' + self.key+'&region='+self.region+'&category='+self.category+'&format=json&jsoncallback=none'
        listings_fp = urllib.urlopen(self.req_url)
        self.listings = simplejson.load(listings_fp)
        return self.listings['stat']

    def get_listings(self):
        return self.listings['listings']
    
    def get_error_details(self):
        self.listings['error']

if __name__=='__main__':
    sample_listings = oodle_listings()
    sample_listings.key = 'CA136C067C3D'
    sample_listings.region='chicago'
    sample_listings.category= 'vehicle/car'
    res = sample_listings.retrieve()
    if res == 'ok':
        print sample_listings.get_listings()
    elif res == 'fail':
        print 'Faild! could not retrive listings'
        print sample_listings.get_error_details()
    
