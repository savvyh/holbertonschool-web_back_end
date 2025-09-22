import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const jobs = [
    { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
    { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
];

describe('createPushNotificationsJobs', () => {
    before(() => {
        queue.testMode.enter();
    });
    
    afterEach(() => {
        queue.testMode.clear();
    });
    
    after(() => {
        queue.testMode.exit();
    });
    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
    });

    it('should create jobs in the queue', () => {
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    });
});
