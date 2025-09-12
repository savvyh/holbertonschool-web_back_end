function calculateNumber(type, a, b) {
  const numberA = Math.round(a);
  const numberB = Math.round(b);

  switch (type) {
    case 'SUM':
      return numberA + numberB;
    case 'SUBTRACT':
      return numberA - numberB;
    case 'DIVIDE':
      if (numberB === 0) {
        return 'Error';
      }
      return numberA / numberB;
    default:
      return 'Error';
  }
}

module.exports = calculateNumber;
