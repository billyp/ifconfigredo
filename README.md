# ifconfigredo
It's a python script that dumps the current config and then reruns ifconfig to gather the new details.  Appropriate for switching networks.  

## What is this for?
It's a way to reboot the ethernet device via python. 

## Why did I do it this way?
I did this as a learning expereince.  I learned how to use the 'sh' function to call shell commands from within Python.  Most importantly, I did this to enable a discussion amongst my team mates on the topic.  

## Why are there two files?
Again, this was a learning experience.  When switching networks, there was an offset of time.  The 'ifconfig down' took longer than the 'ifconfig up' function.  This meant that the ifconfig down was still running when ifconfig up started.  The result was that the network was still down...  not the preferred result :)

The solution, create a second file, (more learning) and add a little delay(again, more learning).  The second file then ran, allowing for a known 'done' of the 'ifconfig down' function.  This allowed the delay in the second file to prevent the 'ifconfig up' from running too soon.

## Billy, this is all already solved by 'dhclient'
Uh, duh!  I know this, as well as a variety of other ways to solve this problem.  Again, I emphasize that the entire point of this exercise was to accomplish a goal, and learn while doing it.  

Thanks Github, thanks Linux and thanks to all the developers of the tools I used to learn more about this world!