# cs515 HM4

Yuhui Wang ywang513@stevens.edu

# 1. Bugs or issues
reset() doesn't stop a running timer
# 2. Resolved issuebugs and issue
The reset() method should also reset the _start_time if the timer is running, or it could stop the timer altogether.
