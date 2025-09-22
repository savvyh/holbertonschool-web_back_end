import kue from 'kue';

const queue = kue.createQueue();

const jobData = 
    {
        phoneNumber: '123',
        message: 'message to be sent',
    };

const job = queue.create('push_notification_code', jobData);

job.on('created', function() {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', function() {
  console.log('Notification job completed');
});

job.on('failed', function() {
  console.log('Notification job failed');
});

job.save();