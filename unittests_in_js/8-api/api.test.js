const request = require('request');
const { expect } = require('chai');

describe('Index page', function() {
  const baseUrl = 'http://localhost:7865';

  it('should return correct status code', function(done) {
    request.get(baseUrl, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct result', function(done) {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should return correct content type', function(done) {
    request.get(baseUrl, (error, response, body) => {
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });

  it('should return correct content length', function(done) {
    request.get(baseUrl, (error, response, body) => {
      expect(response.headers['content-length']).to.equal('29');
      done();
    });
  });
});
