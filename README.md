# Feel Inu

## Description

iOS (and potentially Android) application

users will take a photo of a dog, and send it out.  App will resize/compress/filter the image and ship it out to a server that hosts our model.

the model will classify the image into the following categories:

* Happy
* Sad
* Angry
* Sleepy
* Hungry
* Scared
(and maybe more)

## Plans and Things to Do:

Gather data (couldn't find particularly good data sets, but I could make one by just searching "sad dog", "happy dog" etc and resize/filter and construct our own data)
Develop Convolutional Neural Network (python?)
Host NN on server (Heroku?)
Develop iOS front end (XCode + swift)
Make requests from iOS app to server and display results
Make app pretty
