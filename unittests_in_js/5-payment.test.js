const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
  let consoleLogSpy;

  beforeEach(function() {
    consoleLogSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    consoleLogSpy.restore();
  });

  it('should log "The total is: 120" and call console.log once for 100, 20', function() {
    sendPaymentRequestToApi(100, 20);
    
    sinon.assert.calledOnce(consoleLogSpy);
    sinon.assert.calledWith(consoleLogSpy, 'The total is: 120');
  });

  it('should log "The total is: 20" and call console.log once for 10, 10', function() {
    sendPaymentRequestToApi(10, 10);
    
    sinon.assert.calledOnce(consoleLogSpy);
    sinon.assert.calledWith(consoleLogSpy, 'The total is: 20');
  });
});
