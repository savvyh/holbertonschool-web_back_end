const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  let calculateNumberStub;
  let consoleLogSpy;

  beforeEach(function() {
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    consoleLogSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    calculateNumberStub.restore();
    consoleLogSpy.restore();
  });

  it('should call Utils.calculateNumber with SUM, 100, and 20', function() {
    sendPaymentRequestToApi(100, 20);
    
    sinon.assert.calledOnce(calculateNumberStub);
    sinon.assert.calledWith(calculateNumberStub, 'SUM', 100, 20);
  });

  it('should log "The total is: 10" to console', function() {
    sendPaymentRequestToApi(100, 20);
    
    sinon.assert.calledOnce(consoleLogSpy);
    sinon.assert.calledWith(consoleLogSpy, 'The total is: 10');
  });
});
