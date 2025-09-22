import kue from 'kue';

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    
    if (blacklistedNumbers.includes(phoneNumber)) {
        const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
        done(error);
        return;
    }
    
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    
    done();
}

queue.process('push_notification_code_2', function(job, done) {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
