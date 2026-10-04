## Pomodoro timer code for hacktime
import time
work_seconds = int(input('Enter'))
break_seconds = int(input('Enter'))
total_sessions = int(input('Enter'))

session = 0

while session < total_sessions:
    session = session + 1

    print("\n--------")
    print('Work session', session, 'of', total_sessions, 'started!goodluck!!:D')
    print('-----------')

    for seconds_left in range(work_seconds,0,-1):
        print('Work time remaining',seconds_left, 'seconds....', end = '/r')
        time.sleep(1)
    print('\nWork session complete, well done!')

    if session < total_sessions:
        print('\nTime for a quick', break_seconds,'-second break!!!')
        for seconds_left in range(break_seconds,0,-1):
            print('Break time remaining', seconds_left,'seconds',end = '\r')    
            time.sleep(1)
        print('\nBreak is over!')
    else:
        print('\n-------')
        print('All sessions complete,well done mate!')
        print('----------')    