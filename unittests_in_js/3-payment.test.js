const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  let calculateNumberSpy;

  beforeEach(function() {
    calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  });

  afterEach(function() {
    calculateNumberSpy.restore();
  });

  it('should call Utils.calculateNumber with SUM, 100, and 20', function() {
    sendPaymentRequestToApi(100, 20);
    
    sinon.assert.calledOnce(calculateNumberSpy);
    sinon.assert.calledWith(calculateNumberSpy, 'SUM', 100, 20);
  });
});
