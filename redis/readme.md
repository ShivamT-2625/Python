Redis is an in-memory data storage

running redis through docker daemon :- 
  cmd:- "docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest"

  now the redis GUI is available at localhost:8001 port 

TO RUN THE CMD OF REDIS AT CMD :-
 ON CMD :- docker ps
 NOW :- docker exec -it container_id bash
 .... The cli opens then write cmd :- redis-cli to start interaction with the redis in local

 Storing Data convention for keys :- 
    set <entity>:<id> value

    nx :- stores value if key doesnt exist
    mget for multiple get operation
    incr <value> , value increases
    incrby <value> number , value increase by the number


List
 lpush inserting from left 
 rpush inserting from right 
syntax:- 
 lpush <key> value
 # can be implemented like stack and queue
   if lpush insert and rpush for remove then its QUEUE
   if lpush for insertion and deletion both then its PUSH

 # BLPOP , waits for the value to arrive until the timeout 
          if it arrives within the timeout it gets popped
          if not then it does return after the timeout 