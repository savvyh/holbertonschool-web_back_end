const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should return 6 when adding 3 and 3', function() {
    assert.strictEqual(calculateNumber(3, 3), 6);
  });

  it('should return 4 when adding 1 and 2.8', function() {
    assert.strictEqual(calculateNumber(1, 2.8), 4);
  });

  it('should return 5 when adding 1.2 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return 0 when adding 0 and 0', function() {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  it('should return -2 when adding -1 and -1', function() {
    assert.strictEqual(calculateNumber(-1, -1), -2);
  });

  it('should return -1 when adding -1.4 and 0.4', function() {
    assert.strictEqual(calculateNumber(-1.4, 0.4), -1);
  });

  it('should return 0 when adding -1.4 and 1.4', function() {
    assert.strictEqual(calculateNumber(-1.4, 1.4), 0);
  });
});
