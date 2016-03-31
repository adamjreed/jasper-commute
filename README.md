# jasper-commute
A plugin for Jasper that tells you how long your commute will be based on Google's DistanceMatrix API.

Written by Adam Reed

# Steps to install

* Clone the repository
```
git clone https://github.com/adamjreed/jasper-commute.git
```
* Copy the module file
```
cp jasper-commute/Commute.py <path to jasper modules dir>
```
* Add the following to your profile.yaml file
```
commute:
  api_key: 'Your Google API Key Here'
  home_address: '123 Home St, Beverly Hills, CA 90210'
  work_address: '456 Work Blvd, Beverly Hills, CA 90210'
```

# Trigger phrase
The plugin listens for the word "commute" so try something like this:
* How's my commute today?
* What does my commute look like?
* Tell me about my commute.