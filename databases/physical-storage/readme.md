## problem descriptions and why I'm solving them

- csv filescan: create a node in DBMS that sequentially reads from a csv and load into memory
    - important observations:
        - when coding the logic out, I have used OOP
            -  this prompted a question why:
                1) Objects have state management
                2) which means that its a container where we can load our file and call next and other methods
                3) all while maintaing state of all variables
                4) In procedural programming this will be much harder