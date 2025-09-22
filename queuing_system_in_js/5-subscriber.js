import redis from 'redis';

const client = redis.createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function(error) {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.subscribe('holberton school channel');

client.on('message', function(channel, message) {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});