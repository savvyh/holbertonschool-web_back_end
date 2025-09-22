import kue from 'kue';

const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    for (const job of jobs) {
        const newJob = queue.create('push_notification_code_3', job);
        
        newJob.on('created', function() {
            console.log(`Notification job created: ${newJob.id}`);
        });
        
        newJob.on('complete', function() {
            console.log(`Notification job ${newJob.id} completed`);
        });
        
        newJob.on('failed', function(error) {
            console.log(`Notification job ${newJob.id} failed: ${error}`);
        });
        
        newJob.on('progress', function(progress) {
            console.log(`Notification job ${newJob.id} ${progress}% complete`);
        });
        
        newJob.save();
    }
}

export default createPushNotificationsJobs;
