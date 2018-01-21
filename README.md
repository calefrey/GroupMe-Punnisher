## Inspiration
We wanted to do something fairly simple, that people as inexperienced as us can have running by the end of the Hackathon, and mostly because we want it to be deployed in a very large group chat, lying in wait until its time to shine. 
## What it does
When a new message is added to the group chat, an HTTP POST is sent to the Heroku instance, which is parsed to retrieve the message. The message string is split apart into individual words, which are then compared against the tags in the pun database. If there is a match, the bot sends the relevant pun into the group chat after a 2-second "thinking" delay. Most of the puns are separated into 2 parts, and they are sent individually, 2 seconds apart. In the event that there are multiple puns associated with the tag, a random integer is chosen to determine the one to send. To send the message, an HTTP POST is sent to GroupMe's servers, inserting the glorious pun into the chat.

## How I built it
Flask web server running on Python on a Heroku free instance, linked to my GitHub where a CSV of puns and the relevant tags are stored.
## Challenges I ran into
Never developed anything to deploy on a cloud platform, and while we tried to use AWS Lambda, Heroku proved to be much easier. Also, the bot began to reply to itself, causing a cascading mass of messages to flood our devices.
## Accomplishments that I'm proud of
Actually finishing the project and having it work.
## What I learned
I learned how powerful Python really is, even though it is relatively simple, especially when combined with other packages, such as Flask. Additionally, even though we decided against using AWS, I discovered how many powerful tools they have available, where server uptime is never a concern. I think I will be using AWS for personal projects in the future.
## What's next for GroupMe Punnisher
Adding more puns, and maybe allowing one message to trigger multiple puns if there are multiple keywords. Additionally, the bot currently ignores messages in which the keyword ends in punctuation, which may be remedied using RegEx. We can add more features as well, such as different responses based on who sent the message, now that we have the template setup

## Join the Demo Group by following the link below. 
[GroupMe with the Punnisher](https://groupme.com/join_group/37601736/yjONen)  
The group will be deleted and the bot moved into its intended group at 5 pm on Sun Jan 21.

## The Team 
Matthew Chan, Samuel Minkin, and myself, Caleb Frey
