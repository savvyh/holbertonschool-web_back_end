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

describe('Cart page', function() {
  const baseUrl = 'http://localhost:7865';

  it('should return correct status code when :id is a number', function(done) {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct result when :id is a number', function(done) {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 status code when :id is NOT a number', function(done) {
    request.get(`${baseUrl}/cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 status code when :id is negative', function(done) {
    request.get(`${baseUrl}/cart/-12`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 status code when :id is a decimal', function(done) {
    request.get(`${baseUrl}/cart/12.5`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return correct result for different cart IDs', function(done) {
    request.get(`${baseUrl}/cart/47`, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 47');
      done();
    });
  });
});
